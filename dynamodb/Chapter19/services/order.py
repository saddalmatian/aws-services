from db import order

def create_order(order_info,customer_id,order_list):
    return order.create_order(order_info,customer_id,order_list)
   

def get_order_details(order_id):
    return order.get_order_details(order_id)

    
def update_order(order_status,order_id,customer_id):
    return order.update_order(order_status,order_id,customer_id)

    