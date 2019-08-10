import csv


def get_data():
    result = []
    table = []
    data_headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    for i in range(1, 4):
        with open(f'info_{i}.txt') as data:
            for row in data:
                if 'Изготовитель системы' in row:
                    table.append(row.split()[2])
                elif 'Название ОС' in row:
                    table.append(' '.join(row.split()[2:]))
                elif 'Код продукта' in row:
                    table.append(row.split()[2])
                elif 'Тип системы' in row:
                    table.append(' '.join(row.split()[2:]))
        result.append(table)
        table = []
    result.insert(0, data_headers)
    return result


def write_to_csv():
    with open('main_data.csv', 'w') as data:
        data_writer = csv.writer(data)
        for row in get_data():
            data_writer.writerow(row)
    return


write_to_csv()
