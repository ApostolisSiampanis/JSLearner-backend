from typing import Any
from firebase_functions import db_fn
from firebase_admin import initialize_app, firestore, db
import asyncio

# Initialize the Firebase app and clients
app = initialize_app()
firestore_client = firestore.client()
realtime_db = db.reference()


@db_fn.on_value_written(reference=r"/users/{uid}/experience_score", region="us-central1")
async def update_leaderboard(event):
    """
    Triggered when a user's experience score is updated.
    """
    new_score = event.data.after
    uid = event.params['uid']

    try:
        # Fetch user details from Firestore
        user_ref = firestore_client.collection('users').document(uid)
        user_doc = user_ref.get()

        if user_doc.exists:
            user_data = user_doc.to_dict()
            firstname = user_data.get('first_name', 'Unknown')
            lastname = user_data.get('last_name', 'Unknown')
            initials = f"{firstname[0]}{lastname[0]}"

            # Define the new leaderboard entry
            leaderboard_entry = {
                'initials': initials,
                'score': new_score
            }

            # Check if the user exists in the rankings
            leaderboard_ref = realtime_db.child(f"leaderboard/{uid}")
            existing_entry = leaderboard_ref.get()

            if existing_entry:
                # Update only if the score has changed
                if existing_entry.get('score') != new_score:
                    leaderboard_ref.update(leaderboard_entry)
                    print(f"Leaderboard updated for user {uid} with new score {new_score}.")
            else:
                # Set the ranking in Realtime Database with initials and score
                leaderboard_ref.set(leaderboard_entry)
                print(f"Leaderboard entry created for user {uid} with score {new_score}.")
        else:
            print(f"User {uid} not found in Firestore.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
