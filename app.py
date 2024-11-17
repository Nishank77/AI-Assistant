from flask import Flask, render_template, request, jsonify
import main  # This will import your existing main.py file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # This will render the landing page

# This route will handle the microphone button and trigger the speak method from main.py
@app.route('/speak', methods=['POST'])
def speak():
    main.main_process()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
