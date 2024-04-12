import statistics
from pymongo import MongoClient


client = MongoClient('127.0.0.1', 27017)

def amount_statistics(params):
    print("Среднее занчение: ", statistics.mean(params))
    print("Минимальное значение: ", min(params))
    print("Максимальное значение: ", max(params))

def get_price(db_name, coll_name):
    db = client[db_name]
    coll = db[coll_name]
    cursor = coll.find()

    prices = [document['price'] for document in cursor]

    return prices

db_name = 'drom'
coll_name = 'alls'

if __name__ == "__main__":
    prices = (get_price(db_name, coll_name))
    amount_statistics(prices)
