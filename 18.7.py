import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить оценку ученика
        5. Удалить предмет
        6. Удалить ученика из списка
        7. Изменить оценку ученика по предмету
        8. Заменить предмет
        9. Изменить имя ученика
        10. Вывести все оценки ученика
        11. Вывести средний бал по предметам ученика
        12. Добавить предмет
        13. Добавить ученика
        14. Выход из программы

        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалить оценку ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys() and mark in students_marks[student][class_]:
            students_marks[student][class_].remove(mark)
            print(f'Для {student} по предмету {class_} удалена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета или нет такой оценки ')
    elif command == 5:
        print('5. Удалить предмет')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        if class_ in classes:
            classes.remove(class_)
            del students_marks[student][class_]
            print(f'Предмет {class_} удален')
        else:
            print('ОШИБКА: неверное название предмета')
    elif command == 6:
        print('6.Удалить ученика из списка ')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        if student in students:
            students.remove(student)
            del students_marks[student]
            print(f'Студент {student} удален из списка')
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command ==7:
        print('7. Изменить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку которую хотите изменить: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys() and mark in students_marks[student][class_]:
            students_marks[student][class_].remove(mark)
            mark_ = int(input('Введите ноувую оценку: '))
            students_marks[student][class_].append(mark_)
            print(f'Оценка {mark} у {student} по предмету {class_} изменена на {mark_}')
        else:
            print('ОШИБКА: неверное имя или название предмета или такой оценки нет')
    elif command == 8:
        print('8. Заменить предмет')
        class_ = input('Введите предмет: ')
        if class_ in classes:
            class_n = input('Введите новое название: ')
            if class_n in classes:
                print('ОШИБКА: Такой предмет уже есть')
            else:
                classes.remove(class_)
                classes.append(class_n)
                for student in students_marks.keys():

                    students_marks[student][class_n] = students_marks[student][class_]
                del students_marks[student][class_]
            print(f'Предмет {class_} изменен на {class_n}')
        else:
            print('ОШИБКА: Неверное название предмета')
    elif command == 9:
        print('9. Изменить имя ученика')
        student = input('Введите имя которе надо изменить: ')
        if student in students:
            n_student = input('Введите нове имя: ')
            if n_student in students:
                print('ОШИБКА: Такое имя уже есть')
            else:
                students.remove(student)
                students.append(n_student)
                students_marks[n_student] = students_marks[student]
            del students_marks[student]
            print(f'Имя {student} изменено на {n_student}')
        else:
            print('ОШИБКА: Неверное имя ученика')
    elif command == 10:
        print('10. Вывести все оценки ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            print(student)
            for class_ in classes:
                print(f'{class_} - {students_marks[student][class_]}')
        else:
            print('ОШИБКА: Такого имени нет')
    elif command == 11:
        print('11. Вывести средний бал по предметам ученика')
        student = input('Введите имя ученика: ')
        if student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 12:
        print('12. Добавить предмет')
        new_class = input('Введите новый предмет: ')
        if new_class in classes:
            print('Такой предмет уже есть')
        else:
            classes.append(new_class)
            for student in students_marks:
                students_marks[student][new_class] = []
        print('Предмет добавлен')
    elif command == 13:
        print('13. Добавить ученика')
        new_student = input('Введите имя ученика: ')
        if new_student in students:
            print('Данное имя уже есть')
        else:
            students.append(new_student)
            students_marks[new_student] = {}
            for class_ in classes:
                students_marks[new_student][class_] = {}


            print('Ученик добавлен')
    elif command == 14:
        print('14. Выход из программы')
        break
