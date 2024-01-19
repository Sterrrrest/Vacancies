import requests


from statistics import mean

from functions import predict_rub_salary


def predict_rub_salary_sj(vacancies_language_names, api_token):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    header = {'X-Api-App-Id': api_token}
    salaries = []
    languages = {}
    for text in vacancies_language_names:
        vacancies = []
        count = 100
        page = 5
        period = 30
        town_id = 4
        payLoad = {
            'keyword': text,
            'count': count,
            'page': page,
            'period': period,
            'town': town_id
        }
        response = requests.get(url, params=payLoad, headers=header)
        response.raise_for_status()
        page_payload = response.json()
        for vacancy in page_payload['objects']:
            if (vacancy['payment_from'] or
                 vacancy['payment_to']) and vacancy['currency'] == 'rub':
                vacancies.append(predict_rub_salary(vacancy['payment_from'], vacancy['payment_to']))
        average_payments = int(mean(vacancies))
        salaries.append(average_payments)
        language = {
            'vacancies_found': page_payload['total'],
            'vacancies_processed': len(vacancies),
            'average_salary': average_payments
            }
        languages[text] = language
    return languages
