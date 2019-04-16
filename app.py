from flask import Flask, render_template, request, redirect, url_for, jsonify
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)


#Fake Restaurants
make = {'name': 'The CRUDdy Crab', 'id': '1'}

makes = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
carClasses = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
carClass =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


#Home/Root routing to show all car makes
@app.route('/')
@app.route('/make')
def showMakeMenu():
   return render_template('makes.html', makes = makes)

#Create a new car make
@app.route('/make/new')
def newMake():
    return "This page will be for making a new make"

#Edit an existing car make
@app.route('/make/<int:make_id>/edit')
def editMake(make_id):
    return "This page will be used for editing an existing %s make" % make_id

#Delete an existing car make
@app.route('/make/<int:make_id>/delete')
def deleteMake(make_id):
    return "This page will be for deleting an existing %s make" % make_id

#Show all models of a specific make
@app.route('/make/<int:make_id>')
@app.route('/make/<int:make_id>/class')
def showMakeModels(make_id):
    return "This page is to show all the models of a specific %s make" % make_id

#Add a new model based on make_id
@app.route('/make/<int:make_id>/class/new')
def addMakeModels(make_id):
    return "This page is for adding a new model to an existing %s make." % make_id

#Edit an existing model based on model_id
@app.route('/make/<int:make_id>/class/<int:model_id>/edit')
def editMakeModels(make_id, model_id):
    return "This page is to edit a %s model to an existing make" % model_id

#Delete an existing model based on model_id
@app.route('/make/<int:make_id>/class/<int:model_id>/delete')
def deleteMakeModels(make_id, model_id):
    return "This page is to delete a %s model to an existing make" % model_id

#Tells app to run on localhost:5000
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)