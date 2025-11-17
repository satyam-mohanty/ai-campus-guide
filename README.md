📘 AI-Based Virtual Campus Guide

A rule-based intelligent agent designed to assist students with campus-related queries such as department locations, lab timings, and faculty information.
The project includes both a Command Line Interface (CLI) version and a Tkinter-based GUI prototype.

This system aligns with core AI concepts from Introduction to AI & Intelligent Agents, demonstrating reflex-based agent behavior, knowledge representation, and natural language preprocessing.

**🚀 Features**
Time-based greeting (on start and exit)
Entity detection using fuzzy matching (handles spelling mistakes)
Intent detection (location, timing, HOD queries)
Rule-based response system
Modular Python backend
Tkinter GUI prototype
CLI version fully functional
Extensible knowledge base using Python dictionaries
Clean architecture with separate logic, utilities, and data files

**🧠 How the System Works**
**1. Text Normalization**

User input is cleaned using regex, lowercasing, and whitespace handling.

**2. Entity Detection**

The system matches user queries with campus entities using:
fuzzywuzzy
python-Levenshtein
This enables detection even with spelling errors.

**3. Intent Classification**

Simple keyword-based intent recognition:
“where” → location queries
“when” → timing queries
“who” → HOD/faculty queries

**4. Response Generation**

Responses are generated using structured KB values:
locations
hours
HOD names

**🖥️ Installation & Setup**
1. Install Python Dependencies
pip install fuzzywuzzy python-Levenshtein

**▶️ Running the Project**
To run the GUI
python bot_gui.py

To run CLI Version
python bot_cli.py

**🧩 Technologies Used**
**Backend**
Python
fuzzywuzzy
python-Levenshtein

**Frontend**
will update when done


**🎨 UI Notes**

The current GUI uses Tkinter, which limits modern UI design.

**A planned upgrade includes:**

JavaScript-based interactive chat interface
Modern styling using CSS
Node.js backend integration for real-time responses

**🔮 Future Enhancements:**

Replace dictionary KB with LLM-powered responses
Real-time campus data from APIs
Voice input and text-to-speech
Expanded campus details and services
Better UI using React, Vue, or Svelte
Electron desktop app version

**✨ Author**
Satyam Mohanty
