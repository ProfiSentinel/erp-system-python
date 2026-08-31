from exceptions import InsufficientStockError
from models import PhysicalProduct, Order, DiscountStrategy

class OrderService():
    def process_order(self, order) -> float:

        final_price = order.calculate_grand_total()

        for item in order.items:
            product = item.product
            product.reduce_stock(item.quantity)

        return final_price