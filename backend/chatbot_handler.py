import random

# Predefined chatbot responses (For now, we will replace this with AI later)
responses = {
    "hello": ["Hi there! How can I assist you?", "Hello! What do you need help with?"],
    "scan result": ["I can analyze scan results. Please upload your report."],
    "follow-up": ["You should consult a doctor if you feel discomfort after the scan."],
    "default": ["I'm not sure about that. Could you provide more details?"]
}

def chatbot_response(user_input: str):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])
