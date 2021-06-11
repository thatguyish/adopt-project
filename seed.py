from app import app
from models import db,Pet

db.drop_all()
db.create_all()

pets = [Pet(name='bongo',species='monkey',photo_url='https://c.files.bbci.co.uk/E9DF/production/_96317895_gettyimages-164067218.jpg'),Pet(name='jimmy',species='cat',photo_url='https://www.humanesociety.org/sites/default/files/styles/1240x698/public/2020-07/kitten-510651.jpg?h=f54c7448&itok=ZhplzyJ9'),Pet(name='echo',species='bat',photo_url='https://www.eea.europa.eu/highlights/bat-population-recovering/image_print'),Pet(name='jojo',species='dog',photo_url='https://www.humanesociety.org/sites/default/files/styles/1240x698/public/2018/08/puppy-410265.jpg?h=0c7c9985&itok=ZQixcJRY'),Pet(name='spike',species='porcupine',photo_url='https://www.meigspointnaturecenter.org/wp-content/uploads/2020/05/nature-3588682_1280-1024x662.jpg'),Pet(name='trunks',species='elephant',photo_url='https://assets.nrdc.org/sites/default/files/styles/full_content--retina/public/media-uploads/wlds43_654640_2400.jpg?itok=LbhnLIk9'),Pet(name='gerald',species='T.Rex',photo_url='https://images.theconversation.com/files/200952/original/file-20180105-26154-1wiqvem.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=1200.0&fit=crop')]

db.session.add_all(pets)

db.session.commit()