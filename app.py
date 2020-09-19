import importlib
from flask_lists import dbfunctions as dbfunc

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
secret = importlib.import_module("secret")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = secret.mysql_link
db = SQLAlchemy(app)


class Lists(db.Model):
    __tablename__ = "lists"
    id = db.Column("id", db.Integer, primary_key=True)
    list_name = db.Column("list_name", db.Unicode)
    list_items = db.Column("list_items", db.Unicode)

class Items(db.Model):
    __tablename__ = "items"
    id = db.Column("id", db.Integer, primary_key=True)
    item_name = db.Column("item_name", db.Unicode)




@app.route('/')
def index():
    lists = Lists().query.all()
    print(lists)
    list_names = [l.list_name for l in lists]

    return render_template("index.html", lists=list_names)


@app.route('/<list_name>')
def list(list_name):

    item_names_array = dbfunc.get_items_from_list(list_name)


    return render_template("list.html", items=item_names_array, list_name=list_name)


@app.route('/update_<list_name>')
def update(list_name):
    item_names_array = dbfunc.get_items_from_list(list_name)
    all_items = dbfunc.get_all_Items()
    unused_items = [x for x in all_items if x not in item_names_array]
    return render_template("update.html", items=item_names_array, list_name=list_name, all_items=all_items, unused_items=unused_items)


if __name__ == '__main__':
    app.run(port=80, debug=True)
