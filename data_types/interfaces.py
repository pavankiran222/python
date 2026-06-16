interface = "GigabitEthernet1/0/5"
config = "interface Gi1/0/5\n ip address 10.10.10.1 255.255.255.0"

# Common operations
print(interface.startswith("Gigabit"))
print("10.10.10.1" in config)
print(config.splitlines())