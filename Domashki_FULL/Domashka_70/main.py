from functions import *

name_students = 'students.json'
name_professions = 'professions.json'

data_students = load_students('students.json')
data_professions = load_professions('professions.json')

pk = int(input('Введите номер студента: '))
student = get_student_by_pk(pk, data_students)
if student:
    print(f'Студент {student["full_name"]}.')
    str_skills = ', '.join(student['skills'])
    print(f"Обладает {str_skills}.")
else:
    print("Нет такого студента.")
    quit()

title = input('Введите специальность: ').title()
profession = get_profession_by_title(title, data_professions)
if not profession:
    print("Нет такой специальности.")
    quit()

data = (check_fitness(student, profession))
print(show_result(data, student['full_name']))
