from src.product import Product


class Category:
    """Класс для представления категорий продукта"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: list

    def __init__(self, name: str, description: str, products: list) -> None:
        """Метод для инициализации экземпляра класса Category. Задаем значения атрибутам экземпляра"""

        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """
        Магический метод, возвращающий строковое отображение объекта класса Category с общим количеством
        продуктов этого объекта.
        """

        products_count = 0
        for product in self.__products:
            products_count += product.quantity
        return f"{self.name}, количество продуктов: {products_count} шт."

    def add_product(self, product: Product) -> None:
        """
        Метод принимает на вход аргументы self и продукт для добавления.
        Не возвращает никакого значения
        """

        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        """Геттер возвращает строку со всеми продуктами в приватном атрибуте products."""

        product_str = ""
        for prod in self.__products:
            product_str += f"{str(prod)}\n"
        return product_str

    @property
    def category_products(self) -> list["Product"]:
        """Геттер возвращает список объектов класса Product из класса Category."""

        return self.__products

    def middle_price(self) -> float:
        """
        Метод, возвращающий средний ценник за продукт из списка продуктов класса Category. Если список продуктов
        пустой - возвращается ноль.
        """

        try:
            mid_price = sum([prod.price for prod in self.category_products]) / len(self.category_products)
        except ZeroDivisionError:
            return 0.0
        else:
            return round(mid_price, 1)
