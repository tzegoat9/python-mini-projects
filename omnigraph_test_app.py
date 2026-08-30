
# OmniGraph deletion test ts=1788091302
class Order:
    __tablename__ = "orders"

def process_order(order_id):
    Order.objects.filter(id=order_id).update(status="shipped")
