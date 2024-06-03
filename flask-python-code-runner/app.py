# app.py

from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-python', methods=['POST'])
def run_python():
    code = request.json.get('code')
    try:
        result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, universal_newlines=True)
        return jsonify({'output': result})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.output})

if __name__=='__main__':
        app.run(debug=True)


