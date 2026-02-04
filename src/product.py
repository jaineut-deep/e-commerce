from typing import Any

from src.primary_product import BaseProduct


class Product(BaseProduct):
    """Класс для представления продукта"""

    name: str
    description: str
    __price: float
    quantity: int
    __product_list: list["Product"] = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        self.__product_list.append(self)

    def __str__(self) -> str:
        """Магический метод, возвращающий строковое отображение объекта класса Product."""

        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        """Магический метод, возвращающий сумму произведений цены на количество у двух объектов."""

        if isinstance(self, type(other)):
            result_expense = (self.price * self.quantity) + (other.price * other.quantity)
            return result_expense
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product: dict[str, Any]) -> "Product":
        """Класс-метод принимает на вход два аргумента — cls и продукт для создания в виде словаря —
        и возвращает экземпляр класса Product на основе данных словаря.
        """

        for prod in cls.__product_list:
            if prod.name == product["name"]:
                prod.price = max(prod.price, product.get("price", 0.0))
                prod.quantity += product["quantity"]
                return prod
        return cls(**product)

    @property
    def price(self) -> float:
        """Геттер возвращает значение приватного атрибута цены."""

        return self.__price

    @price.setter
    def price(self, user_price: int | float) -> None:
        """Сеттер принимает два аргумента — self и новое значение цены.
        В сеттере реализована проверка на положительное значение новой цены.
        Сеттер ничего не возвращает.
        """

        if isinstance(user_price, float | int):
            if user_price <= 0:
                print("Цена не должна быть нулевая или отрицательная")
            elif float(user_price) >= self.__price:
                self.__price = float(user_price)
            else:
                if input("Понизить цену?(y/<any_key>): ") == "y":
                    self.__price = float(user_price)
