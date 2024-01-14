import requests

from terminaltables import AsciiTable
from statistics import mean


languages = {}
language_names = [
    'программист Python',
    'программист Java',
    'программист Javascript',
    # 'программист 1c',
    # 'программист HTML1',
    # 'программист C++',
    'программист C#',
    # 'программист C',
    # 'программист Ruby'
]


def predict_rub_salary_hh(vacancy):
    min_salary = vacancy['salary']['from']
    max_salary = vacancy['salary']['to']
    if min_salary and max_salary:
        salary = (min_salary + max_salary) / 2
        return salary
    if min_salary and not max_salary:
        salary = min_salary * 1.2
        return salary
    if not min_salary and max_salary:
        salary = max_salary * 0.8
        return salary


for text in language_names:
    url = 'https://api.hh.ru/vacancies'
    area = '1'
    header = {'HH-User-Agent': ''}
    salaries = []
    page = 0
    pages_number = 1
    vacancies = []
    while page < pages_number:
        payLoad = {'page': page,
          'text': text,
          'area': area,
          'period': 30}
        response = requests.get(url, params=payLoad, headers=header)
        response.raise_for_status()
        page_payload = response.json()
        # pages_number = page_payload['pages']
        pages_number = 5
        total_vacancies = response.json()['found']
        for vacancy in page_payload['items']:
          if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
              vacancies.append(predict_rub_salary_hh(vacancy))
        page += 1
    average_payments = int(mean(vacancies))
    language = {
              'vacancies_found': page_payload['found'],
              'vacancies_processed': len(vacancies),
              'average_salary': average_payments
            }
    languages[text] = (language)


def table(languages, language_names):
        final_table = [('Язык программирования',
                        'Вакансий найдено',
                        'Вакансий обработано',
                        'Средняя зарплата'), ]

        for text in language_names:
            table_data = (text, languages[text]['vacancies_found'], languages[text]['vacancies_processed'], languages[text]['average_salary'],)

            final_table.append(table_data)

        table_instance = AsciiTable(final_table)
        table_instance.justify_columns[2] = 'right'
        print(table_instance.table)
        print()

table(languages, language_names)

    # print(text, vacancies)
    # salaries.append(average_payments)
    # print(text, int(mean(vacancies)))
    # average_payments = int(mean(vacancies))
    # print(text, average_payments)
#  salaries.append(average_payments)
#  language = {
#       'vacancies_found': page_payload['found'],
#       'vacancies_processed': len(vacancies),
#       'average_salary': average_payments
#     }
# languages[text] = (language)
# print(languages)


# print(total_vacancies)
    #
    # for vacancy  in page_payload['items']:
    #   if vacancy['salary'] and vacancy['salary']['currency']=='RUR':
    #       vacancies.append(predict_rub_salary_hh(vacancy))
    # average_payments = int(mean(vacancies))
    # salaries.append(average_payments)
    # language = {
    #   'vacancies_found': page_payload['found'],
    #   'vacancies_processed': len(vacancies),
    #   'average_salary': average_payments
    # }
    # languages['программист Java'] = (language)
# page += 1
# print(language)
# def table(languages, language_names):
#     final_table = [('Язык программирования',
#                     'Вакансий найдено',
#                     'Вакансий обработано',
#                     'Средняя зарплата'), ]
#     for text in language_names:
#         table_data = (text, languages[text]['vacancies_found'], languages[text]['vacancies_processed'], languages[text]['average_salary'],)
#
#         final_table.append(table_data)
#
#     table_instance = AsciiTable(final_table)
#     table_instance.justify_columns[2] = 'right'
#     print(table_instance.table)
#     print()

# def get_all_vacncies(vacancy):
#   url = 'https://api.hh.ru/vacancies'
#   area = '1'
#   header = {'HH-User-Agent': ''}
#   payLoad = {
#     'text': text,
#     'area': area,
#     'period': 30}
#   response = requests.get(url, params=payLoad, headers=header)
#   response.raise_for_status()
#   vacancies = response.json()['found']
#   print(vacancies)
#   return vacancies
#
# texts = ['программист Python',
#  'программист Java',
#  'программист Javascript',
#  'программист Ruby',
#  'программист PHP',
#  'программист C++',
#  'программист C#',
#  'программист C'
# ]
# url = 'https://api.hh.ru/vacancies'




# pop_lang = {
#     'Python': {
#       "vacancies_found": get_all_vacncies(texts[0]),
#       "vacancies_processed": predict_rub_salary(texts[0])[1],
#       "average_salary": predict_rub_salary(texts[0])[0]
#               },
#     'Java': {
#       "vacancies_found": get_all_vacncies(texts[1]),
#       "vacancies_processed": predict_rub_salary(texts[1])[1],
#       "average_salary": predict_rub_salary(texts[1])[0]
#     },
#     'Javascript': {
#       "vacancies_found": get_all_vacncies(texts[2]),
#       "vacancies_processed": predict_rub_salary(texts[2])[1],
#       "average_salary": predict_rub_salary(texts[2])[0]
#     },
#     'Ruby': {
#       "vacancies_found": get_all_vacncies(texts[3]),
#       "vacancies_processed": predict_rub_salary(texts[3])[1],
#       "average_salary": predict_rub_salary(texts[3])[0]
#     },
#     'PHP': {
#       "vacancies_found": get_all_vacncies(texts[4]),
#       "vacancies_processed": predict_rub_salary(texts[4])[1],
#       "average_salary": predict_rub_salary(texts[4])[0]
#     },
#     'C++': {
#       "vacancies_found": get_all_vacncies(texts[5]),
#       "vacancies_processed": predict_rub_salary(texts[5])[1],
#       "average_salary": predict_rub_salary(texts[5])[0]
#     },
#     'C#': {
#       "vacancies_found": get_all_vacncies(texts[6]),
#       "vacancies_processed": predict_rub_salary(texts[6])[1],
#       "average_salary": predict_rub_salary(texts[6])[0]
#     },
#     'C': {
#       "vacancies_found": get_all_vacncies(texts[7]),
#       "vacancies_processed": predict_rub_salary(texts[7])[1],
#       "average_salary": predict_rub_salary(texts[7])[0]
#     }
#
#   }
# print(pop_lang)