from datetime import datetime
from xmlrpc.client import DateTime
from Attivita.Cliente import Cliente
import datetime

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cliente = Cliente()
    cliente.aggiungiCliente("lol", "bello", "pippo", 33333, "mail", "pluto", datetime.datetime(1989, 10, 20), "sndkv", "1")
    print(cliente.visualizzaCliente())
    clientesecondo = Cliente().ricercaUtilizzatore('pippo', 'pluto')
    print(clientesecondo.visualizzaCliente())
    clientesecondo.rimuoviCliente()
    print(clientesecondo.visualizzaCliente())
