from typing import Any
from firebase_functions import db_fn
from firebase_admin import initialize_app, firestore, db
import asyncio

initialize_app()


@db_fn.on_value_written(reference=r"/users/{uid}/experience_score", region="us-central1")
def change_user_score(event):
    """
    Triggered when a user's experience score is updated.
    """
    new_score = event.data.after
    uid = event.params['uid']

    # Call the asynchronous function
    asyncio.run(update_leaderboard(uid, new_score))
    asyncio.run(check_and_update_user_experience(uid, new_score))


async def update_leaderboard(uid, new_score) -> Any:
    """
    Process the update to the leaderboard.
    """
    try:
        # Fetch user details from Firestore
        user_ref = firestore.client().collection('users').document(uid)
        user_doc = user_ref.get()

        if user_doc.exists:
            user_data = user_doc.to_dict()
            firstname = user_data.get('first_name', 'Unknown')
            lastname = user_data.get('last_name', 'Unknown')

            # Define the leaderboard entry
            leaderboard_ref = db.reference(f"leaderboard/{uid}")
            leaderboard_entry = {
                'firstname': firstname,
                'lastname': lastname,
                'score': new_score
            }

            # Update the leaderboard entry in Realtime Database
            leaderboard_ref.set(leaderboard_entry)
            print(f"Leaderboard updated for user {uid} with score {new_score}.")
        else:
            print(f"User {uid} not found in Firestore.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


async def check_and_update_user_experience(uid, new_score) -> Any:
    """
    Check if the user has reached a certain experience level.
    """
    try:
        experience_level_ref = db.reference(f"users/{uid}/experience_level")
        experience_level = experience_level_ref.get()

        new_experience_level = experience_level

        if experience_level is 'A_LOT_OF_EXPERIENCE':
            if new_score < 1000:
                new_experience_level = 'SOME_EXPERIENCE'
        elif experience_level is 'SOME_EXPERIENCE':
            if new_score < 300:
                new_experience_level = 'NO_EXPERIENCE'
            elif new_score >= 1400:
                new_experience_level = 'A_LOT_OF_EXPERIENCE'
        elif experience_level is 'NO_EXPERIENCE':
            if new_score >= 600:
                new_experience_level = 'SOME_EXPERIENCE'

        if new_experience_level != experience_level:
            experience_level_ref.set(new_experience_level)
            print(f"User {uid} has reached {new_experience_level} level.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
