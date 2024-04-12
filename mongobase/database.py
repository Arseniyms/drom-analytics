import pandas as pd
from pymongo import MongoClient

# client = MongoClient(
    # 'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.3', 27017)

client = MongoClient('127.0.0.1', 27017)

def mongoimport(csv_path, db_name, coll_name):
    db = client[db_name]
    coll = db[coll_name]
    coll.drop()
    data = pd.read_csv(csv_path)
    data_dict = data.to_dict(orient='records')
    coll.insert_many(data_dict)

    cursor = coll.find()
    for document in cursor:
        print(document)

csv_file = '/data/cars.csv'
db_name = 'drom'
coll_name = 'alls'

if __name__ == "__main__":
    mongoimport(csv_file, db_name, coll_name)
    print("Выгрузка в базу данных завершена")
