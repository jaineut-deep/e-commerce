from src.product import Product


class Smartphone(Product):
    """Класс для представления смартфона."""

    __product_list: list["Smartphone"] = []

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Метод для инициализации экземпляра класса Smartphone. Задаем значения атрибутам экземпляра."""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

        self.__product_list.append(self)


class LawnGrass(Product):
    """Класс для представления смартфона."""

    __product_list: list["LawnGrass"] = []

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Метод для инициализации экземпляра класса Smartphone. Задаем значения атрибутам экземпляра."""

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

        self.__product_list.append(self)
