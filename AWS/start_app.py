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
        postgreSQL_insert_Query =  """ INSERT INTO machine(machine_uuid, machine_latitude,machine_longitude,machine_avg_footfall,machine_json)  VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (machine_uuid, machine_latitude, machine_longitude, machine_avg_footfall, machine_json)
        cursor.execute(postgreSQL_insert_Query,record_to_insert)
        connection.commit()

    except Exception as error:
        print(str(error))

    finally:
        if(connection):
            cursor.close()
            connection.close()
            
            
def postProductData(product_id, product_name, product_price, product_info):
    try:
        connection = psycopg2.connect(user= user,password=password,host=host,port=port,database=database)
        cursor = connection.cursor()
        postgreSQL_insert_Query =  """ INSERT INTO product(product_id, product_name,product_price,product_info)  VALUES (%s,%s,%s,%s)"""
        record_to_insert = (machine_uuid, machine_latitude, machine_longitude, machine_avg_footfall, machine_json)
        cursor.execute(postgreSQL_insert_Query,record_to_insert)
        connection.commit()

    except Exception as error:
        print(str(error))

    finally:
        if(connection):
            cursor.close()
            connection.close()          
            
def postShopData(shop_uuid, shop_json):
    try:
        connection = psycopg2.connect(user= user,password=password,host=host,port=port,database=database)
        cursor = connection.cursor()
        postgreSQL_insert_Query =  """ INSERT INTO shop(shop_uuid, shop_json)  VALUES (%s,%s)"""
        record_to_insert = (shop_uuid, shop_json)
        cursor.execute(postgreSQL_insert_Query,record_to_insert)
        connection.commit()

    except Exception as error:
        print(str(error))

    finally:
        if(connection):
            cursor.close()
            connection.close()
            
            
def putMachineData(machine_uuid, machine_latitude, machine_longitude, machine_avg_footfall, machine_json):
    try:
        connection = psycopg2.connect(user= user,password=password,host=host,port=port,database=database)
        cursor = connection.cursor()
        postgreSQL_insert_Query =  """ UPDATE machine set machine_uuid = %s, machine_latitude = %s ,machine_longitude = %s, machine_avg_footfall = %s, machine_json = %s where machine_uuid = '"""+ machine_uuid + "'"
        record_to_insert = (machine_uuid, machine_latitude, machine_longitude, machine_avg_footfall, machine_json)
        cursor.execute(postgreSQL_insert_Query,record_to_insert)
        connection.commit()

    except Exception as error:
        print(str(error))

    finally:
        if(connection):
            cursor.close()
            connection.close()
            
            
def putProductData(product_id, product_name, product_price, product_info):
    try:
        connection = psycopg2.connect(user= user,password=password,host=host,port=port,database=database)
        cursor = connection.cursor()
        postgreSQL_insert_Query =  """ UPDATE product set product_id = %s, product_name = %s, product_price = %s, product_info = %s where product_id = '"""+ product_id + "'"
        record_to_insert = (product_id, product_name, product_price, product_info)
        cursor.execute(postgreSQL_insert_Query,record_to_insert)
        connection.commit()

    except Exception as error:
        print(str(error))

    finally:
        if(connection):
            cursor.close()
            connection.close()
            
            
def putShopData(shop_uuid, shop_json):
    try:
        connection = psycopg2.connect(user= user,password=password,host=host,port=port,database=database)
        cursor = connection.cursor()
        postgreSQL_insert_Query =  """ UPDATE shop set shop_uuid = %s, shop_json = %s where shop_uuid = '"""+ shop_uuid + "'"
        record_to_insert = (shop_uuid, shop_json)
        cursor.execute(postgreSQL_insert_Query,record_to_insert)
        connection.commit()

    except Exception as error:
        print(str(error))

    finally:
        if(connection):
            cursor.close()
            connection.close()
            
            
def deleteMachineData(machine_uuid):
    try:
        connection = psycopg2.connect(user= user,password=password,host=host,port=port,database=database)
        cursor = connection.cursor()
        postgreSQL_insert_Query =  """ DELETE from machine where machine_uuid = '"""+ machine_uuid + "'"
        cursor.execute(postgreSQL_insert_Query)
        connection.commit()

    except Exception as error:
        print(str(error))

    finally:
        if(connection):
            cursor.close()
            connection.close()
            
            
def deleteProductData(product_id):
    try:
        connection = psycopg2.connect(user= user,password=password,host=host,port=port,database=database)
        cursor = connection.cursor()
        postgreSQL_insert_Query =  """ DELETE from product where product_id = '"""+ product_id + "'"
        cursor.execute(postgreSQL_insert_Query)
        connection.commit()

    except Exception as error:
        print(str(error))

    finally:
        if(connection):
            cursor.close()
            connection.close()
            
            
def deleteShopData(shop_uuid):
    try:
        connection = psycopg2.connect(user= user,password=password,host=host,port=port,database=database)
        cursor = connection.cursor()
        postgreSQL_insert_Query =  """ DELETE from shop where shop_uuid = '"""+ shop_uuid +"'"
        cursor.execute(postgreSQL_insert_Query)
        connection.commit()

    except Exception as error:
        print(str(error))

    finally:
        if(connection):
            cursor.close()
            connection.close()

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
        machine_json = json.dumps(json_str)
        postMachineData(json_str["uuid"], json_str["latitude"], json_str["longitude"], json_str["avg_footfall"], machine_json)
        response = Response("Success", status = 200, mimetype="text/plain")
    return response

#tbd
@app.route("/machines/<machine_uuid>", methods = ["GET","PUT","DELETE"])
def returnSingleMachineInfo(machine_uuid):
    
    if request.method == "GET":
        query = "Select * from machine where machine_uuid = '" + str(machine_uuid) + "'"
        data = queryData(query)
        response = Response(json.dumps(data, indent = 4), status = 200, mimetype="application/json")
        
    if request.method == "PUT":
        json_str = request.get_json()
        machine_json = json.dumps(json_str)
        putMachineData(json_str["uuid"], json_str["latitude"], json_str["longitude"], json_str["avg_footfall"], machine_json)
        response = Response("Success", status = 200, mimetype="text/plain")
        
    if request.method == "DELETE":
        json_str = request.get_json()
        deleteMachineData(json_str["uuid"])
        response = Response("Success", status = 200, mimetype="text/plain")
    
    
    return response

@app.route("/shops", methods = ["GET","POST"])
def returnListOfShops():
    
    if request.method == "GET":
        query = "Select * from shop"
        data = queryData(query)
        response = Response(json.dumps(data, indent = 4), status = 200, mimetype="application/json") 
    
    if request.method == "POST":
        json_str = request.get_json()
        shop_json = json.dumps(json_str)
        postShopData(json_str["uuid"], shop_json)
        response = Response("Success", status = 200, mimetype="text/plain")
        
    return response

@app.route("/shops/<shop_uuid>", methods = ["GET","PUT","DELETE"])
def returnSingleShopinfo(shop_uuid):
    
    if request.method == "GET":
        query = "Select * from shop where shop_uuid = '" + str(shop_uuid) + "'"
        data = queryData(query)
        response = Response(json.dumps(data, indent = 4), status = 200, mimetype="application/json") 
    
    if request.method == "PUT":
        json_str = request.get_json()
        machine_json = json.dumps(json_str)
        putShopData(json_str["uuid"], shop_json)
        response = Response("Success", status = 200, mimetype="text/plain")
        
        
    if request.method == "DELETE":
        json_str = request.get_json()
        deleteShopData(json_str["uuid"])
        response = Response("Success", status = 200, mimetype="text/plain")
        
    return response

@app.route("/products", methods = ["GET","POST"])
def returnListOfProduct():
    
    if request.method == "GET":
        query = "Select * from product"
        data = queryData(query)
        response = Response(json.dumps(data, indent = 4), status = 200, mimetype="application/json") 
        
        
    if request.method == "POST":    
        json_str = request.get_json()
        product_info = json.dumps(json_str)
        postProductData(json_str["uuid"], json_str["product_name"], json_str["product_price"], product_info)
        response = Response("Success", status = 200, mimetype="text/plain")
    
    return response



@app.route("/products/<product_uuid>", methods = ["GET","PUT","DELETE"])
def returnSingleProductInfo(product_uuid):
    
    if request.method == "GET":
        query = "Select * from product where product_id = '" + str(product_uuid) + "'"
        data = queryData(query)
        response = Response(json.dumps(data, indent = 4), status = 200, mimetype="application/json") 
    
    if request.method == "PUT":
        json_str = request.get_json()
        machine_json = json.dumps(json_str)
        putProductData(json_str["uuid"], json_str["product_name"], json_str["product_price"], product_info)
        response = Response("Success", status = 200, mimetype="text/plain")
        
        
    if request.method == "DELETE":
        json_str = request.get_json()
        deleteProductData(json_str["uuid"])
        response = Response("Success", status = 200, mimetype="text/plain")
        
        
    return response


app.run(host='0.0.0.0', port=8081)