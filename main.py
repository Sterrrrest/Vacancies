from functions import table
from predict_rub_salary_sj import predict_rub_salary_sj
from predict_rub_salary_hh import predict_rub_salary_hh


if __name__ == '__main__':

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

    table(predict_rub_salary_hh(language_names), language_names, title='HeadHunter Moscow')
    table(predict_rub_salary_sj(language_names), language_names, title='SuperJob Moscow')