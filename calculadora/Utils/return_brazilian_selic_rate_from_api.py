import requests
from datetime import datetime

annualInterestSelicRateCode = 1178
currentYear = datetime.utcnow().year
todayDateString = datetime.now().strftime("%d/%m/%Y")
currentMonth = datetime.now().month


def return_latest_brazilian_selic_rates_from_api():
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{annualInterestSelicRateCode}/dados?formato=json&dataInicial=01/{currentMonth}/{currentYear}&dataFinal={todayDateString}"
    response = requests.get(url)

    if response.ok:
        data = response.json()
        return data


def return_selic_rate_from_last_month():
    return return_latest_brazilian_selic_rates_from_api()[-1]
