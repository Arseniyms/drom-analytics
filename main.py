
from parser import  parse
from database import mongoimport, get_price
from drom_analytics import amount_statistics

csv_file = 'cars.csv'
db_name = 'drom'
coll_name = 'alls'


if __name__ == "__main__":
    parse(csv_file)
    print("Паринг в файл закончен")
    mongoimport(csv_file, db_name, coll_name)

    prices = (get_price(db_name, coll_name))
    amount_statistics(prices)