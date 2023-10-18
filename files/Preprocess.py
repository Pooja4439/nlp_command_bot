def preprocess_text(text):
    if 'hi' in text.lower() or 'hello' in text.lower() or 'greetings' in text.lower():
        text = 'hello'
    elif 'break' in text.lower() or 'rest' in text.lower() or 'quit' in text.lower() or 'leave' in text.lower() or 'get out' in text.lower() or 'exit' in text.lower():
        text = 'break'
    elif 'google' in text.lower() or 'search' in text.lower():
        text = 'google search'
    elif 'vs code' in text.lower():
        text = 'open vs code'
    return text.lower()