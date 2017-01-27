from core import models

models.db.connect()

try:
    print("Try to remove table User...")
    models.db.drop_table(models.User)
except Exception as e:
    print(e)
finally:
    print("Try to create table User...")
    models.db.create_table(models.User)

try:
    print("Try to remove table Good...")
    models.db.drop_table(models.Good)
except Exception as e:
    print(e)
finally:
    print("Try to create table Good...")
    models.db.create_table(models.Good)


models.db.close()