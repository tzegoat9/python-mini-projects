
import db
def update_user():
    # Dev forgot the lock!
    db.execute('UPDATE users SET status = "active"')
