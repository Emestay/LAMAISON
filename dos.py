# pip3 install flask

from flask import Flask
from pytuya import BulbDevice

app = Flask(__name__)

# .env
devices = {
    'ac': {'id': 'your_ac_id', 'key': 'your_ac_key', 'ip': 'your_ac_ip'},
    'bulb1': {'id': 'your_bulb1_id', 'key': 'your_bulb1_key', 'ip': 'your_bulb1_ip'},
    'bulb2': {'id': 'your_bulb2_id', 'key': 'your_bulb2_key', 'ip': 'your_bulb2_ip'},
    'washing_machine': {'id': 'your_washing_machine_id', 'key': 'your_washing_machine_key', 'ip': 'your_washing_machine_ip'},
}

def control_device(dev_id, dev_key, dev_ip, command):
    device = BulbDevice(dev_id, dev_key, dev_ip)
    device.set_version(3.3)
    if command == 'on':
        device.turn_on()
    elif command == 'off':
        device.turn_off()

@app.route('/<device>/<command>')
def control(device, command):
    if device in devices and command in ['on', 'off']:
        control_device(devices[device]['id'], devices[device]['key'], devices[device]['ip'], command)
        return f'{device} turned {command}'
    else:
        return 'Invalid device or command'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    