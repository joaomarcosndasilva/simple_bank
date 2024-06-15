from models.cliente import Cliente
from models.conta import Conta

felicity: Cliente = Cliente('Felicity Jones', 'felicity@gmail.com', '112.456.789-10', '02/09/1987')
angelina: Cliente = Cliente('Angelina Jolie', 'angelina@gmail.com', '234.567.898-02', '08/07/1978')

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)
