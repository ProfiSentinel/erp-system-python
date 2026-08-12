from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name:str, base_price:float):
        self.name = name
        self._base_price = base_price

    @property
    def base_price(self):
        return self._base_price

    @base_price.setter
    def base_price(self, value):
        if value < 0:
            raise ValueError("Base price cannot be neegative.")
        self._base_price = value

    @abstractmethod
    def calculate_price(self) -> float:
        pass


class PhysicalProduct(Product):
    def __init__(self, name:str, base_price:float, stock_quantity:int, weight_kg:float, vat_rate: float = 0.21):
        super().__init__(name, base_price)
        self._stock_quantity = stock_quantity
        self.weight_kg = weight_kg
        self.vat_rate = vat_rate


    def calculate_price(self) -> float:
        return self.base_price * (1 + self.vat_rate)

    def reduce_stock(self, quantity: int):
        if quantity > self._stock_quantity:
            raise ValueError("Not enough stock available.")
        self._stock_quantity -= quantity


class ServiceItem(Product):
    def __init__(self, name:str, base_price:float, duration_hours:float, vat_rate: float = 0.21):
        super().__init__(name, base_price)
        self.duration_hours = duration_hours
        self.vat_rate = vat_rate
        

    def calculate_price(self) -> float:
        return self.base_price * self.duration_hours * (1 + self.vat_rate)


class Customer:
    def __init__(self, customer_id: str, name: str, discount_percentage: float = 0.0):
        self.customer_id = customer_id
        self.name = name
        self._discount_percentage = discount_percentage

    @property
    def discount_percentage(self):
        return self._discount_percentage 

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
        discount = total * (self.customer.discount_percentage / 100)
        return total - discount