from ..domains import order


class OrderIn(order.Order):
    pass

class OrderResp(order.OrderInDB):
    pass

class OrderItemIn(order.OrderItems):
    pass

class CustomerResp(order.Order):
    pass
