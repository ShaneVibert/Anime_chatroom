from setuptools import setup, find_packages

setup(
    name="my_fastapi_project",  # Replace with your project name
    version="0.1.0",  # Your package version
    description="A FastAPI-based chat application",  # Short description
    author="Your Name",  # Your name or company
    author_email="youremail@example.com",  # Your email
    packages=find_packages(where="app"),  # The packages that should be included
    install_requires=[
        "fastapi",  # The FastAPI framework
        "uvicorn",  # Uvicorn for running the app
        "requests",  # Requests for making HTTP requests to AniList
        "pydantic",  # Pydantic for validation
    ],
    entry_points={
        'console_scripts': [
            'start-app = app.main:app',  # This makes `start-app` a CLI command
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
