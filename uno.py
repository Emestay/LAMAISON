# from pytuya import BulbDevice
# mes var


def control_device(dev_id, dev_key, dev_ip, command):
    device = BulbDevice(dev_id, dev_key, dev_ip)
    device.set_version(3.3)
    if command == 'on':
        device.turn_on()
    elif command == 'off':
        device.turn_off()


ac_id = 'your_ac_id' 
ac_key = 'your_ac_key' 
ac_ip = 'your_ac_ip' 

bulb1_id = 'your_bulb1_id' 
bulb1_key = 'your_bulb1_key' 
bulb1_ip = 'your_bulb1_ip' 

bulb2_id = 'your_bulb2_id' 
bulb2_key = 'your_bulb2_key' 
bulb2_ip = 'your_bulb2_ip' 

washing_machine_id = 'your_washing_machine_id'
washing_machine_key = 'your_washing_machine_key'
washing_machine_ip = 'your_washing_machine_ip'

# Chaque device
control_device(ac_id, ac_key, ac_ip, 'on') # Clim
control_device(bulb1_id, bulb1_key, bulb1_ip, 'off') # Bulb terasse
control_device(bulb2_id, bulb2_key, bulb2_ip, 'on') # Bulb salon
control_device(washing_machine_id, washing_machine_key, washing_machine_ip, 'off') # Machine a laver
