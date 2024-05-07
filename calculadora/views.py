from django.shortcuts import render
from django.http import HttpResponse
import re

def calcular_investimento(request):
    valor_taxa_selic_ao_ano = 11
    valor_inicial = 10000
    porcentagem_rendimento_ao_ano = 11.5
    valor_rendimento_ao_ano = porcentagem_rendimento_ao_ano / 100
    valor_rendimento_ao_mes = valor_rendimento_ao_ano / 12
    valor_final = valor_inicial
    lista_de_valores_por_mes = []

    def formata_dois_decimais_e_converte_para_float(valor_numerico):
        valor_numerico = "{:.2f}".format(valor_numerico)
        valor_numerico = float(valor_numerico)
        return valor_numerico

    for contador_individual in range(1, 13):
        if valor_final < valor_inicial:
            valor_final = valor_inicial

        valor_final = formata_dois_decimais_e_converte_para_float(valor_final)

        lista_de_valores_por_mes.append(valor_final)
        valor_final = valor_final + valor_inicial * valor_rendimento_ao_mes

    contexto = {
        'valor_juros_acumulado': formata_dois_decimais_e_converte_para_float(valor_final),
        'valores_por_mes': lista_de_valores_por_mes,
        'valor_taxa_selic_ao_ano':  valor_taxa_selic_ao_ano
    }
    return render(request, 'calculadora/calculadora.html', contexto)
