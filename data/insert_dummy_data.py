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
            'descriptionShort': description_short,
            'descriptionLong': description_long
        })
        print(f"Course {cid} uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload course {cid}: {e}")


def upload_lesson(cid, lid, title, theories_list, extra_info):
    try:
        lesson_ref = db.collection('courses').document(str(cid)).collection('lessons').document(str(lid))
        lesson_ref.set({
            'title': title,
            'theoriesList': theories_list,
            'extraInfo': extra_info
        })
        print(f"Lesson {lid} uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload lesson {lid}: {e}")


def upload_question(cid, lid, qid, question_type, hint, question_description, options, correct_answers):
    try:
        question_ref = db.collection('courses').document(str(cid)).collection('lessons').document(str(lid)).collection(
            'questions').document(str(qid))
        question_ref.set({
            'questionType': question_type,
            'hint': hint,
            'questionDescription': question_description,
            'options': options,
            'correctAnswers': correct_answers
        })
        print(f"Question {qid} uploaded successfully.")
    except Exception as e:
        print(f"Failed to upload question {qid}: {e}")


courses = [
    {
        'level': 'BEGINNER',
        'title': 'JavaScript Basics',
        'descriptionShort': 'Learn the basics of JavaScript',
        'descriptionLong': 'This course covers the fundamentals of JavaScript.',
        'lessons': [
            {
                'title': 'Introduction to JavaScript',
                'theoriesList': [
                    'JavaScript is a high-level, interpreted programming language.',
                    'It is one of the core technologies of the World Wide Web.',
                    'JavaScript can be used for both client-side and server-side development.'
                ],
                'extraInfo': 'For more information, visit: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction',
                'questions': [
                    {
                        'questionType': 'multiple_choice',
                        'hint': 'JavaScript is primarily used for web development.',
                        'questionDescription': 'What is JavaScript primarily used for?',
                        'options': ['Web development', 'Data Science', 'Game development', 'Machine Learning'],
                        'correctAnswers': ['Web development']
                    },
                    {
                        'questionType': 'true_false',
                        'hint': 'JavaScript is a scripting language.',
                        'questionDescription': 'JavaScript is the same as Java.',
                        'options': [],
                        'correctAnswers': ['false']
                    },
                    {
                        'questionType': 'fill_in_the_blanks',
                        'hint': 'Consider where JavaScript is commonly run.',
                        'questionDescription': 'JavaScript can run in the browser and on the ____.',
                        'options': [],
                        'correctAnswers': ['server']
                    },
                    # Add 2 more questions for this lesson...
                ]
            },
            {
                'title': 'Variables and Data Types',
                'theoriesList': [
                    'Variables are containers for storing data values.',
                    'In JavaScript, we use the var, let, or const keywords to declare variables.',
                    'JavaScript supports different data types like string, number, and boolean.'
                ],
                'extraInfo': 'For more information, visit: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types',
                'questions': [
                    {
                        'questionType': 'multiple_choice',
                        'hint': 'Think about the keywords used to declare variables.',
                        'questionDescription': 'Which keyword is used to declare a variable in JavaScript?',
                        'options': ['var', 'let', 'const', 'all of the above'],
                        'correctAnswers': ['all of the above']
                    },
                    {
                        'questionType': 'true_false',
                        'hint': 'Consider the mutability of variables.',
                        'questionDescription': 'A variable declared with const can be reassigned.',
                        'options': [],
                        'correctAnswers': ['false']
                    },
                    {
                        'questionType': 'fill_in_the_blanks',
                        'hint': 'Pay attention to the syntax of variable declaration.',
                        'questionDescription': 'Declare a variable named "x" with the value 10 using let.',
                        'options': [],
                        'correctAnswers': ['let x = 10;']
                    },
                    # Add 2 more questions for this lesson...
                ]
            },
            # Add 3-8 more lessons...
        ]
    },
    {
        'level': 'INTERMEDIATE',
        'title': 'Intermediate JavaScript',
        'descriptionShort': 'Deepen your understanding of JavaScript',
        'descriptionLong': 'This course covers intermediate JavaScript topics.',
        'lessons': [
            {
                'title': 'Functions in JavaScript',
                'theoriesList': [
                    'Functions are reusable blocks of code that perform a specific task.',
                    'Functions can take parameters and return values.',
                    'JavaScript supports different types of functions such as named, anonymous, and arrow functions.'
                ],
                'extraInfo': 'For more information, visit: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions',
                'questions': [
                    {
                        'questionType': 'multiple_choice',
                        'hint': 'Consider the syntax of function declaration.',
                        'questionDescription': 'How do you declare a function in JavaScript?',
                        'options': ['function myFunction() {}', 'def myFunction() {}', 'func myFunction() {}', 'myFunction: function() {}'],
                        'correctAnswers': ['function myFunction() {}']
                    },
                    {
                        'questionType': 'true_false',
                        'hint': 'Consider the scope of variables inside functions.',
                        'questionDescription': 'Variables declared inside a function are globally scoped.',
                        'options': [],
                        'correctAnswers': ['false']
                    },
                    {
                        'questionType': 'fill_in_the_blanks',
                        'hint': 'Consider the syntax of an arrow function.',
                        'questionDescription': 'Write an arrow function that takes two parameters and returns their sum.',
                        'options': [],
                        'correctAnswers': ['(a, b) => a + b']
                    },
                    # Add 2-3 more questions for this lesson...
                ]
            },
            # Add 4-9 more lessons...
        ]
    },
    # Add 13 more courses...
]

# Upload courses
for course_index, course in enumerate(courses, start=1):
    cid = f"{course_index:02}"
    upload_course(cid, course['level'], course['title'], course['descriptionShort'], course['descriptionLong'])

    # Upload lessons and their questions
    for lesson_index, lesson in enumerate(course['lessons'], start=1):
        lid = f"{cid}{lesson_index:02}"
        upload_lesson(cid, lid, lesson['title'], lesson['theoriesList'], lesson['extraInfo'])

        for question_index, question in enumerate(lesson['questions'], start=1):
            qid = f"{lid}{question_index:02}"
            upload_question(cid, lid, qid, question['questionType'], question['hint'], question['questionDescription'],
                            question['options'], question['correctAnswers'])

print("Data uploaded successfully!")
