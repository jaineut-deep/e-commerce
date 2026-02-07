from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный базовый класс для представления всех продуктов."""

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> "BaseProduct":
        """Абстрактный метод класса BaseProduct для добавления нового продукта в список продуктов."""

        pass
