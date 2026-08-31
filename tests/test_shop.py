import pytest
from models import PhysicalProduct, Order, Customer, PercentageDiscount, NoDiscount
from exceptions import InsufficientStockError
from services import OrderService

def test_grand_total_with_discount_manual_discount():
    """Ověří, že objednávka správně počítá celkovou cenu včetně zákaznické slevy"""

    # 1. Vytvoření produktu
    notebook = PhysicalProduct("Notebook",10000.0, 5,2.3)

    # 2. vytvoření zákazníka
    vip_customer = Customer("V001", "John",10.0)

    # 3. vytvoření objednávkya přidání jednoho kusu - tak abych neporušil množství na skladě

    order = Order("ORD-TEST",vip_customer)
    order.add_item(notebook,1)

    # 4. spočítání celkové ceny --> 10000 - 10% = 9.10980 Kč
    total = order.calculate_grand_total()

    assert total == 10890.0

def test_grand_total_with_discount_with_discount_class():
    """Ověrí, že správně funguje počítání slevy se třídou Discount"""
     # 1. Vytvoření produktu
    notebook = PhysicalProduct("Notebook",10000.0, 5,2.3)
    
    # 2. vytvoření zákazníka
    vip_customer = Customer("V001", "John",PercentageDiscount(10.0))
    
    # 3. vytvoření objednávkya přidání jednoho kusu - tak abych neporušil množství na skladě
    
    order = Order("ORD-TEST",vip_customer)
    order.add_item(notebook,1)
    
    # 4. spočítání celkové ceny --> 10.000 - 10% = 10890 Kč
    total = order.calculate_grand_total()
    
    assert total == 10890.0

def test_process_order_success():
    "Ověří, že proces objednávky proběhl správně a správně se odečetli položky ze skladu"

    mouse = PhysicalProduct("Myš Logitech",1000.0,10,0.3)

    customer = Customer("C-001", "Jackob", NoDiscount())

    order = Order("ORD-001",customer)
    order.add_item(mouse,2)

    order_service = OrderService()
    final_price = order_service.process_order(order)

    assert final_price == 2420.0
    assert mouse._stock_quantity == 8

def test_process_order_fails_when_out_of_stock():
    """Ověří, že systém vyhodí vyjímku, pokud na skladě není dostatečné množství zboží"""

    headphones = PhysicalProduct("Sluchátka",1500.0,1,0.3)
    customer = Customer("C002", "Bob", NoDiscount())

    order = Order("ORD-002",customer)
    order.add_item(headphones,2)

    order_service = OrderService()

    with pytest.raises(InsufficientStockError):
        order_service.process_order(order)