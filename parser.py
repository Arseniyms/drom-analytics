import requests
from bs4 import BeautifulSoup
import csv

field_names = ['title', 'year', 'price', 'engine', 'power', 'transmission', 'gear', 'body_type', 'color',
                       'mileage', 'wheel', 'generation', 'equipment', 'public_date', 'views', 'description']

def get_html(url, params=None):
    r = requests.get(url, params=params)
    return r

class safe_list(list):
    def get(self, index, default=None):
        try:
            return self.__getitem__(index)
        except IndexError:
            return default

def get_data(url, tag, className):
    soup = BeautifulSoup(url, 'html.parser')
    raw_data = soup.find_all(tag, className)
    raw_data = raw_data[:15]
    data = []

    if tag == 'a':
        [data.append(i.get('href')) for i in raw_data]
    else:
        [data.append(i.text) for i in raw_data]

    return data


def get_content(html, page):
    links = get_data(html, 'a', 'css-4zflqt e1huvdhj1')
    titles = get_data(html, 'div', 'css-16kqa8y e3f4v4l2')

    cars_info = []

    print('Обратка страницы ' + str(page) + '...')

    for i in range(len(links)):
        car_html = get_html(links[i])
        if car_html.status_code == 200:
            description = get_data(car_html.text, 'span', 'css-1kb7l9z e162wx9x0')
            description = safe_list(description)
            description = description.get(1, '').replace('\n', '')
            description = description.replace('\r', '')
            split_title = titles[i].split(',')
            title = split_title[0]
            year = int(split_title[1])

            price = get_data(car_html.text, 'div', 'css-eazmxc e162wx9x0')
            price = safe_list(price)
            price = price.get(0, '').replace('\xa0', u'')[:-1]

            specs_names = get_data(car_html.text, 'th', 'css-a4bpk4 ezjvm5n1')
            specs_value = get_data(car_html.text, 'td', 'css-1la7f7n ezjvm5n0')

            public_date = get_data(car_html.text, 'div', 'css-pxeubi evnwjo70')[0][-10:]

            views = get_data(car_html.text, 'div', 'css-14wh0pm e1lm3vns0')[0]

            for i in range(len(specs_names)):
                specs_value[i] = specs_value[i].replace('\xa0', u'')
                specs_value[i] = specs_value[i].replace('налог', u'')
                specs_value[i] = specs_value[i].replace(',', u'')

            specs = {specs_names[i]: specs_value[i] for i in range(len(specs_names))}

            # print(description)
            # print(title)
            # print(year)
            # print(price)
            # print(public_date)
            # print(int(views))
            # print(specs)
            # print("*" * 40)

            cars_info.append({
                'title': title,
                'year': year,
                'price': price,
                'engine': specs.get('Двигатель'),
                'power': specs.get('Мощность'),
                'transmission': specs.get('Коробка передач'),
                'gear': specs.get('Привод'),
                'body_type': specs.get('Тип кузова'),
                'color': specs.get('Цвет'),
                'mileage': specs.get('Пробег'),
                'wheel': specs.get('Руль'),
                'generation': specs.get('Поколение'),
                'equipment': specs.get('Комплектация'),
                'public_date': public_date,
                'views': views,
                'description': description
            })

    print('Выгрузка данных страницы ' + str(page))

    with open('cars.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writerows(cars_info)

    csvfile.close()

def parse(csv_file):
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
    csvfile.close()

    count = int(input('Введите количество страниц (на каждой странице по 15 объявлений): '))

    for i in range(1, count + 1):
        url = 'https://spb.drom.ru/all/page{}/?unsold=1'.format(str(i))
        html = get_html(url)
        if html.status_code == 200:
            get_content(html.text, i)
        else:
            print('Error')

