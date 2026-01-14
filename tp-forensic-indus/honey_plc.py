import socket
import logging
import datetime

# Configuration
BIND_IP = '0.0.0.0'
BIND_PORT = 5020  # On reprend le même port pour piéger l'attaquant
LOG_FILE = '/app/honeypot.log'

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(5)
    print(f"[*] Honeypot Modbus actif sur {BIND_IP}:{BIND_PORT}")

    with open(LOG_FILE, 'a') as log:
        log.write(f"--- Démarrage Honeypot {datetime.datetime.now()} ---\n")

    while True:
        client_sock, address = server.accept()
        print(f"[!] ALERTE : Connexion entrante de {address[0]}:{address[1]}")
        
        # Enregistrement de l'alerte
        with open(LOG_FILE, 'a') as log:
            log.write(f"{datetime.datetime.now()} - INTRUSION DETECTÉE - Source: {address[0]}\n")
        
        # Leurre : On envoie une fausse bannière PLC
        try:
            client_sock.send(b"\x00\x00\x00\x00\x00\x06\x01\x03\x00\x00\x00\x01") # Fausse réponse Modbus
            data = client_sock.recv(1024)
            if data:
                with open(LOG_FILE, 'a') as log:
                    log.write(f"PAYLOAD REÇU (Hex): {data.hex()}\n")
        except:
            pass
        finally:
            client_sock.close()

if __name__ == '__main__':
    start_honeypot()