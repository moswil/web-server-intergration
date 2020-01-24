from flask import Flask, jsonify, make_response, request


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'message': 'welcome home'})


@app.route('/mpesa/b2c/v1', methods=['POST'])
def listen_b2c():
    # save data
    request_data = request.data

    # perform your processing here, e.g., printing it out
    print(request_data)

    # prepare the response, assuming no errors have occurred. Any response

    # other than a 0 (zero) for the 'ResultCode' during Validation only

    # any error occurred and the transaction is cancelled.
    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": "1234567890"
    }

    # send the response back to the server
    return jsonify({'message': message}), 200


@app.route('/mpesa/b2b/v1')
def listen_b2b():
    request_data = request.data
    print(request_data)
    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": "1234567890"
    }

    return jsonify({'message': message}), 200


@app.route('/mpesa/lnm/v1/online-payment')
def lnm_online_payment():
    pass


@app.route('/mpesa/lnm/v1/query-request')
def lnm_query_request():
    pass


if __name__ == "__main__":
    app.run(debug=True)
