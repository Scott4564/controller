import netmiko
# Connect to a Cisco Router using SSH and run show commands
router = {
'device_type': 'cisco_ios',
'ip': '192.168.1.1',
'username': 'admin',
'password': 'cisco',
'secret': 'class',
}
# Establish a connection
connection = netmiko.ConnectHandler(**router)

# Show output
output = connection.send_command('show ip int brief')
device = connection.find_prompt()
print (device + '\n' + output)
# Disconnect
connection.disconnect()
# Connect to a Cisco Switch using SSH and run show commands
switch = {
'device_type': 'cisco_ios',
'ip': '192.168.1.2',
'username': 'admin',
'password': 'cisco',
'secret': 'class',
}
# Establish a connection
connection = netmiko.ConnectHandler(**switch)
# Show output
output = connection.send_command('show ip int brief')
device = connection.find_prompt()
print (device + '\n' + output)
# Disconnect
connection.disconnect()
