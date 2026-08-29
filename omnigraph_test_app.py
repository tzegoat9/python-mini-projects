
import db
def update_user():
    db.advisory_lock('users')
    db.execute('UPDATE users SET status = "active"')
