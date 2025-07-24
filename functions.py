import requests
import json

BASE_URL = "https://34.160.0.69.nip.io/v1/order-management"

def create_order(order_data):
    """
    Creates an order.
    Corresponds to operationId: createOrder
    """
    url = f"{BASE_URL}/orders"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(order_data), headers=headers)
    return response.json()

def fetch_orders():
    """
    Fetches all orders.
    Corresponds to operationId: fetchOrders
    """
    url = f"{BASE_URL}/orders"
    response = requests.get(url)
    return response.json()

def get_order(order_id):
    """
    Gets an order by ID.
    Corresponds to operationId: getOrder
    """
    url = f"{BASE_URL}/orders/{order_id}"
    response = requests.get(url)
    return response.json()

def update_order(order_id, order_data):
    """
    Updates an order.
    Corresponds to operationId: updateOrder
    """
    url = f"{BASE_URL}/orders/{order_id}"
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, data=json.dumps(order_data), headers=headers)
    return response.json()

def delete_order(order_id):
    """
    Deletes an order.
    Corresponds to operationId: deleteOrder
    """
    url = f"{BASE_URL}/orders/{order_id}"
    response = requests.delete(url)
    return response.json()



