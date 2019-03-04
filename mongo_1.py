import pymongo
import pprint
from bson.objectid import ObjectId
from bson import SON

myclient = pymongo.MongoClient("mongodb://192.168.34.6:27017/")
# myclient.drop_database("StrategicMap")
# mydb = myclient["moh"]
# mycol = mydb["first"]
'''
myquery = {'username': {'$regex': '^2'}}

x = mycol.find_one()
print(x)
for i in mycol.find(myquery):   # specifying the result
    print(i)
for i in mycol.find().sort('username', -1)     #sort descending

for i in mycol.find().sort('username'):    # sort results
    print(i)


myquery = {'username': {'$regex': '^t'}}
newvalues = {'$set': {'new': 'true'}}
x = mycol.update_many(myquery, newvalues)    # Update document\

mydoc = mycol.find().sort('username').limit(3)
for i in mydoc:
    print(i)
d = {'_id': 1, 'name': 'Valeriia'}
mycol.insert_one(d)

for i in mycol.find({}, {'_id': 0}):
    print(i)

#print(myclient.list_database_names()) #list of database
#mydb = myclient["StrategicMap"]
#mycol = mydb["app_data_version"]
#print(mydb.list_collection_names()) #list of collections

value = {'_id': '1', 'snap': '12'}
values = mydb.values
#values.delete_many({})
#values.insert_one(value)

for i in values.find({}):
    pprint.pprint(i)

'''


# mycol.delete_one({})

# print(mydb.list_collection_names())
from collections import Iterable
'''
for i in mycol.find({'name': 'hospital_codes'}, {'values_list'}):
    print(i['values_list'][0]['code'])
    mycol.create_index({})
'''

# print(mydb.list_collection_names())


def print_col(col, filter={}, fields=None, q=False):  # print document's data
    mydb = myclient["StrategicMap"]
    mycol = mydb[col]
    k = mycol.find(filter, fields)
    if q:
        print(k.count())
    pprint.pprint([i for i in k])


def vers_unique():
    mydb = myclient["StrategicMap"]
    mycol = mydb["app_data_version"]
    mycol.create_index([
        ('hospital_type', pymongo.ASCENDING),
        ('version_number', pymongo.DESCENDING)
    ], unique=True)


def meas_unique():
    mydb = myclient["StrategicMap"]
    mycol = mydb["app_data_measure"]
    mycol.create_index([
        ('measure_code', pymongo.DESCENDING),
        ('hospital_type', pymongo.ASCENDING)
    ], unique=True)


def acttual_unique():
    mydb = myclient["StrategicMap"]
    mycol = mydb["app_data_measure"]
    mycol.create_index([
        ('measure_code', pymongo.DESCENDING),
        ('hospital_type', pymongo.ASCENDING),
        ('version_number', pymongo.DESCENDING),
        ('hospital_code', pymongo.ASCENDING)
    ], unique=True)


def my_print(col, db="StrategicMap"):
    mydb = myclient[db]
    mycol = mydb[col]
    query = mycol.find({}, {'cancel': 1})
    for i in query:
        pprint.pprint(i)


def del_doc(col, query={'id': 3}):
    mydb = myclient["StrategicMap"]
    mycol = mydb[col]
    mycol.delete_one(query)


def del_one(col, query):
    try:
        mydb = myclient["StrategicMap"]
    except:
        print('Eeception occured')
    mycol = mydb[col]
    x = mycol.delete_one(query)
    print(x.deleted_count)


def drop_col(col):
    mydb = myclient["StrategicMap"]
    mycol = mydb[col]
    mycol.drop()


def update(col):
    mydb = myclient["StrategicMap"]
    mycol = mydb[col]
    query = {'id': 1}
    values = {'$set': {'active': True, 'cancel': False}}
    mycol.update_one(query, values)


def get(col, id):
    mydb = myclient["StrategicMap"]
    mycol = mydb[col]
    query = dict()
    query['_id'] = ObjectId(id)
    k = [i for i in mycol.find(query)]
    pprint.pprint(k)


def print_col_names():
    mydb = myclient["StrategicMap"]
    print(mydb.list_collection_names())


def del_many(col, data):
    mydb = myclient["StrategicMap"]
    mycol = mydb[col]
    query = mycol.delete_many(data)

def get_hosp():
    mydb = myclient["StrategicMap"]
    mycol = mydb["app_data_decryptiontables"]
    k = mycol.find({'name': 'hospital_codes'}, {'type_3': 1})
    pprint.pprint([i for i in k])

def create_array():
    mydb = myclient["StrategicMap"]
    mycol = mydb["app_data_decryptiontables"]
    data = {
        'name': 'hospital_codes',
        'type_1': [
            SON([('hosp_code', '01103'), ('name', 'ביה"ח אסף הרופה'), ('type', '1')]),
            SON([('hosp_code', '01108'), ('name', 'ביה"ח ברזילי'), ('type', '1')]),
            SON([('hosp_code', '01204'), ('name', 'ביה"ח בני ציון'), ('type', '1')]),
            SON([('hosp_code', '01107'), ('name', 'ביה"ח נהריה'), ('type', '1')]),
            SON([('hosp_code', '01106'), ('name', 'ביה"ח הלל יפה'), ('type', '1')]),
            SON([('hosp_code', '01109'), ('name', 'ביה"ח פוריה'), ('type', '1')]),
            SON([('hosp_code', '01102'), ('name', 'ביה"ח רמב"ם'), ('type', '1')]),
            SON([('hosp_code', '01201'), ('name', 'ביה"ח איכילוב'), ('type', '1')]),
            SON([('hosp_code', '01104'), ('name', 'ביה"ח וולפסון'), ('type', '1')]),
            SON([('hosp_code', '01105'), ('name', 'ביה"ח זיו'), ('type', '1')]),
            SON([('hosp_code', '01101'), ('name', 'ביה"ח שיבה'), ('type', '1')])
        ],
        'type_3': [
            SON([('hosp_code', '11101'), ('name', 'ביה"ח שער המנשה'), ('type', '3')]),
            SON([('hosp_code', '11102'), ('name', 'ביה"ח יהודה אברבנאל'), ('type', '3')]),
            SON([('hosp_code', '11103'), ('name', 'ביה"ח ע"ש פליגלמן מזור'), ('type', '3')]),
            SON([('hosp_code', '11104'), ('name', 'המרכז לבריאות הנפש בער יעקב'), ('type', '3')]),
            SON([('hosp_code', '11105'), ('name', 'המרכז הרפואי לברהנ לב השרון'), ('type', '3')]),
            SON([('hosp_code', '11106'), ('name', 'ביה"ח מעלה הכרמל'), ('type', '3')]),
            SON([('hosp_code', '11107'), ('name', 'המרכז לבריאות הנפש בער שבה'), ('type', '3')]),
            SON([('hosp_code', '11109'), ('name', 'מרכז רפואי לבריאות הנפש ירושלים'), ('type', '3')])
        ],
        'type_2': [
            SON([('hosp_code', '21101'), ('name', 'מרכז רפואי גריאטרי שמואל הרופא'), ('type', '2')]),
            SON([('hosp_code', '21102'), ('name', 'מרכז גריאטרי שיקומי ע"ש פלימן'), ('type', '2')]),
            SON([('hosp_code', '22101'), ('name', 'מרכז הגריאטרי המשולב ע"ש שוהם, פרדס'), ('type', '2')]),
            SON([('hosp_code', '22102'), ('name', 'מרכז גריאטרי דורות נתניה'), ('type', '2')]),
            SON([('hosp_code', '22103'), ('name', 'מרכז גריאטרי ראשל"צ'), ('type', '2')]),
            SON([('hosp_code', '31101'), ('name', 'מרכז קהילתי לבריאות הנפש - יפו'), ('type', '2')])
        ],
        'type_0': [
            SON([('hosp_code', '1'), ('name', 'חטיבה'), ('type', '0')])
        ]
    }
    mycol.insert_one(data)
# update('app_data_measure')

# get('app_data_decryptiontables', '5c164636326f423ce4c54b51')


# print_col('app_data_measure', fields={'measure_code', 'hospital_type'})
print_col('app_data_decryptiontables', {'name': 'business_topic'})
# print_col('app_data_version', fields={'version_name': 1})
# print_col('app_data_version', {'version_number': 1003})
# print_col('app_data_measure', fields={'business_topic','is_division', 'measure_name', 'measure_code'})
#print_col_names()
# print_col('app_data_nationalaverage')
# print_col('app_data_version')
# get_hosp()
# create_array()