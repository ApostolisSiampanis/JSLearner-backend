import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('service-account.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def upload_course(cid, title, description_short, description_long):
    try:
        course_ref = db.collection('courses').document(str(cid))
        course_ref.set({
            'title': title,
            'description_short': description_short,
            'description_long': description_long
        })
        print(f"Course {cid} uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload course {cid}: {e}")

def upload_lesson(cid, lid, title, theories_list, extra_info):
    try:
        lesson_ref = db.collection('courses').document(str(cid)).collection('lessons').document(str(lid))
        lesson_ref.set({
            'title': title,
            'theories_list': theories_list,
            'extra_info': extra_info
        })
        print(f"Lesson {lid} uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload lesson {lid}: {e}")

def upload_question(cid, lid, qid, question_type, hint, question_description, options, correct_answers):
    try:
        question_ref = db.collection('courses').document(str(cid)).collection('lessons').document(str(lid)).collection('questions').document(str(qid))
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

# Example usage
cid = 87
lid = 8702
qid_1 = 870205
qid_2 = 870206
qid_3 = 870207

# Upload a course
upload_course(cid, 'JavaScript Basics', 'Learn the basics of JavaScript', 'This course covers the fundamentals of JavaScript.')

# Upload a lesson
upload_lesson(cid, lid, 'Introduction to Variables',
              ['Variables are containers for storing data values.', 'In JavaScript, we use the var, let, or const keywords to declare variables.'],
              'For more information, visit: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types')

# Upload questions
upload_question(cid, lid, qid_1, 'multiple_choice', 'Remember the basics of variable declaration.',
                'Which keyword is used to declare a variable in JavaScript?',
                ['var', 'let', 'const', 'all of the above'], ['all of the above'])

upload_question(cid, lid, qid_2, 'true_false', 'Think about the mutability of variables declared with const.',
                'A variable declared with const can be reassigned.', [], ['false'])

upload_question(cid, lid, qid_3, 'fill_in_the_blanks', 'Pay attention to the syntax of variable declaration.',
                'Declare a variable named "x" with the value 10 using let.', [], ['let x = 10;'])

print("Data uploaded successfully!")
