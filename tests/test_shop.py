import pytest
from models import PhysicalProduct, Order, Customer
from exceptions import InsufficientStockError
from services import OrderService

def test_grand_total_with_discount():

    # Založení fyzického produktu
    notebook = PhysicalProduct("Notebook", 23000.00, 5, 2.34,0.21)

    # Založení zákznika se slevou
    vip_customer = Customer("V001", "John",10.0)

    # vytvoření objednákvy a přidání produktu do objednávky
    order = Order("ORD-TEST", vip_customer)
    order.add_item(notebook,1)

    # Zpočítání celkové ceny
    total = order.calculate_grand_total()

    assert total == 25047.00


def test_process_order_fails_when_out_of_stocks():

    # Založení fyzického produktu
    mouse = PhysicalProduct("Myš Logitech", 1200.00,1,0.2,0.21)

    customer = Customer("V001", "Bob",0.0)

    #Založení objednávky a pokus o přidání většího množství, než je aktuálně na skladě
    order = Order("ORD-TEST",customer)
    order.add_item(mouse,5)

    orderService = OrderService()

    with pytest.raises(InsufficientStockError):
        orderService.process_order(order)

    

    