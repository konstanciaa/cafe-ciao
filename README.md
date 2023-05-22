# Cafe "Ciao"

Cafe "Ciao" is a Pyhton termninal app, which runs in the Code Institute mock terminal on Heroku.

Users can leave their review after visiting the cafe. The have to answer four questions by giving points from 1 to 5, where 1 is bad and 5 is good. The app saves users review and recommendations into Google Spreadsheet. It also analyses performance for the last five entries and shows areas for imrpovement.

[View the live project here.](https://cafe-ciao.herokuapp.com/)

![Am I responsive - screenshot](/docs/responsive.jpeg)

## How to use it
- Users answer four questions, by giving a point from 1 to 5, where 1 is bad and 5 is good.
- Users can see an average review score, based on their input.
- Users are invited to answer one more question. They can give their recommendations.

## Features
- Users are welcomed to leave a review after visiting the cafe "Ciao"

![a screenshot of the first screen](/docs/welcoming.jpeg)

- On the next screen users can read short instructions on how to answer the questions.

![instructions](/docs/instructions.jpeg)

- After a user answers the first question, the second question appears, and so on.

![four questions](/docs/four-questions.jpeg)

- If users type a letter or a number which is hihger than 5, they see a message which informs them about the mistake and reloads the question.

![invalid input number](/docs/invalid-input-number.jpeg)

- After users answered all four questions, they can see their average review score.

![average review score](/docs/average-score.jpeg)

- Users are invited to answer one more question, where they can write their recommendations on improvement. If a user is willing to give recommendations, they can type "yes" and proceed to the next screen.

![question about recommendations](/docs/recommends-question.jpeg)

- If users made a spelling mistake when typing "yes" or "no", they are informed with the short message and asked to enter their answer again.

![spelling mistake message](/docs/spelling-mistake.jpeg)

- Here users can freely type their recommendations.

![recommendations](/docs/recommendations.jpeg)

- On the last screen, users can see that their recommendation is taken into account. It was saved to a separate worksheet with the other recommendations. 
- Also users are able to see the analysis on performance and areas for improvement.

![last screen with feedback and analysis](/docs/feedback.jpeg)

- If users choose not to give recommendations, they may type "no" and see the following screen with the analysis.

![last screen with analysis without recommendations from the user](/docs/without-recommends.jpeg)


## Future features

- Analyze performance since opening
- Add more questions to the survey

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.

Steps for deployment:
- Fork or clone this repository
- Create a new Heroku app
- Set the buildpacks to **Python** and **NodeJS** in that order
- Link the Heroku app to the repository
- Click on **Deploy**

## User Experience
1. As a User, I want to understand the purpose of the web application.
2. As a User, I want to see clearly written instructions which explain what to do.

## Technologies used
- Python
- External libraries: gspread, statistics, os, time

## Testing
| **To test** | **Expected Result** |
| -------------------------------|----------------------------------|
|Open the app in different browsers. | The app works properly in different browsers: Chrome, Safari.
|Open it on a tablet and on a mobile phone. | It's responsive and looks good on a range of devices.
|Try to enter a letter or a number higher than 5, when answering first four questions. | The app shows error message and asks the question again.
|Try to answer all questions. | All quetsions work properly.

## Testing User Stories from User Experience Section
1. As a User, I want to understand the purpose of the web application.
- *Upon running the program, users are automatically greeted with a welcoming message, which gives clear idea of what it is about.*

2. As a User, I want to see clearly written instructions which explain what to do.
- *The second screen, which opens automatically after 5 seconds, contains short and clear instructions on how to answer questions in the survey.*

## Validator Testing
No errors were returned from [CI Python Linter](https://pep8ci.herokuapp.com/)

![a screenshot from Python Linter](/docs/validation.jpeg)


## Credits
- Code Institute for the deployment terminal
- The code to clear screen was taken from [GeeksforGeeks](https://www.geeksforgeeks.org/clear-screen-python/)
- The code for displaying countdown in terminal was taken from [this post on Stackoverflow](https://stackoverflow.com/questions/17220128/display-a-countdown-for-the-python-sleep-function)

