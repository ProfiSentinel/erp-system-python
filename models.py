from abc import ABC, abstractmethod
from exceptions import InsufficientStockError

# _____ SLEVY _____

class DiscountStrategy(ABC):
    """Abstraktní předek pro všechny typy slev"""

    @abstractmethod
    def calculate(self, total_price: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    """Žádná sleva"""

    def calculate(self, total_price: float) -> float:
        return total_price


class PercentageDiscount(DiscountStrategy):
    """Procentuální sleva"""

    def __init__(self, percentage: float):
        self.percentage = percentage

    def calculate(self, total_price: float) -> float:
        discount_amount = total_price * (self.percentage / 100)
        return max(0.0, total_price - discount_amount)


class FixedDiscount(DiscountStrategy):
    """Fixní částka slevová"""

    def __init__(self, amount: float):
        self.amount = amount

    def calculate(self, total_price: float) -> float:
        return max(0.0, total_price - self.amount)


# _____ PRODUKTY _____

class Product(ABC):
    """Předek pro produkty"""

    def __init__(self, name: str, base_price: float):
        self.name = name
        self._base_price = base_price

    @property
    def base_price(self) -> float:
        return self._base_price

    @base_price.setter
    def base_price(self, value: float):
        if value < 0:
            raise ValueError("Base price cannot be negative.")
        self._base_price = value

    @abstractmethod
    def calculate_price(self) -> float:
        pass


class PhysicalProduct(Product):
    def __init__(self, name: str, base_price: float, stock_quantity: int, weight_kg: float, vat_rate: float = 0.21):
        super().__init__(name, base_price)
        self._stock_quantity = stock_quantity
        self.weight_kg = weight_kg
        self.vat_rate = vat_rate

    @property
    def stock_quantity(self) -> int:
        """Getter pro získání aktuálního stavu skladu"""
        return self._stock_quantity

    def calculate_price(self) -> float:
        return self.base_price * (1 + self.vat_rate)

    def reduce_stock(self, quantity: int):
        if quantity > self._stock_quantity:
            raise InsufficientStockError("Not enough stock available.")
        self._stock_quantity -= quantity


class ServiceItem(Product):
    def __init__(self, name: str, base_price: float, duration_hours: float, vat_rate: float = 0.21):
        super().__init__(name, base_price)
        self.duration_hours = duration_hours
        self.vat_rate = vat_rate

    def calculate_price(self) -> float:
        return self.base_price * self.duration_hours * (1 + self.vat_rate)


# _____ ZÁKAZNÍCI A OBJEDNÁVKY _____

class Customer:
    def __init__(self, customer_id: str, name: str, discount_strategy: DiscountStrategy = None):
        self.customer_id = customer_id
        self.name = name

        if isinstance(discount_strategy, (int, float)):
            self.discount_strategy = PercentageDiscount(float(discount_strategy))
        else:
<<<<<<< HEAD
            self.discount_strategy = discount_strategy or NoDiscount()
=======
            # Oprava: Vytváříme instanci NoDiscount(), nikoli třídu
            self.discount_strategy = discount_strategy or NoDiscount()

>>>>>>> b553233 (Refactor: Add gitignore, update README and fix order service logic)

class VIPCustomer(Customer):
    def __init__(self, customer_id: str, name: str):
        super().__init__(customer_id, name, discount_strategy=PercentageDiscount(10.0))


class OrderItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def get_total_price(self) -> float:
        return self.product.calculate_price() * self.quantity


class Order:
    def __init__(self, order_id: str, customer: Customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []

    def add_item(self, product: Product, quantity: int = 1):
        self.items.append(OrderItem(product, quantity))

    def calculate_grand_total(self) -> float:
        total = sum(item.get_total_price() for item in self.items)
        return self.customer.discount_strategy.calculate(total)
