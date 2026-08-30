
import db
def update_settings():
    db.transaction()
    db.execute('UPDATE settings SET val = 1')
