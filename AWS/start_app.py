from flask import Flask, Response, request
import json
import psycopg2

host = "borneohacker93.postgres.database.azure.com"
port = 5432
database = "data"
user = "borneohacker93@borneohacker93"
password = "Kolomee93"


def queryData(query):
    data = []
    try:
        connection = psycopg2.connect(user= user,password=password,host=host,port=port,database=database)
        cursor = connection.cursor()
        postgreSQL_select_Query = query
        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall()
    except Exception as error:
        print(str(error))

    finally:
        if(connection):
            cursor.close()
            connection.close()
        return data
    
def postMachineData(machine_uuid, machine_latitude, machine_longitude, machine_avg_footfall, machine_json):
    try:
        connection = psycopg2.connect(user= user,password=password,host=host,port=port,database=database)
        cursor = connection.cursor()
        postgreSQL_insert_Query =  """ INSERT INTO word_info(machine_uuid, machine_latitude,machine_longitude,machine_avg_footfall)  VALUES (%s,%s,%s,%s)"""
        record_to_insert = (machine_uuid, machine_latitude, machine_longitude, machine_avg_footfall, machine_json)
        cursor.execute(postgreSQL_select_Query)
        data = cursor.fetchall()
    except Exception as error:
        print(str(error))

    finally:
        if(connection):
            cursor.close()
            connection.close()
        return data
    
    
    
    



app = Flask(__name__)
wsgi_app = app.wsgi_app



@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/returnsum')
def index1():
    return 'return sum'

@app.route("/heartbeat", methods = ["GET"])
def heartbeat():
    return "Alive"

#tbd
@app.route("/machines", methods = ["GET","POST"])
def returnListOfMachines():
    
    if request.method == "GET":
        query = "Select * from machine"
        data = queryData(query)
        
        response = Response(json.dumps(data, indent = 4), status = 200, mimetype="application/json") 
        
        
    if request.method == "POST":
        
        json_str = request.get_json()
        print(json_str[""])
        
        
    
    return response

#tbd
@app.route("/machines/<machine_uuid>", methods = ["GET","PUT","DELETE"])
def returnSingleMachineInfo(machine_uuid):
    
    if request.method == "GET":
        query = "Select * from machine where machine_uuid = '" + str(machine_uuid) + "'"
        data = queryData(query)
        
        response = Response(json.dumps(data, indent = 4), status = 200, mimetype="application/json") 
    
    
    return response

@app.route("/shops", methods = ["GET","POST"])
def returnListOfShops():
    
    if request.method == "GET":
        query = "Select * from shop"
        data = queryData(query)
        
        response = Response(json.dumps(data, indent = 4), status = 200, mimetype="application/json") 
        
    
    
    return response

@app.route("/shops/<shop_uuid>", methods = ["GET","POST","PUT","DELETE"])
def returnSingleShopinfo(shop_uuid):
    
    if request.method == "GET":
        query = "Select * from shop where shop_uuid = '" + str(shop_uuid) + "'"
        data = queryData(query)
        
        response = Response(json.dumps(data, indent = 4), status = 200, mimetype="application/json") 
    
    
    return response

@app.route("/products", methods = ["GET","POST"])
def returnListOfProduct():
    
    if request.method == "GET":
        query = "Select * from product"
        data = queryData(query)
        
        response = Response(json.dumps(data, indent = 4), status = 200, mimetype="application/json") 
    
    return response



@app.route("/products/<product_uuid>", methods = ["GET","POST","PUT","DELETE"])
def returnSingleProductInfo(product_uuid):
    
    if request.method == "GET":
        query = "Select * from product where product_id = '" + str(product_uuid) + "'"
        data = queryData(query)
        
        response = Response(json.dumps(data, indent = 4), status = 200, mimetype="application/json") 
    
    
    return response


app.run(host='0.0.0.0', port=8081)