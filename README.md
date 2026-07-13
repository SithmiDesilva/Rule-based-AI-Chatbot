
# 🤖 Rule-Based AI Chatbot

A simple Rule-Based AI Chatbot built using Python that responds to predefined user inputs. This project demonstrates the fundamentals of Artificial Intelligence using conditional logic and dictionary-based responses without relying on Machine Learning or Large Language Models.

---

## 📌 Project Overview

This chatbot simulates a basic conversation with users by matching predefined inputs to predefined responses. It is designed to help beginners understand how AI systems can make decisions using explicit rules before moving on to advanced AI concepts like Machine Learning and Natural Language Processing.

The chatbot supports continuous interaction until the user chooses to exit.

---

## ✨ Features

- Interactive command-line chatbot
- Continuous conversation loop
- Handles greetings and common questions
- Answers AI, science, technology, programming, and general knowledge questions
- Uses dictionary-based response lookup
- Supports exit commands (`bye`, `exit`, `quit`)
- Input sanitization using `strip()` and `lower()`
- Gracefully handles unknown questions

---

## 🛠 Technologies Used

- Python 3.19
- Dictionaries (Hash Maps)
- Conditional Statements
- Loops
- Basic AI Concepts

---

## 📂 Project Structure

```
AI-Chatbot/
│
├── main2.py        # Main chatbot program
├── README.md         # Project documentation
```

---

## 🚀 How It Works

1. Displays a welcome message.
2. Accepts user input.
3. Cleans the input by removing extra spaces and converting it to lowercase.
4. Searches for the input in the chatbot's knowledge base.
5. Displays the corresponding response.
6. Continues the conversation until the user enters an exit command.

---

## 💬 Example Conversation

```text
==================================================
Welcome to the Rule-Based AI Chatbot!
Type 'bye', 'exit', or 'quit' to end the chat.
==================================================

You: hello
Bot: Hello! How can I help you today?

You: what is ai
Bot: Artificial Intelligence enables machines to perform tasks that typically require human intelligence.

You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

You: bye
Bot: Goodbye! Have a great day!
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Rule-based-AI-Chatbot.git
```

### 2. Navigate to the Project Folder

```bash
cd Rule-based-AI-Chatbot
```

### 3. Run the Chatbot

```bash
python main2.py
```

or, if your system uses Python 3 explicitly:

```bash
python main2.py
```

---

## 📖 Knowledge Base

The chatbot currently responds to questions related to:

- Greetings
- Personal introduction
- Artificial Intelligence
- Machine Learning
- Python programming
- Technology
- Science
- Mathematics
- General knowledge
- Sports
- Everyday conversation

Unknown questions receive a default response asking the user to try another question.

---

## 🧠 AI Concepts Demonstrated

This project demonstrates several fundamental AI and programming concepts:

- Rule-Based Artificial Intelligence
- Decision Making
- Dictionary Lookup
- Input Processing
- Control Flow
- User Interaction
- Continuous Program Execution

---

## 📈 Future Improvements

Some ideas for extending this project include:

- Add support for multiple languages
- Implement fuzzy string matching
- Add text-to-speech functionality
- Display the current date and time
- Build a graphical user interface (GUI)
- Store conversation history
- Integrate with an AI language model
- Add voice input support

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

- Python programming
- Writing clean and readable code
- Using dictionaries for efficient data lookup
- Designing rule-based AI systems
- Building interactive console applications
- Problem-solving using conditional logic

## 📄 License

This project is created for educational and learning purposes.

---

⭐ If you found this project useful, consider giving it a star!
