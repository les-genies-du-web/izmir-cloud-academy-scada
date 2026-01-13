# plc.py
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
import logging

# Configuration du logging pour voir les attaques en temps réel
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def run_server():
    # Store:
    # Coils (0-100): Adresse 0 = Pompe, Adresse 1 = Alarme
    # Holding Registers (0-100): Adresse 0 = Temperature
    store = ModbusSlaveContext(
        co = ModbusSequentialDataBlock(0, [0]*100),
        hr = ModbusSequentialDataBlock(0, [20]*100), # Temp init = 20
        ir = ModbusSequentialDataBlock(0, [0]*100),
        di = ModbusSequentialDataBlock(0, [0]*100)
    )
    context = ModbusServerContext(slaves=store, single=True)
    
    print("--- PLC MODBUS DÉMARRÉ SUR PORT 502 ---")
    print("--- VULNÉRABILITÉS : NO AUTH, CLEAR TEXT ---")
    StartTcpServer(context=context, address=("0.0.0.0", 502))

if __name__ == "__main__":
    run_server()