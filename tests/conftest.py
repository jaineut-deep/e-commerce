import pytest

from src.category import Category
from src.helpers import GoodsIter
from src.product import Product
from src.subproducts import LawnGrass, Smartphone


@pytest.fixture
def get_tecno() -> Product:
    return Product(name="Tecno 15", description="Budget variant with performance", price=1569.0, quantity=23)


@pytest.fixture
def get_ulefone() -> Product:
    return Product(name="Ulefone 13T", description="Bright led flashlight", price=1849.0, quantity=150)


@pytest.fixture
def get_vivo() -> Product:
    return Product(name="Vivo iQ Z9", description="Capacity 6800mAh and faceID", price=2441.0, quantity=34)


@pytest.fixture
def get_genius() -> Product:
    return Product(name="Genius U75", description="Nice ergonomics", price=25.0, quantity=180)


@pytest.fixture
def get_zelotes() -> Product:
    return Product(name="Zelotes T50", description="Vertical mouse", price=35.0, quantity=101)


@pytest.fixture
def get_expensive_mouse() -> Product:
    return Product(
        name="Attack Shark R5 Ultra", description="Hybrid-connecting ergonomic mouse", price=45.7, quantity=57
    )


@pytest.fixture
def get_phone_cat(get_tecno: Product, get_ulefone: Product, get_vivo: Product) -> Category:
    return Category(
        name="Smartphones",
        description="Modern devices for connection, messages and internet serfing",
        products=[get_tecno, get_ulefone, get_vivo],
    )


@pytest.fixture
def get_game_mouse(get_genius: Product, get_zelotes: Product) -> Category:
    return Category(
        name="Game Mouse",
        description="Ergonomics game mice with high performance and optical sensor",
        products=[get_genius, get_zelotes],
    )


@pytest.fixture
def get_phone_iterator(get_phone_cat: Category) -> GoodsIter:
    return GoodsIter(get_phone_cat)


@pytest.fixture
def get_mouse_iterator(get_game_mouse: Category) -> GoodsIter:
    return GoodsIter(get_game_mouse)


@pytest.fixture
def get_smartphone_product() -> Smartphone:
    return Smartphone("Okitel", "Rough phone for travels", 156.8, 81, 85.2, "KT802", 128, "Gray/orange")


@pytest.fixture
def get_grass_product() -> LawnGrass:
    return LawnGrass("Буратино", "Морозоустойчивая газонная трава", 99.9, 183, "Россия", "6 дней", "Изумрудный")
