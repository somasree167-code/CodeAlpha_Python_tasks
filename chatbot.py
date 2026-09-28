def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm a simple chatbot built using Python."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a nice day!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome!"
    else:
        return "Sorry, I don't understand that. Try saying hi, hello, or goodbye."


print("Simple Chatbot")
print("Type 'exit' to quit")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Bot:", response)
