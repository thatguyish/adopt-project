from models import connectdb
from flask import Flask,render_template,redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import connectdb,Pet,db
from forms import PetForm
import inspect

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///adopt'
app.config['SECRET_KEY']='secretkey1'

connectdb(app)

@app.route('/')
def list_pets():
    """lists all pets"""

    all_pets = Pet.query.all()
    return render_template('home.html',all_pets=all_pets)

@app.route('/add',methods=['POST','GET'])
def add_pet():
    """display a form that allows you to add new pets"""

    form = PetForm()
    form.available.widget.input_type = 'hidden'
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        db.session.add(Pet(name=name,species=species,photo_url=photo,age =age,notes=notes))
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html',form=form)


@app.route('/<pet_id>',methods=['POST','GET'])
def pet_display(pet_id):
    """display pet information and allows you to edit it"""

    pet = Pet.query.get(pet_id)
    form = PetForm(obj=pet)
    form.available.widget.input_type = 'checkbox'

    petinfo = dict()
    for val in form:
        if val.data:
            name = val.name
            data = val.data
            petinfo[name]=data
    
    for (k,v) in petinfo.items():
        print(k,v)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data
        pet.photo_url=photo_url
        pet.notes = notes
        pet.available = available
        db.session.add(pet)
        db.session.commit()
        return redirect(f'/{pet_id}')
    else:
        return render_template('pet_display.html',pet=pet,form=form)

