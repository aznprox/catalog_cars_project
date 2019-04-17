from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Make, Model

app = Flask(__name__)

engine = create_engine('sqlite:///carmake.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#------------------
#JSON API ENDPOINTS
#------------------

@app.route('/makes/JSON')
def showMakesJSON():
    makes = session.query(Make).all()
    return jsonify(AllMakes=[m.serialize for m in makes])

@app.route('/makes/<int:make_id>/JSON')
def showOneMakeJSON(make_id):
    oneMake = session.query(Make).filter_by(id=make_id).one()
    return jsonify(Make=[oneMake.serialize])

@app.route('/make/<int:make_id>/model/JSON')
def showMakeModelsJSON(make_id):
    models = session.query(Model).filter_by(make_id=make_id).all()
    return jsonify(AllModels=[m.serialize for m in models])

@app.route('/make/<int:make_id>/model/<int:model_id>/JSON')
def showOneModelJSON(make_id, model_id):
    model = session.query(Model).filter_by(id=model_id).one()
    return jsonify(oneModel=model.serialize)

#--------------------
#CRUD FUNCTIONALITIES
#--------------------

#Home/Root routing to show all car makes
@app.route('/')
@app.route('/makes')
def showMakeMenu():
    makes = session.query(Make).all()
    session.close()
    return render_template('makes.html', makes = makes)

#Create a new automobile make
@app.route('/makes/new', methods=['GET', 'POST'])
def newMake():
    if request.method == 'POST':
        newMake = Make(
        name=request.form['name'], 
        image=request.form['image'],
        description=request.form['description'])
     
        session.add(newMake)
        session.commit()
        return redirect(url_for('showMakeMenu'))
    else:
        return render_template('newMake.html')

#Edit an existing car make
@app.route('/makes/<int:make_id>/edit', methods=['GET', 'POST'])
def editMake(make_id):
    editedMake = session.query(Make).filter_by(id=make_id).one()
    if request.method =='POST':
        if request.form['name']:
            editedMake.name = request.form['name']
        if request.form['image']:
            editedMake.image = request.form['image']
        if request.form['description']:
            editedMake.description = request.form['description']
        session.add(editedMake)
        session.commit()
        return redirect(url_for('showMakeMenu'))
    else:
        return render_template('editMake.html', make_id=make_id, beingEditedMake = editedMake)

#Delete an existing car make
@app.route('/makes/<int:make_id>/delete', methods=['GET', 'POST'])
def deleteMake(make_id):
    makeToDelete = session.query(Make).filter_by(id=make_id).one()
    if request.method == 'POST':
        session.delete(makeToDelete)
        session.commit()
        return redirect(url_for('showMakeMenu'))
    else:
        return render_template('deleteMake.html', make = makeToDelete)
    
#Show all the models of a specific make
@app.route('/make/<int:make_id>/model')
def showMakeModels(make_id):
    make = session.query(Make).filter_by(id=make_id).one()
    models = session.query(Model).filter_by(make_id=make_id)
    return render_template('selections.html', make_id = make_id, models=models, make=make)

#Add a new model based on make_id
@app.route('/make/<int:make_id>/model/new', methods=['GET', 'POST'])
def addMakeModels(make_id):
    if request.method == 'POST':
        newModel = Model(
            name=request.form['name'],
            image=request.form['image'],
            description=request.form['description'],
            price=request.form['price'],
            make_id=make_id
        )
        session.add(newModel)
        session.commit()
        return redirect(url_for('showMakeModels', make_id = make_id))
    else:
        return render_template('newModel.html', make_id = make_id)

#Edit an existing model based on model_id
@app.route('/make/<int:make_id>/model/<int:model_id>/edit', methods =['GET', 'POST'])
def editMakeModels(make_id, model_id):
    editedModel = session.query(Model).filter_by(id=model_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedModel.name = request.form['name']
        if request.form['description']:
            editedModel.description = request.form['name']
        if request.form['price']:
            editedModel.price = request.form['price']
        if request.form['image']:
            editedModel.image = request.form['image']
        session.add(editedModel)
        session.commit()
        return redirect(url_for('showMakeModels', make_id = make_id))
    else:
        return render_template('editModel.html',make_id=make_id, model_id = model_id, model = editedModel)

#Delete an existing model based on model_id
@app.route('/make/<int:make_id>/model/<int:model_id>/delete', methods =['GET', 'POST'])
def deleteMakeModels(make_id, model_id):
    deleteModel = session.query(Model).filter_by(id=model_id).one()
    if request.method == 'POST':
        session.delete(deleteModel)
        session.commit()
        return redirect(url_for('showMakeModels', make_id = make_id))
    else:
        return render_template('deleteModel.html', model = deleteModel)


#Tells app to run on localhost:8000
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)