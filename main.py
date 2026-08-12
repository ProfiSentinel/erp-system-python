from models import PhysicalProduct, Customer, Order
from exceptions import InsufficientStockError
from services import OrderService

if __name__ == "__main__":
    # Založení fyzického produktu - skladem 5 kusů
    notebook = PhysicalProduct(
        name="Gaming Laptop", base_price=20000.0, stock_quantity=5, weight_kg=2.5
    )

   # Založení zákazníka se se slevou 10 %
    vip_customer = Customer(
        customer_id="C001", name="Jan Novák", discount_percentage=10.0
    )

    # Vytvoření objednávky se zákazníkem a přidání položky do objednávky
    order = Order(order_id="ORD-2026-001", customer=vip_customer)
    order.add_item(notebook, quantity=2)  

    # Zpracování objednávky přes OrderService
    service = OrderService()

    try:
        total_price = service.process_order(order)
        print(f"Objednávka úspěšně zpracována!")
        print(f"Cena po slevě a včetně DPH: {total_price} Kč")
        print(f"Zbývající kusy na skladě: {notebook._stock_quantity}")

        # Pokusíme se objednat víc kusů, než kolik zbývá (zbyly 3, chceme 4)
        print("\nZkoušíme vytvořit další příliš velkou objednávku...")
        bad_order = Order(order_id="ORD-2026-002", customer=vip_customer)
        bad_order.add_item(notebook, quantity=4)
        service.process_order(bad_order)

    except InsufficientStockError as e:
        print(f"CHYBA SKLADU: {e}")