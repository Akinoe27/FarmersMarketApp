from app import app
from app import mysql
from flask import render_template
from flask import jsonify

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM product") 
    product_data = cursor.fetchall()
    cursor.close()
    return render_template('products.html', products = product_data)

@app.route('/orders')
def showOrders():
    return render_template('order_confirmation.html')

#route to test connection
# @app.route('/testconnect')
# def test_db():
#     try:
#         cursor = mysql.connection.cursor()
#         cursor.close()
#         print("Database credentials are all correct")
#         return jsonify({'message':'Database credentials are all goods'})
#     except Exception as e: 
#         print("Some of the database credentials is incorrect",str(e))
#         return jsonify({'message':'Database credentials error'})