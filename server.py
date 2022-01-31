from flask import Flask, request


app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():

    data = request.form['data']
    print("Received data: ", data)

    return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)
