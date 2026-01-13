# Dans le terminal attacker, lancez python
import socket

# Simulation d'un client légitime qui demande la température
from pymodbus.client import ModbusTcpClient
client = ModbusTcpClient('lab_plc')
client.write_register(0, 555) # L'opérateur règle la temp à 555
client.close()