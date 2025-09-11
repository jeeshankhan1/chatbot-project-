# this is a code simple chatbot
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What's on your mind?",
    "how are you": "I'm a chatbot, so I don't have feelings, but I'm ready to help!",
    "what is your name": "I am a simple chatbot created to assist you.",
    "bye": "Goodbye! Have a great day!"
}

def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. What's your name?")
    user_name = input("You: ")
    print(f"Chatbot: Nice to meet you, {user_name}!")
    print("Chatbot: You can type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye! Hope to talk to you again soon.")
            break
        found_response = False
        for keyword in responses:
            if keyword in user_input:
                print(f"Chatbot: {responses[keyword]}")
                found_response = True
                break
        if not found_response:
            print("Chatbot: I'm sorry, I don't understand that. Can you rephrase?")
if == "main":
    chatbot()