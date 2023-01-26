import json


def load_students(filename):
    """
    Функция выгружает из JSON данные и возвращает данные о студенте.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def load_professions(filename):
    """
    Функция выгружает из JSON данные и возвращает данные о професии.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_student_by_pk(pk, data):
    """
    Функция возвращает данные по введенным параметрам.
    """
    for item in data:
        if pk == item['pk']:
            return item


def get_profession_by_title(title, data):
    for item in data:
        if title == item['title']:
            return item


def check_fitness(student, profession):
    set_student = set(student['skills'])
    set_profession = set(profession['skills'])
    has_skills = set_student.intersection(set_profession)
    lost_skills = set_profession.difference(set_student)
    fit_percent = round(len(has_skills) / len(lost_skills) * 100)
    result = {
        'has': has_skills,
        'lacker': lost_skills,
        'fit_percent': fit_percent
    }
    return result


def show_result(data, name):
    str_has = ', '.join(data['has'])
    str_lacks = ', '.join(data['lacker'])
    str_output = f"Пригодность {data['fit_percent']}%\n" \
                 f"{name} знает {str_has}\n" \
                 f"{name} не знает {str_lacks}"
    return str_output
