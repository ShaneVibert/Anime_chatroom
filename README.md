FastAPI Anime Chat Application

This project is a real-time chat application built with FastAPI, which integrates with the AniList API to fetch a list of popular anime shows and allows users to join chat rooms based on these anime titles. The application provides a WebSocket-based communication system where users can chat in real-time about specific anime.

Table of Contents
- Project Overview
- Features
- Technologies Used
- Getting Started
- Prerequisites
- Installation
- Running Locally
- Testing
- Docker Setup
- API Documentation
- Endpoints
- Contributing
- License
- Acknowledgements


Project Overview

This project is a simple, real-time chat application that allows users to:

- Browse a list of popular anime shows.
- Join a chat room for a specific anime show.
- Send and receive messages in real-time in a chat room dedicated to the anime show they’re interested in.

The application uses FastAPI for the backend, WebSockets for real-time communication, and integrates with AniList to fetch anime data.

Features

Fetch anime data from AniList: The app pulls a list of anime shows, including their genres, descriptions, and cover images.

WebSocket-based chat rooms: Users can join a specific chat room for an anime and send messages in real time.

Message history: The app saves the chat history for each anime show, allowing users to see past messages when they join a chat room.

CORS-enabled: Supports cross-origin resource sharing, allowing frontend apps to connect with the backend.

Technologies Used
- FastAPI: Modern, fast web framework for building APIs with Python 3.6+ based on standard Python type hints.
- Uvicorn: ASGI server for serving the FastAPI app.
- WebSockets: Protocol used for real-time, two-way communication between the frontend and backend.
- Requests: HTTP library used to fetch data from the AniList API.
- Pydantic: Data validation and settings management using Python type annotations.
- Docker: Containerization of the application for easy deployment.
- Getting Started

Prerequisites

Before you begin, ensure you have the following installed:

Python 3.7+: The application requires Python version 3.7 or higher.

pip: Python's package installer, which comes with Python.

git: Version control system to manage your codebase.

Docker (optional): For containerized deployment.

Installation

Clone the repository

Copy code
- git clone https://github.com/yourusername/fastapi-anime-chat.git
cd fastapi-anime-chat

Create a virtual environment

It's best practice to use a virtual environment to isolate project dependencies:

bash
Copy code
python -m venv venv
Activate the virtual environment

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies

Install all necessary dependencies using pip:

bash
Copy code
pip install -r requirements.txt
Check the requirements

To ensure everything is installed correctly, you can verify that all dependencies are correctly installed:

bash
Copy code
pip list
Running Locally
Once the project is set up, you can run the application locally with Uvicorn:

Start the FastAPI server

Run the FastAPI application using Uvicorn:

bash
Copy code
uvicorn app.main:main --reload
The --reload flag enables auto-reloading, so the server will restart automatically when you make changes to the code.
Access the app

The app should now be running at http://127.0.0.1:8000.

Open your browser and visit http://127.0.0.1:8000 to view the interactive API docs powered by Swagger UI.
The WebSocket endpoint can be accessed using any WebSocket client, such as in the browser using JavaScript or through a tool like Postman.
Testing
Run tests with pytest

You can run the tests using pytest to ensure everything is working correctly:

bash
Copy code
pytest tests/
This will automatically find and run all the tests in the tests directory.

Docker Setup
If you prefer to run the application using Docker, follow these steps:

Build the Docker image

bash
Copy code
docker build -t fastapi-anime-chat .
Run the Docker container

bash
Copy code
docker run -p 8000:8000 fastapi-anime-chat
This will start the application and expose it on http://127.0.0.1:8000.

API Documentation
Endpoints
Here’s a list of the key endpoints available in the application:

GET /anime
Description: Fetches a list of popular anime.

Response: A list of anime shows with their details such as title, genres, description, and cover image.

Example response:

json
Copy code
{
  "anime": [
    {
      "id": 1,
      "title": "Naruto",
      "genres": ["Action", "Adventure"],
      "description": "Naruto is a ninja seeking to become the Hokage.",
      "coverImage": "https://example.com/naruto.jpg"
    },
    ...
  ]
}
GET /chat/{anime_id}
Description: Fetches the chat history for a specific anime by anime_id.

Response: A list of messages sent in the chat room for that anime.

Example response:

json
Copy code
{
  "chat_history": [
    {
      "user": "User1",
      "content": "This anime is amazing!",
      "timestamp": "2024-12-21T14:00:00Z"
    },
    ...
  ]
}
WebSocket /ws/{anime_id}
Description: Establishes a WebSocket connection for real-time chat in a specific anime chat room.

Request: Sends a JSON message with user, content, and timestamp.

Example message:

json
Copy code
{
  "user": "User1",
  "content": "Hello, anyone here?",
  "timestamp": "2024-12-21T14:05:00Z"
}
Response: Broadcasts the chat message to all connected clients in the same chat room.

Contributing
We welcome contributions to improve the app. Here are some ways you can help:

Bug Fixes: If you find any bugs, feel free to open an issue or submit a pull request with a fix.
Feature Requests: Suggest new features or improvements in the issues section.
Code Style: Please ensure that your code adheres to the existing code style. You can run flake8 for linting.
To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them.
Push to your forked repository and submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements

FastAPI: A modern web framework for building APIs.

Uvicorn: ASGI server for running FastAPI apps.

AniList: An excellent API for anime data, used to fetch anime information for this app.

Docker: Containerization of the app to make deployment easier.


