import re

greeting_patterns = [
    r"hi|hello|hey|hoedy",
    r"what's up|sup",
]

greeting_responses = [
    "Hello! How can I assist you today?",
    "Hi there! How can I help?",
]

name_patterns = [
    r"my name is (\w+)",
    r"i am (\w+)",
]

name_responses = [
    "Nice to meet you, {}!",
    "Hello, {}! How can I assist you?",
]

default_response = "I'm not sure how to respond to that. Please ask something else."

def chatbot_response(user_input):
    for pattern, response in zip(name_patterns, name_responses):
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            name = match.group(1)
            return response.format(name)
    
    for pattern, response in zip(greeting_patterns, greeting_responses):
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    
    return default_response

print("Chatbot: Hello! What's your name>")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:",response)