# scripts/fake_plc.py
import logging
from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

# Simulation d'un serveur Modbus simple sur le port 5020 (pour éviter les soucis de root)
# Dans le TP, on considérera que c'est le port 502 standard.
def run_server():
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17]*100),
        co=ModbusSequentialDataBlock(0, [17]*100),
        hr=ModbusSequentialDataBlock(0, [17]*100),
        ir=ModbusSequentialDataBlock(0, [17]*100))
    context = ModbusServerContext(slaves=store, single=True)
    
    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    
    print("❌ Démarrage du PLC Siemens S7-1200 (Simulé) sur le port 5020...")
    StartTcpServer(context, address=("0.0.0.0", 5020))

if __name__ == "__main__":
    run_server()