import redis
import csv
import json

data = {}
with open("CSV_FILES/EQ100521.CSV") as csvfile:
    csvReader = csv.DictReader(csvfile)
    for rows in csvReader:
        key = rows["SC_CODE"]
        data[key] = rows

with open("equity.json", 'w', encoding='utf-8') as jsonfile:
    jsonfile.write(json.dumps(data))


redis_instance = redis.StrictRedis(
    host='localhost', port=6379, db=0)

with open("equity.json") as jsonfile:
    jsonReader = json.load(jsonfile)
    for row in jsonReader:
        redis_instance.set(row, json.dumps(jsonReader[row]))

with open("equity.json") as jsonfile:
    jsonReader = json.load(jsonfile)
    for row in jsonReader:
        print(json.loads(redis_instance.get(row))['HIGH'])
