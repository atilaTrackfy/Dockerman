from flask import Flask, request


app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():

    data = request.form.get('data')
    print("Received data: ", data)

    return help(data)

@app.route('/get', methods=['GET'])
def get():

    print("oi")

    return "oi2"

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True)
