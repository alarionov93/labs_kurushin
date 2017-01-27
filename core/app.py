from flask import Flask
from flask import render_template
from flask import request

from core.models import User, Good

app = Flask(__name__) # инициализируем приложение

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/users/', methods=['GET'])
def users():
    users = User.select().order_by('name')

    return render_template('users.html', users=users)

@app.route('/users/add/', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        passwd = request.form['passwd']
        if name and email and passwd:
            if len(User.filter(email=email)) > 0:
                return render_template('new_user.html', success=False, info='Email уже существует')
            try:
                user = User(name=name, email=email, passwd=passwd)
                user.save()
            except Exception as e:
                return render_template('new_user.html', success=False, info='Неизвестная ошибка')
        else:
            return render_template('new_user.html', success=False, info='Не заполнены обязательные поля')

        return render_template('new_user.html', success=True)
    else:
        return render_template('new_user.html')

@app.route('/goods/', methods=['GET'])
def goods():
    goods = Good.select().order_by('name')

    return render_template('goods.html', goods=goods)

@app.route('/goods/add/', methods=['GET', 'POST'])
def add_good():
    if request.method == 'POST':
        good_name = request.form['name']
        good_price = request.form['price']
        if good_name and good_price:
            good = Good(name=good_name, price=good_price)
            good.save()
        else:
            render_template('new_good.html', success=False, info='Не заполнены обязательные поля')

        return render_template('new_good.html', success=True)
    else:
        return render_template('new_good.html')