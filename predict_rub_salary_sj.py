import requests
import os


from statistics import mean
from dotenv import load_dotenv, find_dotenv
from functions import predict_rub_salary


def predict_rub_salary_sj(language_names):
    load_dotenv(find_dotenv())
    token_api = os.environ['SUPER_JOB_KEY']
    url = 'https://api.superjob.ru/2.0/vacancies/'
    header = {'X-Api-App-Id': token_api}
    salaries = []
    languages = {}
    for text in language_names:
        vacancies = []
        payLoad = {
            'keyword': text,
            'count': 100,
            'page': 5,
            'period': 30,
            'town': 4
        }
        response = requests.get(url, params=payLoad, headers=header)
        response.raise_for_status()
        page_payload = response.json()
        for vacancy in page_payload['objects']:
            if ((vacancy['payment_from'] or
                 vacancy['payment_to'])) != 0 and vacancy['currency'] == 'rub':
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