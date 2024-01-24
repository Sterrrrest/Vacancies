from terminaltables import AsciiTable


def get_table(languages, title):
    final_table = [('Язык программирования',
                    'Вакансий найдено',
                    'Вакансий обработано',
                    'Средняя зарплата'), ]
    for language, language_stats in languages.items():
        table_data = (language, language_stats['vacancies_found'], language_stats['vacancies_processed'], language_stats['average_salary'], )
        final_table.append(table_data)

    table_instance = AsciiTable(final_table, title)
    table_instance.justify_columns[2] = 'right'
    return table_instance.table


def predict_rub_salary(min_salary, max_salary):

    if min_salary and max_salary:
        salary = (min_salary + max_salary) / 2
        return salary
    if min_salary and not max_salary:
        salary = min_salary * 1.2
        return salary
    if not min_salary and max_salary:
        salary = max_salary * 0.8
        return salary
