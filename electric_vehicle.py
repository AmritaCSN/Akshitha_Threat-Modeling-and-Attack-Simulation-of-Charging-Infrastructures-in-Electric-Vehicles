import requests

def authenticate(username, password):
    payload = {'username': username, 'password': password}
    response = requests.post('http://192.168.1.232/authenticate', data=payload)
    if response.status_code == 200:
        print('Authentication successful')
        send_charging_request('EV001')  # Assuming EV ID is 'EV001'
    else:
        print('Authentication failed')

def send_charging_request(ev_id):
    payload = {'ev_id': ev_id}
    response = requests.post('http://192.168.1.232/charge_request', data=payload)
    if response.status_code == 200:
        print('Charging request sent successfully')
    else:
        print('Failed to send charging request')

if __name__ == '__main__':
    authenticate('user123', 'password123')
