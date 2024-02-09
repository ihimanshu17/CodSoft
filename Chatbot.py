import re

def simple_chatbot(user_input):
    # Define rules and responses
    rules = {
        r'hello|hi|hey': 'Hello! How can I help you?',
        r'how are you': 'I am a chatbot, so I don\'t have feelings, but thanks for asking!',
        r'your name|who are you': 'I am a simple rule-based chatbot.',
        r'bye|goodbye': 'Goodbye! Have a great day!',
        r'\b(?:thanks|thank you)\b': 'You\'re welcome!',
        r'.*': 'I didn\'t understand that. Can you please rephrase or ask another question?'
    }

    # Check user input against rules
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

# Main loop for the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = simple_chatbot(user_input)
    print("Chatbot:", response)
