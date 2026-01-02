from src.category import Category
from src.product import Product


def test_category_init(
    get_phone_cat: Category,
    get_game_mouse: Category,
    get_tecno: Product,
    get_ulefone: Product,
    get_vivo: Product,
    get_genius: Product,
    get_zelotes: Product,
) -> None:
    assert get_phone_cat.name == "Smartphones"
    assert get_phone_cat.description == "Modern devices for connection, messages and internet serfing"
    assert get_phone_cat.products == [get_tecno, get_ulefone, get_vivo]

    assert get_game_mouse.name == "Game Mouse"
    assert get_game_mouse.description == "Ergonomics game mice with high performance and optical sensor"
    assert get_game_mouse.products == [get_genius, get_zelotes]

    assert Category.product_count == 5
    assert Category.category_count == 2
