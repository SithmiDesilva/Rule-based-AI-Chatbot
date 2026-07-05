print("Hi there! How can I assist you today?")

user_input = input("Please enter your question or request: ")
user_input = user_input.lower().strip()

if "who are you?" in user_input:
    print("I am an AI assistant here to help you with your questions and tasks.")
elif "what can you do?" in user_input:
    print("I can answer questions, provide information, and assist with various tasks.")
elif "help" in user_input:
    print("Sure! Please specify what you need help with.")
else:
    print("I'm sorry, I didn't understand that. Could you please rephrase your question or request?")

    