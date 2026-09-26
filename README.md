# Python ERP Core Module

A modular, object-oriented backend core for an Enterprise Resource Planning (ERP) order management system built in Python. 

This project demonstrates clean code principles, domain modeling, design patterns, and unit testing using `pytest`.

---

## Key Features & Concepts

- **Object-Oriented Design (OOP):** Applied abstraction, inheritance, encapsulation (`@property`), and polymorphism across products and customer entities.
- **Design Patterns:** Implemented the **Strategy Pattern** (`DiscountStrategy`) to allow dynamic calculation of customer-specific discounts (`PercentageDiscount`, `FixedDiscount`, `NoDiscount`).
- **Transactional Service Layer:** `OrderService` handles order processing with two-phase stock verification to ensure data consistency and prevent race conditions.
- **Robust Error Handling:** Custom exceptions (`InsufficientStockError`) to manage edge cases and out-of-stock scenarios gracefully.
- **Automated Unit Testing:** Comprehensive test coverage via `pytest` covering happy paths, edge cases, and exception handling.

---

## Project Structure

```text
ERP_project/
├── models.py         # Domain models (Product, Customer, Order, DiscountStrategy)
├── services.py       # Application service layer (OrderService)
├── exceptions.py     # Custom domain exceptions
├── main.py           # Application entry point / usage example
└── tests/
    └── test_shop.py  # Automated unit tests using pytest