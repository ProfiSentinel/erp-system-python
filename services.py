from exceptions import InsufficientStockError
from models import PhysicalProduct, Order

class OrderService:
    def process_order(self, order: Order) -> float:
        for item in order.items:
            if isinstance(item.product, PhysicalProduct):
                if item.quantity > item.product._stock_quantity:
                    raise InsufficientStockError(
                        f"Not enough stock aviable for the physical product"
                    )
                item.product.reduce_stock(item.quantity)

        return order.calculate_grand_total()