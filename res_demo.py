from flask import Flask, flash, g, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
import secrets
import plotly.express as px
import plotly.io as pio
import io
import base64
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, validators ,SelectField

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
# Kết nối đến MongoDB
client = MongoClient("mongodb://localhost:27017/")
# Chọn cơ sở dữ liệu, tên cơ sở dữ liệu là "new_restaurant_database"
db = client["demo"]
# Chọn collection, tên collection là "restaurants"
collection = db["OpenS"]


@app.route('/add_restaurant', methods=['GET', 'POST'])
def add_restaurant():
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        borough = request.form['borough']
        cuisine = request.form['cuisine']
        name = request.form['name']
        restaurant_id = request.form['restaurant_id']
        approved = request.form.get('approved', False)
        pending_approval = request.form.get('pending_approval', True)

        # Tạo một dictionary đại diện cho nhà hàng mới
        new_restaurant = {
            "borough": borough,
            "cuisine": cuisine,
            "name": name,
            "restaurant_id": restaurant_id,
            "approved": approved,
            "pending_approval": pending_approval
        }

        # Thêm nhà hàng mới vào cơ sở dữ liệu
        collection.insert_one(new_restaurant)

        # Chuyển hướng người dùng đến trang hiển thị danh sách nhà hàng
        return redirect(url_for('list_restaurants'))

    # Nếu là phương thức GET, hiển thị form để nhập thông tin nhà hàng
    return render_template('add_restaurant.html')

@app.route('/edit_restaurant/3', methods=['GET', 'POST'])
def edit_restaurant(restaurant_id):
    if request.method == 'POST':
        # Lấy dữ liệu từ form
        borough = request.form['borough']
        cuisine = request.form['cuisine']
        name = request.form['name']
        approved = request.form.get('approved', False)
        pending_approval = request.form.get('pending_approval', True)

        # Cập nhật thông tin của nhà hàng trong cơ sở dữ liệu
        collection.update_one(
            {"_id": ObjectId(restaurant_id)},
            {"$set": {
                "borough": borough,
                "cuisine": cuisine,
                "name": name,
                "approved": approved,
                "pending_approval": pending_approval
            }}
        )

        # Chuyển hướng người dùng đến trang hiển thị danh sách nhà hàng
        return redirect(url_for('list_restaurants'))

    # Nếu là phương thức GET, hiển thị form để sửa thông tin nhà hàng
    restaurant = collection.find_one({"_id": ObjectId(restaurant_id)})
    return render_template('edit_restaurant.html', restaurant=restaurant)


if __name__ == '__main__':
    app.run(debug=True)