from exceptions import InsufficientStockError
from models import PhysicalProduct, Order

<<<<<<< HEAD
class OrderService:
    def process_order(self, order) -> float:

        final_price = order.calculate_grand_total()
=======
>>>>>>> b553233 (Refactor: Add gitignore, update README and fix order service logic)

class OrderService:
    def process_order(self, order: Order) -> float:
        # 1. FÁZE: Ověření dostupnosti na skladě pro všechny fyzické produkty
        for item in order.items:
            product = item.product
            if isinstance(product, PhysicalProduct):
                if item.quantity > product.stock_quantity:
                    raise InsufficientStockError(
                        f"Nedostatek zásob pro produkt: {product.name}"
                    )

<<<<<<< HEAD
        return final_price
=======
        # 2. FÁZE: Pokud kontroly prošly, odečteme zboží ze skladu
        for item in order.items:
            product = item.product
            if isinstance(product, PhysicalProduct):
                product.reduce_stock(item.quantity)

        # 3. FÁZE: Výpočet a vrácení finální ceny
        return order.calculate_grand_total()
>>>>>>> b553233 (Refactor: Add gitignore, update README and fix order service logic)
