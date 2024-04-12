from parser.parser import parse


csv_file = '../data/cars.csv'
db_name = 'drom'
coll_name = 'alls'


if __name__ == "__main__":
    parse(csv_file)
    print("Парсинг в файл закончен")
    # mongoimport(csv_file, db_name, coll_name)

    # prices = (get_price(db_name, coll_name))
    # amount_statistics(prices)