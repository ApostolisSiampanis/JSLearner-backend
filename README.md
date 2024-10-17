# Educational Software (2024) - JSLearner Server

## Project Overview

The **JSLearner Backend** is a team assignment for creating the backend infrastructure for the [JSLearner Mobile App](https://github.com/thkox/educational-software_2024-JSLearner), developed as part of the "Educational Software" course, offered in the 8th semester of the 2023-2024 academic year at the University of Piraeus, Department of Informatics. This serverless backend, developed using Firebase Cloud Functions and hosted on Google Cloud, provides real-time data synchronization, experience tracking, and leaderboard management for the JSLearner app. It supports key functionalities required to monitor user progress, assess performance, and dynamically adjust content based on user experience.

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

### 1. Cloud Functions

- **Experience Score Updates:** Cloud Functions trigger events to update user scores and adjust their experience levels based on progress.
- **Automatic Level Adjustment:** Users are promoted or demoted between experience levels based on predefined thresholds (e.g., XP scores below 300 or above 1400).
- **Leaderboard Updates:** The leaderboard is updated dynamically as users gain or lose experience points, ensuring real-time competition.

## Setup Instructions

1. Clone the backend repository:
    ```bash
    git clone https://github.com/thkox/JSLearner-backend.git
    ```

2. Install dependencies and Firebase CLI tools:
    ```bash
    pip install -r requirements.txt
    firebase login
    firebase init
    ```

3. Deploy the functions to Firebase:
    ```bash
    firebase deploy --only functions
    ```

## Documentation and Resources

- Full project details can be found in the [Project-documentation.pdf](./docs/Project-documentation.pdf).

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
