from flask import Flask, render_template, request
from main import encrypt, decrypt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    text = request.form['text']
    key = request.form['key']
    mode = request.form['mode']

    if mode == 'encrypt':
        result = encrypt(text, key)
    else:
        result = decrypt(text, key)

    return render_template('result.html', result=result, text=text, key=key, mode=mode)

if __name__ == "__main__":
    app.run(debug=True)