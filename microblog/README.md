Project to study Flask  
Following steps from The Flask Mega-Tutorial  
Maybe someday will become something useful  

Tips, tricks, howto etc.:  
For start:
```
flask db migrate
flask db upgrade
```

Running:  
`flask run`  
With browser go to http://127.0.0.1:5000

Updating database models:
```
flask db migrate -m "name_of_table table"  
flask db upgrade
```

Adding new users:
```
flask shell
from app.models import User
from app import db
u = User(username='user', email='user@email.com')
u.set_password('salasana')
db.session.add(u)
db.session.commit()
```

Reset password:
```
flask shell
from app.models import User
from app import db
#Get user id:
users = User.query.all()
users
[<ID: 1> <User user>]
u = User.query.get(ID)
u.set_password('salasana')
db.session.commit()
```

Set api-key for ms translate-service:
```export MS_TRANSLATOR_KEY=YOURKEYHERE```