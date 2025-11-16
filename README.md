AI-Based Virtual Campus Guide

A simple AI Reflex Agent (chatbot) built in Python and Tkinter for a university project. This agent uses rule-based logic and fuzzy string matching to understand user queries and provide information about campus departments, labs, and timings from a static knowledge base.

This project demonstrates the evolution from a basic command-line interface (CLI) to a clean, modern, and user-friendly graphical user interface (GUI).

Key Features

Simple Reflex Agent: The bot operates on a simple CONDITION-ACTION rule-based system.

Natural Language Input: Users can type questions in plain English.

Fuzzy String Matching: Uses fuzzywuzzy to handle common spelling mistakes (e.g., "libary" vs. "library").

Intent Recognition: Detects user intent (e.g., "where," "when," "who") based on keywords.

Modern GUI: A clean, responsive, and "premium" styled GUI built with Python's standard Tkinter library.

Modular Design: The core logic, knowledge base, and UI are separated, making the code easy to maintain and understand.

How to Run

1. Prerequisites

Python 3.6+

pip (Python package installer)

2. Setup

Clone the repository:

git clone [https://github.com/](https://github.com/)[YourUsername]/[YourRepoName].git
cd [YourRepoName]


Create a Virtual Environment (Recommended):

# Create a new environment named 'venv'
python -m venv venv

# Activate the environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


Install Dependencies:

pip install -r requirements.txt


3. Run the Application

To run the GUI version of the application, execute the main GUI script:

python bot_gui.py


(Note: File names may vary if you have renamed them, e.g., main.py or app.py)

The chat window will open, and you can begin interacting with the Virtual Campus Guide.
