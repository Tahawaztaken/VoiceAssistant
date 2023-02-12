from flask import Flask, render_template, jsonify
import SpeechRecognition

app = Flask(__name__)

@app.route('/get_data')
def getData():
    command = SpeechRecognition.transcribe_audio()
    print(f"flask:{command}")
    return jsonify(command)

@app.route('/')
def home(name=None):
    return render_template("index.html", name=name)





# if __name__ == '__main__':
#     app.run(debug=True)