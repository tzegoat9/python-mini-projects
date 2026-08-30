
# OmniGraph e2e test ts=1788090415
class Order:
    __tablename__ = "orders"

class Inventory:
    __tablename__ = "inventory"

def process_order(order_id):
    Order.objects.filter(id=order_id).update(status="shipped")

def update_inventory(product_id):
    Inventory.objects.filter(product_id=product_id).update(qty=0)
