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

## Related Repositories
**[JSLearner Mobile App](https://github.com/ApostolisSiampanis/JSLearner)**

The JSLearner Mobile App is the frontend interface for users to interact with the JSLearner platform. Built using Kotlin and Jetpack Compose for Android, the mobile app offers an engaging, interactive learning experience for users aiming to improve their JavaScript skills. It integrates seamlessly with the backend, utilizing Firebase Cloud Functions and Realtime Database to provide real-time data synchronization and user progress tracking.

The app enables users to access lessons, take quizzes, and monitor their progress on a personalized learning roadmap. It also allows users to compete with others on a global leaderboard, which is updated dynamically through this backend. The mobile app retrieves and stores user experience points, quiz scores, and authentication details, all managed securely by the backend infrastructure.

This frontend-backend collaboration ensures a smooth, cohesive learning environment, making JSLearner an effective tool for mastering JavaScript.

## Contributors

<table>
  <tr>
    <td align="center"><a href="https://github.com/ApostolisSiampanis"><img src="https://avatars.githubusercontent.com/u/75365398?v=4" width="100px;" alt="Apostolis Siampanis"/><br /><sub><b>Apostolis Siampanis</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/thkox"><img src="https://avatars.githubusercontent.com/u/79880468?v=4" width="100px;" alt="Theodore Koxanoglou"/><br /><sub><b>Theodore Koxanoglou</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/AlexanderCholis"><img src="https://avatars.githubusercontent.com/u/66769337?v=4" width="100px;" alt="Alexander Cholis"/><br /><sub><b>Alexander Cholis</b></sub></a><br /></td>
  </tr>
</table>

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
