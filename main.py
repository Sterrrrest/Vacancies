import os


from functions import get_table
from predict_rub_salary_sj import predict_rub_salary_sj
from predict_rub_salary_hh import predict_rub_salary_hh
from dotenv import load_dotenv, find_dotenv


if __name__ == '__main__':

    load_dotenv(find_dotenv())
    api_token = os.environ['SUPER_JOB_KEY']

    language_names = [
      'программист Python',
      'программист Java',
      'программист Javascript',
      'программист 1c',
      'программист PHP',
      'программист C++',
      'программист C#',
      'программист C'
    ]

    print(get_table(predict_rub_salary_hh(language_names), language_names, title='HeadHunter Moscow'))
    print(get_table(predict_rub_salary_sj(language_names, token_api), language_names, title='SuperJob Moscow'))