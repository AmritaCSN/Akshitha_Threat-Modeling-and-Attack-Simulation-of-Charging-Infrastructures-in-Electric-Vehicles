from flask import Flask, request

app = Flask(__name__)

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    if username == 'user123' and password == 'password123':
        return 'Authentication successful', 200
    else:
        return 'Authentication failed', 401

@app.route('/charge_request', methods=['POST'])
def charge_request():
    ev_id = request.form['ev_id']
    print(f'Received charging request from EV {ev_id}')
    print('Initiating charging session...')
    print('Charging session complete')
    return 'Charging session complete', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


