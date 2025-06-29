def chatbot():
    print("🤖 Chatbot: Hello! I'm your simple chatbot. Type 'bye' to end.\n")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hi there! How can I help you?")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm just a bunch of code, but I'm running great!")
        elif user_input == "what is your name":
            print("🤖 Chatbot: I'm CodeBot, your Python assistant.")
        elif user_input == "thank you":
            print("🤖 Chatbot: You're welcome!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day! 👋")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

chatbot()