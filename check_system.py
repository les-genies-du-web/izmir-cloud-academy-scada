from pymodbus.client import ModbusTcpClient
import sys

# Remplacer par l'IP du PLC trouvée lors du scan nmap (ex: 172.18.0.2)
PLC_IP = "172.xx.0.xx" 

client = ModbusTcpClient(PLC_IP, port=502)
client.connect()

# Lecture du registre 0 (Pression)
# address=0, count=1, slave=1
rr = client.read_holding_registers(0, 1, slave=1)

if rr.isError():
    print("Erreur de lecture")
else:
    print(f"--- ETAT SYSTEME ---")
    print(f"Pression actuelle : {rr.registers[0]} Bars")
    
client.close()