import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, request, jsonify

# Define reflections and pairs
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}

pairs = [
    [r"my name is (.*)", ["Hello %1, How are you today?"]],
    [r"hi|hey|hello", ["Hello", "Hey there"]],
    [r"what is your name ?", ["I am a bot. You can call me Crazy!"]],
    [r"how are you ?", ["I'm doing good. How about you?"]],
    [r"sorry (.*)", ["It's alright", "It's OK, never mind"]],
    [r"I am fine", ["Great to hear that. How can I help you?"]],
    [r"quit", ["Goodbye! Take care."]],
    [r"The car was not clean", ["Go to the rating page and type your problem"]]
]

# Initialize Flask app
app = Flask(__name__)

# Create a Chat object
chatbot = Chat(pairs, reflections)

# Define a POST endpoint
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
