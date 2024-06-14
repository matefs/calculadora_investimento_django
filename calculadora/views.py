from django.shortcuts import render
from django.http import HttpResponse
import re
from .Utils.return_brazilian_selic_rate_from_api import return_selic_rate_from_last_month



def calcular_investimento(request):
    numeroDeMesesInvestido = None
    valor_taxa_selic_ao_ano = (float(return_selic_rate_from_last_month()['valor']) - 0.10 or 0  )
    valor_inicial = 0
    porcentagem_rendimento_ao_ano = valor_taxa_selic_ao_ano
    valor_rendimento_ao_ano = porcentagem_rendimento_ao_ano / 100
    valor_rendimento_ao_mes = valor_rendimento_ao_ano / 12
    valor_final = valor_inicial
    lista_de_valores_por_mes = []

    if request.method == 'POST':
        if hasattr(request, 'form'):  # If using a form class
            form = request.form
            print(form)
        else:  # If not using a form class
            valor_inicial = 0  + int(request.POST.get('valor_inicial'))
            tempo_investimento = int(request.POST.get('tempo_investimento'))
            numeroDeMesesInvestido = tempo_investimento # quantos meses kk 

            deposito_mensal =  float(request.POST.get('deposito_mensal'))
            print('Valor inicial', valor_inicial)


    def formata_dois_decimais_e_converte_para_float(valor_numerico):
        valor_numerico = "{:.2f}".format(valor_numerico)
        valor_numerico = float(valor_numerico)
        return valor_numerico

    for contador_individual in range(1, (numeroDeMesesInvestido or 1) + 1):
        print(contador_individual, valor_final )
        if valor_final < valor_inicial:
            valor_final = valor_inicial

        valor_final = formata_dois_decimais_e_converte_para_float(valor_final)

        lista_de_valores_por_mes.append(valor_final)
        valor_final = valor_final + valor_inicial * valor_rendimento_ao_mes

    contexto = {
        'valores_por_mes': lista_de_valores_por_mes,
        'valor_taxa_selic_ao_ano': valor_taxa_selic_ao_ano,
        'valor_inicial': valor_inicial,
        'porcentagem_rendimento_ao_ano': porcentagem_rendimento_ao_ano,
        'valor_rendimento_ao_ano': valor_rendimento_ao_ano,
        'valor_rendimento_ao_mes': valor_rendimento_ao_mes,
        'valor_juros_acumulado': formata_dois_decimais_e_converte_para_float(valor_final),
        'valores_por_mes': lista_de_valores_por_mes,
        'numeroDeMesesInvestido' : numeroDeMesesInvestido,
        'taxaSelic' : return_selic_rate_from_last_month
    }
    return render(request, 'calculadora/calculadora.html', contexto)
