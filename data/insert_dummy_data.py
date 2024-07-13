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


courses = [
    {
        'level': 'BEGINNER',
        'title': 'JavaScript Basics',
        'description_short': 'Learn the basics of JavaScript',
        'description_long': 'This course covers the fundamentals of JavaScript, including variables, data types, operators, and control flow.',
        'lessons': [
            {
                'title': 'Introduction to JavaScript',
                'theories_list': [
                    'JavaScript is a high-level, interpreted programming language.',
                    'It is one of the core technologies of the World Wide Web.',
                    'JavaScript can be used for both client-side (in web browsers) and server-side development (with Node.js).',
                    'JavaScript code is typically embedded in HTML pages or linked as external files.'
                ],
                'description': 'In this lesson, you will learn the basics of JavaScript and its role in web development.',
                'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide',
                'questions': [
                    {
                        'question_type': 'TRUE_FALSE',
                        'hint': 'JavaScript is a scripting language.',
                        'question_description': 'JavaScript is the same as Java.',
                        'options': [],
                        'correct_answers': ['false']
                    },
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'JavaScript is primarily used for web development.',
                        'question_description': 'What is JavaScript primarily used for?',
                        'options': ['Web development', 'Data Science', 'Game development', 'Machine Learning'],
                        'correct_answers': ['Web development']
                    },
                    {
                        'question_type': 'FILL_IN_THE_BLANKS',
                        'hint': 'Consider where JavaScript is commonly run.',
                        'question_description': 'JavaScript can run in the browser and on the ____.',
                        'options': [],
                        'correct_answers': ['server']
                    },
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Think about the file extension for JavaScript code.',
                        'question_description': 'What is the file extension for JavaScript code?',
                        'options': ['.js', '.java', '.py', '.html'],
                        'correct_answers': ['.js']
                    },
                    {
                        'question_type': 'FILL_IN_THE_BLANKS',
                        'hint': 'Consider how you embed JavaScript in HTML.',
                        'question_description': 'The ____ tag is used to embed JavaScript code in an HTML file.',
                        'options': [],
                        'correct_answers': ['<script>']
                    },
                ]
            },
            {
                'title': 'Variables and Data Types',
                'theories_list': [
                    'Variables are containers for storing data values.',
                    'In JavaScript, we use the `var`, `let`, or `const` keywords to declare variables.',
                    'JavaScript supports different data types like string, number, boolean, null, undefined, object, and symbol.',
                    'Strings are for text, numbers for numeric values, booleans for true/false, and objects for collections of data.'
                ],
                'description': 'In this lesson, you will learn the basics of JavaScript and its role in web development.',
                'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide',
                'questions': [
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Think about the keywords used to declare variables.',
                        'question_description': 'Which keyword is used to declare a variable in JavaScript?',
                        'options': ['var', 'let', 'const', 'all of the above'],
                        'correct_answers': ['all of the above']
                    },
                    {
                        'question_type': 'TRUE_FALSE',
                        'hint': 'Consider the mutability of variables.',
                        'question_description': 'A variable declared with `const` can be reassigned.',
                        'options': [],
                        'correct_answers': ['false']
                    },
                    {
                        'question_type': 'FILL_IN_THE_BLANKS',
                        'hint': 'Pay attention to the syntax of variable declaration.',
                        'question_description': 'Declare a variable named "message" and assign it the string value "Hello, world!".',
                        'options': [],
                        'correct_answers': ['let message = "Hello, world!";', 'var message = "Hello, world!";', 'const message = "Hello, world!";']
                    },
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Think about the data type used for storing whole numbers.',
                        'question_description': 'Which data type is used to represent whole numbers in JavaScript?',
                        'options': ['string', 'number', 'boolean', 'object'],
                        'correct_answers': ['number']
                    },
                    {
                        'question_type': 'TRUE_FALSE',
                        'hint': 'Consider the difference between null and undefined.',
                        'question_description': 'In JavaScript, `null` and `undefined` represent the same thing.',
                        'options': [],
                        'correct_answers': ['false']
                    }
                ]
            }
        ]
    },
    {
        'level': 'BEGINNER',
        'title': 'JavaScript Basics',
        'description_short': 'Learn the basics of JavaScript',
        'description_long': 'This course covers the fundamentals of JavaScript, including variables, data types, operators, and control flow.',
        'lessons': [
            {
                'title': 'Introduction to JavaScript',
                'theories_list': [
                    'JavaScript is a high-level, interpreted programming language.',
                    'It is one of the core technologies of the World Wide Web.',
                    'JavaScript can be used for both client-side (in web browsers) and server-side development (with Node.js).',
                    'JavaScript code is typically embedded in HTML pages or linked as external files.'
                ],
                'description': 'In this lesson, you will learn the basics of JavaScript and its role in web development.',
                'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide',
                'questions': [
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'JavaScript is primarily used for web development.',
                        'question_description': 'What is JavaScript primarily used for?',
                        'options': ['Web development', 'Data Science', 'Game development', 'Machine Learning'],
                        'correct_answers': ['Web development']
                    },
                    {
                        'question_type': 'TRUE_FALSE',
                        'hint': 'JavaScript is a scripting language.',
                        'question_description': 'JavaScript is the same as Java.',
                        'options': [],
                        'correct_answers': ['false']
                    },
                    {
                        'question_type': 'FILL_IN_THE_BLANKS',
                        'hint': 'Consider where JavaScript is commonly run.',
                        'question_description': 'JavaScript can run in the browser and on the ____.',
                        'options': [],
                        'correct_answers': ['server']
                    },
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Think about the file extension for JavaScript code.',
                        'question_description': 'What is the file extension for JavaScript code?',
                        'options': ['.js', '.java', '.py', '.html'],
                        'correct_answers': ['.js']
                    },
                    {
                        'question_type': 'FILL_IN_THE_BLANKS',
                        'hint': 'Consider how you embed JavaScript in HTML.',
                        'question_description': 'The ____ tag is used to embed JavaScript code in an HTML file.',
                        'options': [],
                        'correct_answers': ['<script>']
                    }
                ]
            },
            {
                'title': 'Variables and Data Types',
                'theories_list': [
                    'Variables are containers for storing data values.',
                    'In JavaScript, we use the `var`, `let`, or `const` keywords to declare variables.',
                    'JavaScript supports different data types like string, number, boolean, null, undefined, object, and symbol.',
                    'Strings are for text, numbers for numeric values, booleans for true/false, and objects for collections of data.'
                ],
                'description': 'In this lesson, you will learn the basics of JavaScript and its role in web development.',
                'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide',
                'questions': [
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Think about the keywords used to declare variables.',
                        'question_description': 'Which keyword is used to declare a variable in JavaScript?',
                        'options': ['var', 'let', 'const', 'all of the above'],
                        'correct_answers': ['all of the above']
                    },
                    {
                        'question_type': 'TRUE_FALSE',
                        'hint': 'Consider the mutability of variables.',
                        'question_description': 'A variable declared with `const` can be reassigned.',
                        'options': [],
                        'correct_answers': ['false']
                    },
                    {
                        'question_type': 'FILL_IN_THE_BLANKS',
                        'hint': 'Pay attention to the syntax of variable declaration.',
                        'question_description': 'Declare a variable named "message" and assign it the string value "Hello, world!".',
                        'options': [],
                        'correct_answers': ['let message = "Hello, world!";', 'var message = "Hello, world!";',
                                            'const message = "Hello, world!";']
                    },
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Think about the data type used for storing whole numbers.',
                        'question_description': 'Which data type is used to represent whole numbers in JavaScript?',
                        'options': ['string', 'number', 'boolean', 'object'],
                        'correct_answers': ['number']
                    },
                    {
                        'question_type': 'TRUE_FALSE',
                        'hint': 'Consider the difference between null and undefined.',
                        'question_description': 'In JavaScript, `null` and `undefined` represent the same thing.',
                        'options': [],
                        'correct_answers': ['false']
                    }
                ]
            }
        ]
    },
    {
        'level': 'INTERMEDIATE',
        'title': 'Intermediate JavaScript',
        'description_short': 'Deepen your understanding of JavaScript',
        'description_long': 'This course covers intermediate JavaScript topics.',
        'lessons': [
            {
                'title': 'Object-Oriented Programming (OOP) in JavaScript',
                'theories_list': [
                    'JavaScript supports OOP through prototypes and classes.',
                    'Classes provide a blueprint for creating objects.',
                    'Objects are instances of classes and can have properties and methods.'
                ],
                'description': 'In this lesson, you will learn the basics of JavaScript and its role in web development.',
                'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide',
                'questions': [
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Consider the keywords used for OOP.',
                        'question_description': 'Which keyword is used to define a class in JavaScript?',
                        'options': ['function', 'class', 'object', 'constructor'],
                        'correct_answers': ['class']
                    },
                    {
                        'question_type': 'TRUE_FALSE',
                        'hint': 'Think about the relationship between classes and objects.',
                        'question_description': 'An object is an instance of a class.',
                        'options': [],
                        'correct_answers': ['true']
                    },
                    {
                        'question_type': 'FILL_IN_THE_BLANKS',
                        'hint': 'Consider the syntax for creating an object.',
                        'question_description': 'Create an object named "person" with a property "name" set to "Alice".',
                        'options': [],
                        'correct_answers': ['const person = { name: "Alice" };']
                    },
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Think about the purpose of the constructor method.',
                        'question_description': 'What is the purpose of the constructor method in a class?',
                        'options': ["To initialize the object's properties", "To define the object's methods",
                                    'To create a new instance of the class',
                                    'To inherit properties from another class'],
                        'correct_answers': ["To initialize the object's properties"]
                    },
                    {
                        'question_type': 'TRUE_FALSE',
                        'hint': 'Consider the concept of inheritance in OOP.',
                        'question_description': 'JavaScript supports multiple inheritance.',
                        'options': [],
                        'correct_answers': ['false']
                    },
                ]
            },
            {
                'title': 'Asynchronous JavaScript',
                'theories_list': [
                    'JavaScript is single-threaded, but it can handle asynchronous operations using callbacks, promises, and async/await.',
                    'Callbacks are functions passed as arguments to other functions and executed later.',
                    'Promises represent the eventual result of an asynchronous operation.',
                    'Async/await provides a cleaner syntax for working with promises.'
                ],
                'description': 'In this lesson, you will learn the basics of JavaScript and its role in web development.',
                'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide',
                'questions': [
                    {
                        'question_type': 'TRUE_FALSE',
                        'hint': "Think about the nature of JavaScript's execution model.",
                        'question_description': 'JavaScript is a multi-threaded language.',
                        'options': [],
                        'correct_answers': ['false']
                    },
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Consider the order of execution in asynchronous code.',
                        'question_description': 'Which of the following is used to handle asynchronous operations in JavaScript?',
                        'options': ['Callbacks', 'Promises', 'Async/await', 'All of the above'],
                        'correct_answers': ['All of the above']
                    },
                    {
                        'question_type': 'FILL_IN_THE_BLANKS',
                        'hint': 'Consider the syntax for creating a promise.',
                        'question_description': 'Create a promise that resolves with the value "Success" after 1 second.',
                        'options': [],
                        'correct_answers': [
                            'const promise = new Promise((resolve, reject) => { setTimeout(() => resolve("Success"), 1000); });']
                    },
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Think about the purpose of the "catch" block in a promise chain.',
                        'question_description': 'What is the purpose of the "catch" block in a promise chain?',
                        'options': ['To handle successful promise resolutions', 'To handle promise rejections',
                                    'To transform the resolved value of a promise', 'To create a new promise'],
                        'correct_answers': ['To handle promise rejections']
                    },
                    {
                        'question_type': 'TRUE_FALSE',
                        'hint': 'Consider the relationship between async/await and promises.',
                        'question_description': 'Async/await is built on top of promises.',
                        'options': [],
                        'correct_answers': ['true']
                    }
                ]
            }
        ]
    },
    {
        'level': 'ADVANCED',
        'title': 'Asynchronous JavaScript',
        'description_short': 'Master asynchronous operations in JavaScript',
        'description_long': 'This course covers advanced asynchronous JavaScript concepts like callbacks, promises, async/await, and error handling.',
        'lessons': [
            {
                'title': 'Callbacks and Promises',
                'theories_list': [
                    'Callbacks are functions passed as arguments to other functions, executed later.',
                    'Promises represent the eventual result of an asynchronous operation.',
                    'Promises can be chained to handle sequential asynchronous tasks.'
                ],
                'description': 'In this lesson, you will learn the basics of JavaScript and its role in web development.',
                'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide',
                'questions': [
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Consider the order of execution in asynchronous code.',
                        'question_description': 'Which of the following is NOT a way to handle asynchronous operations in JavaScript?',
                        'options': ['Callbacks', 'Promises', 'Async/await', 'Threads'],
                        'correct_answers': ['Threads']
                    },
                    {
                        'question_type': 'TRUE_FALSE',
                        'hint': 'Think about the states a promise can be in.',
                        'question_description': 'A promise can be in one of three states: pending, fulfilled, or rejected.',
                        'options': [],
                        'correct_answers': ['true']
                    },
                    {
                        'question_type': 'FILL_IN_THE_BLANKS',
                        'hint': 'Consider the method used to handle a fulfilled promise.',
                        'question_description': 'The ____ method is used to handle the successful resolution of a promise.',
                        'options': [],
                        'correct_answers': ['then']
                    }
                ]
            },
            {
                'title': 'Async/Await and Error Handling',
                'theories_list': [
                    'Async/await provides a cleaner syntax for working with promises.',
                    'The async keyword is used to declare a function that returns a promise.',
                    'The await keyword is used to pause execution until a promise is resolved.',
                    'Error handling in async/await is done using try...catch blocks.'
                ],
                'description': 'In this lesson, you will learn the basics of JavaScript and its role in web development.',
                'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide',
                'questions': [
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Consider the syntax of async functions.',
                        'question_description': 'How do you declare an async function in JavaScript?',
                        'options': ['async function myFunction() {}', 'function async myFunction() {}',
                                    'async myFunction() {}', 'function myFunction() async {}'],
                        'correct_answers': ['async function myFunction() {}']
                    },
                    {
                        'question_type': 'TRUE_FALSE',
                        'hint': 'Think about the return value of async functions.',
                        'question_description': 'Async functions always return a promise.',
                        'options': [],
                        'correct_answers': ['true']
                    },
                    {
                        'question_type': 'FILL_IN_THE_BLANKS',
                        'hint': 'Consider the keyword used to pause execution in async functions.',
                        'question_description': 'The ____ keyword is used to wait for a promise to resolve in an async function.',
                        'options': [],
                        'correct_answers': ['await']
                    },
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Think about the purpose of try...catch blocks.',
                        'question_description': 'What is the purpose of a try...catch block in an async function?',
                        'options': ['To handle the successful resolution of a promise',
                                    'To handle errors that occur during the async function',
                                    'To initiate a new promise', 'To transform the result of a promise'],
                        'correct_answers': ['To handle errors that occur during the async function']
                    },
                    {
                        'question_type': 'FILL_IN_THE_BLANKS',
                        'hint': 'Consider the syntax for handling errors in async functions.',
                        'question_description': 'Write an async function that fetches data from an API and handles potential errors using try...catch.',
                        'options': [],
                        'correct_answers': [
                            'async function fetchData() {\n  try {\n    const response = await fetch(\'https://api.example.com/data\');\n    const data = await response.json();\n    console.log(data);\n  } catch (error) {\n    console.error(\'Error fetching data:\', error);\n  }\n}']
                    }
                ]
            },
            {
                'title': 'Async/Await and Error Handling',
                'theories_list': [
                    'Async/await provides a cleaner syntax for working with promises.',
                    'The async keyword is used to declare a function that returns a promise.',
                    'The await keyword is used to pause execution until a promise is resolved.',
                    'Error handling in async/await is done using try...catch blocks.'
                ],
                'description': 'In this lesson, you will learn the basics of JavaScript and its role in web development.',
                'url': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide',
                'questions': [
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Consider the syntax of async functions.',
                        'question_description': 'How do you declare an async function in JavaScript?',
                        'options': ['async function myFunction() {}', 'function async myFunction() {}',
                                    'async myFunction() {}', 'function myFunction() async {}'],
                        'correct_answers': ['async function myFunction() {}']
                    },
                    {
                        'question_type': 'TRUE_FALSE',
                        'hint': 'Think about the return value of async functions.',
                        'question_description': 'Async functions always return a promise.',
                        'options': [],
                        'correct_answers': ['true']
                    },
                    {
                        'question_type': 'FILL_IN_THE_BLANKS',
                        'hint': 'Consider the keyword used to pause execution in async functions.',
                        'question_description': 'The ____ keyword is used to wait for a promise to resolve in an async function.',
                        'options': [],
                        'correct_answers': ['await']
                    },
                    {
                        'question_type': 'MULTIPLE_CHOICE',
                        'hint': 'Think about the purpose of try...catch blocks.',
                        'question_description': 'What is the purpose of a try...catch block in an async function?',
                        'options': ['To handle the successful resolution of a promise',
                                    'To handle errors that occur during the async function',
                                    'To initiate a new promise', 'To transform the result of a promise'],
                        'correct_answers': ['To handle errors that occur during the async function']
                    },
                    {
                        'question_type': 'FILL_IN_THE_BLANKS',
                        'hint': 'Consider the syntax for handling errors in async functions.',
                        'question_description': 'Write an async function that fetches data from an API and handles potential errors using try...catch.',
                        'options': [],
                        'correct_answers': [
                            'async function fetchData() {\n  try {\n    const response = await fetch(\'https://api.example.com/data\');\n    const data = await response.json();\n    console.log(data);\n  } catch (error) {\n    console.error(\'Error fetching data:\', error);\n  }\n}']
                    }
                ]
            }
        ]
    },
]

# Upload courses
for course_index, course in enumerate(courses, start=1):
    cid = f"{course_index:02}"
    upload_course(cid, course['level'], course['title'], course['description_short'], course['description_long'])

    # Upload lessons and their questions
    for lesson_index, lesson in enumerate(course['lessons'], start=1):
        lid = f"{cid}{lesson_index:02}"
        upload_lesson(cid, lid, lesson['title'], lesson['theories_list'], lesson['description'], lesson['url'])

        for question_index, question in enumerate(lesson['questions'], start=1):
            qid = f"{lid}{question_index:02}"
            upload_question(cid, lid, qid, question['question_type'], question['hint'],
                            question['question_description'],
                            question['options'], question['correct_answers'])

print("Data uploaded successfully!")
