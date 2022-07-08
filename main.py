import datetime

from Attivita.Acquisto import Acquisto
from Attivita.Cliente import Cliente
from Servizio.Bottiglia import Bottiglia
from Attivita.Prenotazione import Prenotazione
from copy import deepcopy

if __name__ == '__main__':
    #acquisto = Acquisto()
    #acquisto.verificaPrenotazione(3)
    #acquisto.effettuaAcquisto(1, None, 3)
    #acquisto.effettuaAcquisto(1, 'Giana', 3)
    #acquisto.effettuaAcquisto(1, None)

    elenco = []  # list
    p = Bottiglia()

    p = p.aggiungiBottiglia('Giana', 10)
    d = deepcopy(p)
    elenco.append(d)

    p = p.aggiungiBottiglia('Papola', 5)
    d = deepcopy(p)
    elenco.append(d)

    #for elem in elenco:
    #    print(elem)
    cliente = Cliente()
    cliente.aggiungiCliente('test', 'privato', 'Pino', 331, 'pippo@gmail', 'Pinoli', datetime.datetime(2001,10,13), 'CF', 0)

    pren = Prenotazione(elenco)
    pren.aggiungiPrenotazione(2, cliente, elenco)        #for elem in pren.prodotti:  #print(elem)
    print(pren)
