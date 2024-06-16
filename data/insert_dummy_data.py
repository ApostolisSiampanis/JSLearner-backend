import firebase_admin
from firebase_admin import credentials, firestore
import random

# Initialize Firebase Admin SDK
cred = credentials.Certificate('service-account.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


# Function to upload course
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


# Function to upload lesson
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


# Function to upload question
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


# Generate content and upload
course_titles = ["JavaScript Basics", "JavaScript Variables", "JavaScript Functions", "JavaScript Arrays",
                 "JavaScript Objects",
                 "JavaScript DOM Manipulation", "JavaScript Events", "JavaScript Asynchronous Programming",
                 "JavaScript Promises",
                 "JavaScript Fetch API", "JavaScript Classes", "JavaScript Modules", "JavaScript Error Handling",
                 "JavaScript Debugging", "JavaScript Advanced Concepts"]

course_descriptions_short = ["Learn the basics of JavaScript.", "Understand variables in JavaScript.",
                             "Learn about functions in JavaScript.",
                             "Understand how arrays work in JavaScript.", "Learn about objects in JavaScript.",
                             "Manipulate the DOM using JavaScript.",
                             "Handle events in JavaScript.", "Learn about asynchronous programming in JavaScript.",
                             "Understand promises in JavaScript.",
                             "Use the Fetch API to make HTTP requests.", "Understand JavaScript classes.",
                             "Learn about JavaScript modules.",
                             "Handle errors in JavaScript.", "Debug JavaScript code.",
                             "Master advanced JavaScript concepts."]

course_descriptions_long = [
    "This course covers the fundamentals of JavaScript, including syntax, data types, and basic programming concepts.",
    "This course dives into JavaScript variables, covering var, let, const, and scope.",
    "Learn how to define and invoke functions, understand function scope, and higher-order functions.",
    "Understand array operations, methods, and how to manipulate arrays in JavaScript.",
    "Learn about JavaScript objects, properties, methods, and inheritance.",
    "Explore how to interact with the DOM, traverse the DOM tree, and update elements dynamically.",
    "Understand event handling, event listeners, and how to manage events in JavaScript.",
    "Dive into asynchronous programming, callbacks, and the event loop in JavaScript.",
    "Learn about promises, how to create them, and handle asynchronous operations.",
    "Understand how to use the Fetch API for network requests and handle responses.",
    "Learn about JavaScript classes, constructors, and inheritance.",
    "Understand the concept of modules, how to export and import modules in JavaScript.",
    "Learn how to handle errors, throw exceptions, and use try-catch blocks.",
    "Explore debugging techniques, using breakpoints, and debugging tools.",
    "Master advanced JavaScript concepts like closures, prototypes, and async/await."]

for course_id in range(1, 16):  # 15 courses
    cid = str(course_id).zfill(2)
    upload_course(cid, course_titles[course_id - 1], course_descriptions_short[course_id - 1],
                  course_descriptions_long[course_id - 1])

    for lesson_number in range(1, 11):  # 10 lessons per course
        lid = f"{cid}{str(lesson_number).zfill(2)}"
        lesson_title = f"Lesson {lesson_number} of {course_titles[course_id - 1]}"
        theories_list = [
            f"Theory point {i} for lesson {lesson_number} of course {course_id}." for i in range(1, 6 + course_id)
            # Increasing theories length with course_id
        ]
        extra_info = f"Extra information for lesson {lesson_number}. For more details visit: https://example.com/{lesson_number}"

        upload_lesson(cid, lid, lesson_title, theories_list, extra_info)

        for question_number in range(1, 11):  # 10 questions per lesson
            qid = f"{lid}{str(question_number).zfill(2)}"
            question_type = random.choice(['multiple_choice', 'true_false', 'fill_in_the_blanks'])
            hint = f"Hint for question {question_number} of lesson {lesson_number}."
            question_description = f"Description for question {question_number} of lesson {lesson_number}."

            if question_type == 'multiple_choice':
                options = ['Option A', 'Option B', 'Option C', 'Option D']
                correct_answers = ['Option A']  # Placeholder, you can set it based on real content
            elif question_type == 'true_false':
                options = []
                correct_answers = ['true']  # Placeholder, you can set it based on real content
            elif question_type == 'fill_in_the_blanks':
                options = []
                correct_answers = [f"Correct answer {question_number}"]

            upload_question(cid, lid, qid, question_type, hint, question_description, options, correct_answers)

print("All data uploaded successfully!")
