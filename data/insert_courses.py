import json

import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('service-account.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


def upload_course(cid, level, title, description_short, description_long):
    try:
        course_ref = db.collection('courses').document(str(cid))
        course_ref.set({
            'level': level,
            'title': title,
            'description_short': description_short,
            'description_long': description_long
        })
        print(f"Course {cid} uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload course {cid}: {e}")


def upload_lesson(cid, lid, title, theories_list, description, url):
    try:
        lesson_ref = db.collection('courses').document(str(cid)).collection('lessons').document(str(lid))
        lesson_ref.set({
            'title': title,
            'theories_list': theories_list,
            'description': description,
            'url': url
        })
        print(f"Lesson {lid} uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload lesson {lid}: {e}")


def upload_question(cid, lid, qid, question_type, hint, question_description, options, correct_answers):
    try:
        question_ref = db.collection('courses').document(str(cid)).collection('lessons').document(str(lid)).collection(
            'questions').document(str(qid))
        question_ref.set({
            'question_type': question_type,
            'hint': hint,
            'question_description': question_description,
            'options': options,
            'correct_answers': correct_answers
        })
        print(f"Question {qid} uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload question {qid}: {e}")


# Load courses from JSON
with open('courses.json', 'r') as file:
    courses = json.load(file)

# Upload courses
for course_index, course in enumerate(courses, start=1):
    cid = f"{course_index:02}"
    upload_course(cid, course['level'], course['title'], course['description_short'], course['description_long'])

    # Upload lessons and their questions
    for lesson_index, lesson in enumerate(course['lessons'], start=1):
        lid = f"{cid}{lesson_index:02}"
        upload_lesson(cid, lid, lesson['title'], lesson['theories_list'], lesson['description'], lesson['url'])

        if lesson.get('questions') is not None:
            for question_index, question in enumerate(lesson['questions'], start=1):
                qid = f"{lid}{question_index:02}"
                upload_question(cid, lid, qid, question['question_type'], question['hint'],
                                question['question_description'],
                                question['options'], question['correct_answers'])
                pass
        else:
            print(f"Lesson '{lesson['title']}' does not have any questions.")


print("Data uploaded successfully!")
