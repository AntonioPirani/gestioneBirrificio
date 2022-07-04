from datetime import datetime
from xmlrpc.client import DateTime
from Attivita.Dipendente import Dipendente
import datetime

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dipendente = Dipendente()
    #dipendente.aggiungiDipendente("aaaa", "pippo", 33333, "mail", "pluto", datetime.datetime(1989, 10, 20), "sndkv", "1")
    #print(dipendente.visualizzaDipendente())
    dipendentesecondo = Dipendente().ricercaUtilizzatore('pippo', 'pluto')
    print(dipendentesecondo.visualizzaDipendente())
