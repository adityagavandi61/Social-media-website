# Dashavatar Cultural Drama Social Media Website

Welcome to the Dashavatar Cultural Drama Social Media Website project! This project was developed as a college project aimed at showcasing the Dashavatar cultural drama to a global audience through a social media platform. Not only does it serve as a platform for sharing cultural content, but it also incorporates innovative features to engage users in an interactive manner. This project was awarded the 2nd prize for its innovative idea in leveraging social media for cultural promotion.

## Introduction

The Dashavatar Cultural Drama Social Media Website is a Django-based application that allows users to interact with each other through posts, likes, comments, and follows. The platform is designed to have two types of users:

1. **Profile User:** These users are the creators and uploaders of cultural drama content. They can upload posts showcasing different aspects of the Dashavatar cultural drama, including videos, images.

2. **Viewer User:** These users can view the posts uploaded by profile users, like them, leave comments, and follow their favorite profiles to stay updated with their latest uploads.

## Features

- **User Authentication:** Secure user authentication system allowing users to sign up, log in, and log out.
- **Profile Creation:** Profile users can create their profiles, providing information about themselves and their involvement in Dashavatar cultural drama.
- **Post Creation:** Profile users can upload posts containing multimedia content such as videos, images, and text related to Dashavatar cultural drama.
- **Interaction:** Viewer users can like posts, leave comments, and follow profile users to stay connected with their updates.
- **News Feed:** A personalized news feed for viewer users displaying posts from profiles they follow, allowing them to discover and engage with content related to Dashavatar cultural drama.

## Technologies Used

- **Django:** Python-based web framework for rapid development and clean design.
- **SQLite3:** Lightweight and easy-to-set-up relational database system for storing user data and post content.
- **HTML, CSS, JavaScript:** Frontend technologies for building the user interface and enhancing user experience.
- **Bootstrap:** Frontend framework for responsive and visually appealing web design.

## Installation

To run this project locally, follow these steps:

1. Clone the repository to your local machine using `git clone <repository-url>`.
2. Navigate to the project directory.
3. Set up a virtual environment to manage dependencies (`python -m venv venv`).
4. Activate the virtual environment (`source venv/bin/activate` on Unix/Linux, `venv\Scripts\activate` on Windows).
5. Install dependencies from `requirements.txt` using `pip install -r requirements.txt`.
6. Apply migrations to set up the SQLite3 database (`python manage.py migrate`).
7. Create a superuser for accessing the Django admin panel (`python manage.py createsuperuser`).
8. Start the development server (`python manage.py runserver`).

## Usage

Once the development server is running, you can access the website by navigating to `http://localhost:8000` in your web browser. 

- Profile users can sign up, create their profiles, and upload posts showcasing Dashavatar cultural drama.
- Viewer users can sign up or log in, browse through posts, like them, leave comments, and follow profile users to stay updated.
