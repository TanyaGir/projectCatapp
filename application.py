from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mydatabase_setup import Base, Category, Item

engine = create_engine('sqlite:///catalog.db')
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/catalog')
def showCatalog():
    category = session.query(Category).all()
    catArray=[]
    itemArray=[]
    latArray=[]
    output = ''
    for c in category:
        catArray.append(c.name)
        item = session.query(Item).filter_by(cat_id = c.id).order_by(Item.item_date.desc()).limit(1).all()

        for i in item:
            itemArray.append(i.item_name)
    return render_template('index.html',categories = catArray, items = itemArray)

#show all the items in a category
@app.route('/catalog/<int:category_id>/items')
def showItems(category_id):
    selecteditems = session.query(Item).filter_by(cat_id = category_id).all()
    return render_template('items.html',items = selecteditems)

#create/add a new menu item
@app.route('/catalog/<int:category_id>/items/new' ,methods=['GET','POST'])
def newItem(category_id):
    catalogitem = session.query(Category).filter_by(id = category_id).one()
    if request.method == 'POST':
        newItem = Item(item_name = request.form['name'],
                       item_description = request.form['description'],
                       cat_id = category_id )
        session.add(newItem)
        session.commit()
        return redirect(url_for('showItems', category_id=category_id))
    else:
       return render_template('newItem.html', category_id = category_id, catalogitem = catalogitem)

#delete a items
@app.route('/catalog/<int:category_id>/items/<int:item_id>/delete', methods=['GET','POST'])
def deleteItem(category_id, item_id):
    catalogitem = session.query(Category).filter_by(id = category_id).one()
    itemToDelete = session.query(Item).filter_by(item_id = item_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showItems', category_id= category_id))
    else:
        return render_template('deleteItem.html', item = itemToDelete)



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)
