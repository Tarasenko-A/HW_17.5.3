import json
#with open("orders_july_2023.json", "r") as my_file:
with open(r'D:\Program Files\Test\orders_july_2023.JSON', "r") as my_file:
    orders_july = my_file.read()
orders = json.loads(orders_july)
print('''
Информация:1
1. Номер самого дорогого заказа за июль
2. Номер заказа с самым большим количеством товаров
3. День в июле в который было сделано больше всего заказов
4. Пользователь сделал самое большое количество заказов за июль
5. Пользователь у которого самая большая суммарная стоимость заказов за июль
6. Средняя стоимость заказа в июле
7. Средняя стоимость товаров в июле?
8. Конец запроса''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        #print('1. Какой номер самого дорогого заказа за июль?')
        max_price = 0
        max_order = ''
        for order_num, orders_data in orders.items():
            price = orders_data['price']
            if price > max_price:
                max_order = order_num
                max_price = price
        print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')
        # Номер заказа с самой большой стоимостью: o_182416, стоимость заказа: 29900

    elif command == 2:
        #print('2. Какой номер заказа с самым большим количеством товаров?')
        max_quantity = 0
        max_order = ''
        for order_num, orders_data in orders.items():
            quantity = orders_data['quantity']
            if quantity > max_quantity:
                max_order = order_num
                max_quantity = quantity
            print(f'Номер заказа с самым большим количеством товаров: {max_order}, количество товаров: {max_quantity}')
        # Номер заказа с самым большим количеством товаров: o_182378, количество товаров: 20

    elif command == 3:
        #print('3. В какой день в июле было сделано больше всего заказов?')
        date_dict = {}
        for order_num, orders_data in orders.items():
            date = orders_data['date']
            date_dict[date] = date_dict.get(date, 0) + 1
        for date in sorted(date_dict):
            max_value = max(date_dict.values())
            if date_dict[date] == max_value:
                print(f'Больше всего заказов было сделано в {date}: {date_dict[date]}')
            # Больше всего заказов было сделано в 2023-30-07: 33

    elif command == 4:
        #print('4. Какой пользователь сделал самое большое количество заказов за июль?')
        user_dict = {}
        max_orders = 0
        for order_num, orders_data in orders.items():
            user_id = orders_data['user_id']
            user_dict[user_id] = user_dict.get(user_id, 0) + 1
            orders_2 = user_dict.get(user_id)
            if orders_2 > max_orders:
                max_orders = orders_2
        print(f'Пользователь: {user_id} сделал наибольшее кол-во заказов: {max_orders}')
        # Пользователь: 358411 сделал наибольшее кол-во заказов: 1

    elif command == 5:
        #print('5. У какого пользователя самая большая суммарная стоимость заказов за июль?')
        user_dict = {}
        max_price = 0
        for order_num, orders_data in orders.items():
            user_id = orders_data['user_id']
            user_dict[user_id] = user_dict.get(user_id, 0) + orders_data['price']
            all_price = user_dict.get(user_id)
            if all_price > max_price:
                max_price = all_price
        print(f'Пользователь {user_id} имеет самую большую суммарную стоимость заказов за июль: {max_price}')
        # Пользователь 358411 имеет самую большую суммарную стоимость заказов за июль: 29900

    elif command == 6:
        #print('6. Какая средняя стоимость заказа была в июле?')
        price_sum = 0
        price_count = 0
        for order_num, orders_data in orders.items():
            price_sum += orders_data['price']
            price_count = len(orders)
        print(f'Средняя стоимость заказа в июле: {price_sum // price_count}')
        # Средняя стоимость заказа в июле: 15314

    elif command == 7:
        #print('7. Какая средняя стоимость товаров в июле?')
        price_sum = 0
        price_count = 0
        for order_num, orders_data in orders.items():
            price_sum += orders_data['price']
            price_count += orders_data['quantity']
        print(f'Средняя стоимость товаров в июле: {price_sum // price_count}')
        # Средняя стоимость товаров в июле: 1462

    elif command == 8:
        print('Конец запроса')
        break
