# ==========================================
# Project 1: Rule-Based AI Chatbot
# ==========================================

print("=" * 50)
print("Welcome to the Rule-Based AI Chatbot!")
print("Type 'bye', 'exit', or 'quit' to end the chat.")
print("=" * 50)

# Knowledge Base (Dictionary)
responses = {

    # Greetings
    "hello": "Hello! How can I help you today?",
    "hi": "Hi! Nice to meet you!",
    "hey": "Hey there!",
    "good morning": "Good morning! Have a wonderful day!",
    "good afternoon": "Good afternoon!",
    "good evening": "Good evening!",
    "good night": "Good night! Sleep well!",
    "greetings": "Greetings! How may I assist you?",

    # Identity
    "what is your name": "My name is DecodeBot.",
    "who are you": "I'm DecodeBot, a rule-based AI chatbot.",
    "what are you": "I'm a chatbot built using Python.",
    "who created you": "I was created by a developer using Python.",
    "creator": "My creator is a Python developer.",
    "your name": "I'm DecodeBot.",

    # Well-being
    "how are you": "I'm doing great! Thanks for asking.",
    "how are you doing": "I'm functioning perfectly!",
    "how's it going": "Everything is running smoothly!",
    "are you okay": "Yes, I'm working perfectly.",

    # Help
    "help": "You can greet me, ask about me, ask for a joke, fun fact, or simple AI questions.",
    "what can you do": "I can answer predefined questions using rule-based logic.",
    "commands": "Try saying hello, ask my name, ask for a joke, or say bye.",
    "menu": "Available topics: Greetings, AI, Python, Math, Fun Facts, Jokes.",

    # Appreciation
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "thanks a lot": "You're very welcome!",
    "great": "I'm glad you liked it!",
    "awesome": "Thank you!",

    # Apology
    "sorry": "That's okay!",
    "my mistake": "No problem at all.",
    "oops": "Mistakes happen!",

    # AI Questions
    "what is ai": "Artificial Intelligence is the simulation of human intelligence by computers.",
    "what is machine learning": "Machine Learning allows computers to learn patterns from data.",
    "what is deep learning": "Deep Learning is a subset of Machine Learning using neural networks.",
    "what is python": "Python is a popular programming language used in AI, web development, and data science.",
    "what is chatbot": "A chatbot is a program that communicates with users through text or speech.",

    # Programming
    "favorite language": "I like Python because it's simple and powerful.",
    "what is programming": "Programming is the process of writing instructions for computers.",
    "what is coding": "Coding means writing computer programs.",
    "what is github": "GitHub is a platform used to host and manage code repositories.",

    # Fun
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "another joke": "Why do Java developers wear glasses? Because they don't C#.",
    "fun fact": "Did you know? The first computer bug was an actual moth!",
    "tell me something": "Python was named after Monty Python, not the snake!",
    "interesting fact": "The first website ever created is still online.",

    # Math
    "what is 2+2": "2 + 2 = 4.",
    "what is pi": "Pi is approximately 3.14159.",
    "what is zero": "Zero is the additive identity in mathematics.",
    "what is infinity": "Infinity represents something without any limit.",

    # Time and Date
    "time": "Sorry, I cannot access the current time.",
    "date": "Sorry, I cannot access today's date.",
    "day": "Sorry, I cannot determine today's day.",

    # General Knowledge
    "capital of sri lanka": "Sri Jayawardenepura Kotte is the administrative capital of Sri Lanka.",
    "capital of india": "New Delhi is the capital of India.",
    "capital of france": "Paris is the capital of France.",
    "largest ocean": "The Pacific Ocean is the largest ocean on Earth.",
    "largest planet": "Jupiter is the largest planet in our Solar System.",
    "smallest planet": "Mercury is the smallest planet in our Solar System.",
    "what is the capital of japan": "Tokyo is the capital of Japan.",
    "what is the capital of australia": "Canberra is the capital of Australia.",
    "who discovered gravity": "Sir Isaac Newton is credited with discovering gravity.",
    "who invented the telephone": "Alexander Graham Bell invented the telephone.",
    "who invented the computer": "Charles Babbage is known as the Father of the Computer.",
    "who invented python": "Python was created by Guido van Rossum in 1991.",
    "what is the tallest mountain": "Mount Everest is the tallest mountain in the world.",
    "what is the fastest animal": "The cheetah is the fastest land animal.",
    "what is the largest country": "Russia is the largest country in the world.",
    "what is the smallest country": "Vatican City is the smallest country in the world.",

    # Science
    "what is the sun": "The Sun is a star at the center of our Solar System.",
    "what is the moon": "The Moon is Earth's only natural satellite.",
    "why is the sky blue": "The sky appears blue because sunlight is scattered by Earth's atmosphere.",
    "why do we breathe": "We breathe to take in oxygen and remove carbon dioxide.",
    "what is water": "Water is a compound made of hydrogen and oxygen (H₂O).",
    "what is gravity": "Gravity is the force that attracts objects toward each other.",
    "how many planets are there": "There are eight planets in our Solar System.",
    "which planet is known as the red planet": "Mars is known as the Red Planet.",
    "which planet is closest to the sun": "Mercury is the closest planet to the Sun.",
    "which planet is known as the blue planet": "Earth is known as the Blue Planet.",

    # Technology
    "what is a computer": "A computer is an electronic device that processes data.",
    "what is the internet": "The Internet is a global network that connects computers worldwide.",
    "what is wifi": "Wi-Fi is a wireless technology used to connect devices to the Internet.",
    "what is software": "Software is a collection of programs that tell a computer what to do.",
    "what is hardware": "Hardware refers to the physical components of a computer.",
    "what is an operating system": "An operating system manages computer hardware and software resources.",
    "what is windows": "Windows is an operating system developed by Microsoft.",
    "what is linux": "Linux is a free and open-source operating system.",
    "what is ai": "Artificial Intelligence enables machines to perform tasks that typically require human intelligence.",
    "what is data science": "Data Science involves analyzing data to gain insights and support decision-making.",

    # Education
    "what is mathematics": "Mathematics is the study of numbers, quantities, shapes, and patterns.",
    "what is physics": "Physics is the study of matter, energy, motion, and forces.",
    "what is chemistry": "Chemistry is the study of substances and how they interact.",
    "what is biology": "Biology is the study of living organisms.",
    "what is history": "History is the study of past events.",
    "what is geography": "Geography is the study of Earth's landscapes, environments, and populations.",


    # Weather
    "how is the weather": "Sorry, I can't access live weather information.",
    "is it raining": "I can't check live weather yet.",

    # Motivation
    "motivate me": "Believe in yourself. Every expert was once a beginner.",
    "quote": "Success is the sum of small efforts repeated day after day.",
    "inspire me": "The best way to predict the future is to create it.",

    # Personal
    "do you sleep": "No, I work 24/7.",
    "do you eat": "No, I don't need food.",
    "do you have friends": "Every user is my friend!",
    "can you learn": "Not yet. I'm rule-based, so I only know predefined responses.",
    "are you intelligent": "I'm intelligent within the rules programmed into me.",

    # Farewell
    "bye": "Goodbye! Have a wonderful day!",
    "goodbye": "See you next time!",
    "see you": "Take care!",
    "see you later": "See you later! Stay safe!",
    "exit": "Goodbye!",
    "quit": "Session ended. Goodbye!"
}

# Exit commands
exit_commands = ["bye", "exit", "quit"]

# Continuous conversation
while True:

    # Get user input
    user_input = input("\nYou: ")

    # Input sanitization
    user_input = user_input.lower().strip()

    # Check for exit
    if user_input in exit_commands:
        print("Bot: Goodbye! Have a great day!")
        break

    # Get response
    response = responses.get(
        user_input,
        "Sorry, I don't understand that. Please try another question."
    )

    # Display response
    print("Bot:", response)