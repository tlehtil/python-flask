Project to study Flask
Following steps from The Flask Mega-Tutorial
Maybe somedat will become something useful


Tips, tricks, howto etc.:
Running:
flask run
With browser go to http://127.0.0.1:5000


Updating database models:
flask db migrate -m "name_of_table table"
flask db upgrade

Adding new users:
flask shell
from app.models import User
from app import db
u = User(username='teemu', email='teemu@lehti.la')
u.set_password('salasana')
db.session.add(u)
db.session.commit()

Reset password:
flask shell
from app.models import User
from app import db
#Get user id:
users = User.query.all()
users
[<ID: 1> <User teemu>]
u = User.query.get(ID)
u.set_password('salasana')
db.session.commit()