# ==========================================
# Project 1: Rule-Based AI Chatbot
# ==========================================

print("=" * 50)
print("Welcome to the Rule-Based AI Chatbot!")
print("Type 'bye', 'exit', or 'quit' to end the chat.")
print("=" * 50)

# Knowledge Base (Dictionary)
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi! Nice to meet you.",
    "hey": "Hey! What can I do for you?",
    "good morning": "Good morning! Have a wonderful day.",
    "good afternoon": "Good afternoon!",
    "good evening": "Good evening!",

    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "I'm DecodeBot, your AI assistant.",
    "who are you": "I'm a simple rule-based AI chatbot.",
    "help": "You can greet me, ask my name, ask how I am, or say thanks.",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "what can you do": "I can answer predefined questions using rule-based logic.",
    "creator": "I was created as part of an AI training project.",
    "time": "Sorry, I cannot tell the current time yet.",
    "date": "Sorry, I cannot tell today's date yet."
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