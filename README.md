# Language Learning Web App

This is a language learning web application built using Python, Flask, and SQLite. The app offers users a platform to learn a new language through different categories: vocabulary, grammar, and images. Each of these categories contains items that users can review and set their mastery level on.

## Features

- **Vocabulary & Grammar**: Users can add new vocabulary and grammar items to the app. Each item consists of a title and a description. Users can also set their mastery level for each item: "Show More", "Show Less", or "Mastered". These mastery levels affect how often the item is shown to the user in the future.

- **Images**: Users can add images to vocabulary and grammar items. Images are stored in the same directory in a folder named "images". The user needs to add paths to the image.

- **Reminders**: The app shows a random item from each category as a reminder when the user visits the page. The selection of the reminder item is weighted based on the user's mastery level, with items set to "Show More" being more likely to be selected.

- **User authentication**:  Allow users to create an account and save their progress.

## Installation

```sh
# Clone the repository
git clone https://github.com/kamra34/language_learning_platform.git
# Change into the directory
cd repository

# Install the required packages
pip install -r requirements.txt

# Run the application
flask run
````

# Future Plans
This is an ongoing project. In the future, we plan to add more features such as:

- Additional learning materials: Add more categories such as audio and video materials.
- Practice exercises: Implement practice exercises for users to test their knowledge.
- Progress tracking: Track and display the user progress over time.

Contributions to the project are welcome! Please feel free to create a pull request or open an issue.

# License
This project is licensed under the terms of the MIT license.
