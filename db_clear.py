#!myvenv/bin/python3

from app import db, models


users = models.User.query.all()
for u in users:
    db.session.delete(u)

scores = models.Score.query.all()
for s in scores:
    db.session.delete(s)

db.session.commit()

print('DB was cleared.')
