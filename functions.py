from terminaltables import AsciiTable


def table(languages, language_names, title):
    final_table = [('Язык программирования',
                    'Вакансий найдено',
                    'Вакансий обработано',
                    'Средняя зарплата'), ]
    for text in language_names:
        table_data = (text, languages[text]['vacancies_found'], languages[text]['vacancies_processed'],
                      languages[text]['average_salary'],)
        final_table.append(table_data)

    table_instance = AsciiTable(final_table, title)
    table_instance.justify_columns[2] = 'right'
    print(table_instance.table)
    print()


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
