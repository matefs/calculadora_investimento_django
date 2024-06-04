 
## Calculadora de Investimento em Django

Este repositório contém uma aplicação web desenvolvida em Django para calcular investimentos. A aplicação permite que você insira informações sobre o tipo de investimento, valor inicial, taxa de juros e período de investimento, e em seguida, ela calcula o montante final.


 ![image](https://github.com/matefs/calculadora_investimento_django/assets/30128774/208af157-2883-4a8a-ae8b-8ec639dcf93a)


### Funcionalidades

- **Calculadora de Poupança**: A aplicação utiliza a API do Banco Central do Brasil para obter dados sobre a taxa de juros da poupança. Você pode consultar a API aqui.
- **Gráfico Dinâmico**: Além do cálculo, a aplicação também exibe um gráfico dinâmico que mostra a evolução do investimento ao longo do tempo. O gráfico é baseado no código disponível neste exemplo.

### Como usar

1. Clone este repositório:
    
    `git clone https://github.com/matefs/calculadora_investimento_django.git`
    
2. Instale as dependências:
    
    `pip install -r requirements.txt`
    
3. Execute a aplicação:
    
    `python manage.py runserver`
    
4. Acesse a aplicação no navegador em **`http://localhost:8000`**.

## Testes: 
- A importação usando pytest não funciona uma vez existe um `__ini__` 

### Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

Espero que esta calculadora seja útil para você! 😊

 
## O que está por vir: 
- [ ] Todo:  calcular poupança por mês consultando api do governo: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.25/dados?formato=json&dataInicial=01/05/2024&dataFinal=31/12/2024`
- [ ] Todo: add dinamic chart: `https://jsfiddle.net/qahx2t3b/`
