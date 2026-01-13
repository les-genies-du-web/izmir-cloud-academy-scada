# plc.py
import logging
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

# Configuration des logs pour voir le "Clear Text"
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def run_server():
    # Définition de la mémoire
    store = ModbusSlaveContext(
        co=ModbusSequentialDataBlock(0, [0]*100),
        hr=ModbusSequentialDataBlock(0, [20]*100), 
        ir=ModbusSequentialDataBlock(0, [0]*100),
        di=ModbusSequentialDataBlock(0, [0]*100)
    )
    
    context = ModbusServerContext(slaves=store, single=True)
    
    print("--- PLC DÉMARRÉ (Version Stable) ---")
    # Lancement du serveur
    StartTcpServer(context=context, address=("0.0.0.0", 5020))

if __name__ == "__main__":
    run_server()
