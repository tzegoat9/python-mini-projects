
# Python Service Writing to Global Users (ts=1788097805)
import db

def onboard_user(user_id):
    db.execute("INSERT INTO global_users (id, status) VALUES (?, 'onboarded')", user_id)
