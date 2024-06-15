from datetime import date
from datetime import datetime
import locale

def date_para_str(data:date) -> str:
    return date.strftime(data, '%d/%m/%Y')

def str_para_date(data:str) -> date:
    return datetime.strptime(data, "%d/%m/%Y")

def formata_float_str_moeda(valor: float) -> str:
    # Configurando a localidade para 'pt_BR' (Português do Brasil)
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = float(valor)
    # Formatação utilizando as convenções locais
    valor_formatado = locale.currency(valor, grouping=True)
    return valor_formatado

