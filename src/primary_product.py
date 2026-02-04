from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для представления всех продуктов."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """Абстрактный метод класса BaseProduct для добавления нового продукта в список продуктов."""

        pass
