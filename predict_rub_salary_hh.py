import requests

from statistics import mean
from functions import predict_rub_salary


def predict_rub_salary_hh(language_names):
    languages = {}
    for text in language_names:
        url = 'https://api.hh.ru/vacancies'
        area = '1'
        period = 30
        header = {'HH-User-Agent': ''}
        page = 0
        pages_number = 1
        vacancies = []
        while page < pages_number:
            payLoad = {'page': page,
              'text': text,
              'area': area,
              'period': period}
            response = requests.get(url, params=payLoad, headers=header)
            response.raise_for_status()
            page_payload = response.json()
            pages_number = page_payload['pages']
            for vacancy in page_payload['items']:
                if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
                    vacancies.append(predict_rub_salary(vacancy['salary']['from'], vacancy['salary']['to']))
            page += 1
        average_payments = int(mean(vacancies))
        language = {
                  'vacancies_found': page_payload['found'],
                  'vacancies_processed': len(vacancies),
                  'average_salary': average_payments
                }
        languages[text] = language
    return languages
