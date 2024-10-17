# Educational Software (2024) - JSLearner Server

## Project Overview

The JSLearner Backend handles the backend logic for the JSLearner mobile app, providing real-time data synchronization, experience tracking, and leaderboard management. This serverless backend, developed using Firebase Cloud Functions and hosted on Google Cloud, supports all major functionalities required to track user progress, assess performance, and offer dynamic content based on user experience.

This backend was developed for the "Educational Software" course in the 8th semester at the University of Piraeus, Department of Informatics (Academic Year 2023-2024).

## Course Information

- **Institution:** University of Piraeus
- **Department:** Department of Informatics
- **Course:** Educational Software (2024)
- **Semester:** 8th

## Technologies Used

- Python
- Firebase Authentication
- Firebase Realtime Database
- Firestore
- Google Cloud

## Features

1. **Cloud Functions**

   - **Experience Score Updates:** Cloud Functions trigger events to update user scores and adjust their experience levels based on their progress.
   - **Automatic Level Adjustment:** Users are promoted or demoted between experience levels based on predefined thresholds (e.g., XP scores below 300 or above 1400).
   - **Leaderboard Updates:** The leaderboard is refreshed dynamically when users gain or lose experience points.

## Setup Instructions

1. Clone the backend repository:
    ```bash
    git clone https://github.com/thkox/JSLearner-backend.git
    ```

2. Install dependencies and Firebase CLI tools.
    ```bash
    pip install -r requirements.txt
    firebase login
    firebase init
    ```

3. Deploy the functions to Firebase:
    ```bash
    firebase deploy --only functions
    ```


### Front-end: [JSLearner](https://github.com/AlexanderCholis/JSLearner)
### Project Team:  [Apostolis Siampanis](https://github.com/ApostolisSiampanis) | [Theodoros Koxanoglou](https://github.com/thkox) | [Alexander Cholis](https://github.com/AlexanderCholis)
