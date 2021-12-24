from db import customer


def get_customer(id):
    return customer.get_customer(id)

def get_customer_order(customer_id):
    return customer.get_customer_order(customer_id)

def create_customer(customer_info):
    return customer.create_customer(customer_info)

def create_customer_email(customer_name,customer_email):
    return customer.create_customer_email(customer_name,customer_email)

def update_email(customer_name,customer_email):
    return customer.update_email(customer_name,customer_email)

def delete_email(customer_name):
    return customer.delete_email(customer_name)    

