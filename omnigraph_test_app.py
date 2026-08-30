
import db
def update_isolated():
    db.execute('UPDATE isolated_table SET val = 1')
