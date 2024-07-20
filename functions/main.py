from firebase_functions import db_fn
from firebase_admin import initialize_app, firestore, db
import asyncio

app = initialize_app()
firestore_db = firestore.client()


@db_fn.on_value_written(reference=r"/users/{uid}/experience_score", region="us-central1")
def update_rankings(event):
    """
    Triggered when a user's experience score is updated.
    """
    new_score = event.data.after.val()
    uid = event.params['uid']

    # Call the asynchronous function
    asyncio.run(process_update(uid, new_score))


async def process_update(uid, new_score):
    try:
        # Fetch user details from Firestore
        user_ref = firestore_db.collection('users').document(uid)
        user_doc = user_ref.get()

        if user_doc.exists:
            user_data = user_doc.to_dict()
            firstname = user_data.get('first_name', 'Unknown')
            lastname = user_data.get('last_name', 'Unknown')

            # Update the rankings in Realtime Database
            ranking_ref = db.reference(f"rankings/{new_score}/{uid}")
            ranking_ref.set({
                'first_name': firstname,
                'last_name': lastname
            })

            print(f"Ranking updated for user {uid} with score {new_score}.")
        else:
            print(f"User {uid} not found in Firestore.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
