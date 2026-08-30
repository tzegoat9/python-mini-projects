
import db

# OmniGraph end-to-end test PR, timestamp=1788090333
def process_order():
    db.execute("UPDATE orders SET status = 'shipped' WHERE id = 1")

def update_inventory():
    db.execute("UPDATE inventory SET qty = qty - 1 WHERE product_id = 1")
