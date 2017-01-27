from peewee import *

# db = 'data.db'

db = SqliteDatabase('data.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField(unique=False, null=False, default='')
    email = CharField(unique=True, null=False)
    passwd = CharField(unique=False, null=False)

    @property
    def new_events_count(self):
        return 1

    def to_json(self):
        return {
            'name': self.name,
            'email': self.email
        }

class Good(BaseModel):
    name = CharField(unique=False, null=False, default='')
    price = CharField(unique=False, null=False, default=0)

    def to_json(self):
        return {
            'name': self.name,
            'price': self.price
        }
