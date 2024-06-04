import sys, os
sys.path.insert(1,f'{os.getcwd()}/calculadora/')
from Utils.return_brazilian_selic_rate_from_api import return_selic_rate_from_last_month

def test_if_api_is_responding():
    data_valor = return_selic_rate_from_last_month()
    assert 'data' in data_valor
    assert 'valor' in data_valor
    print('\nSucess: ',data_valor)

