import pytest

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
    get_expensive_mouse: Product,
) -> None:
    assert get_phone_cat.name == "Smartphones"
    assert get_phone_cat.description == "Modern devices for connection, messages and internet serfing"
    assert get_phone_cat.products == (
        "Tecno 15, 1569.0 руб. Остаток: 23 шт.\n"
        "Ulefone 13T, 1849.0 руб. Остаток: 150 шт.\n"
        "Vivo iQ Z9, 2441.0 руб. Остаток: 34 шт.\n"
    )

    assert get_game_mouse.name == "Game Mouse"
    assert get_game_mouse.description == "Ergonomics game mice with high performance and optical sensor"
    assert get_game_mouse.products == (
        "Genius U75, 25.0 руб. Остаток: 180 шт.\n" "Zelotes T50, 35.0 руб. Остаток: 101 шт.\n"
    )
    get_game_mouse.add_product(get_expensive_mouse)
    assert get_game_mouse.products == (
        "Genius U75, 25.0 руб. Остаток: 180 шт.\n"
        "Zelotes T50, 35.0 руб. Остаток: 101 шт.\n"
        "Attack Shark R5 Ultra, 45.7 руб. Остаток: 57 шт.\n"
    )
    assert Category.product_count == 6
    assert Category.category_count == 2


def test_category_products_list(
    get_phone_cat: Category,
    get_game_mouse: Category,
    get_tecno: Product,
    get_ulefone: Product,
    get_vivo: Product,
    get_genius: Product,
    get_zelotes: Product,
) -> None:
    assert get_phone_cat.category_products == [get_tecno, get_ulefone, get_vivo]
    assert get_game_mouse.category_products == [get_genius, get_zelotes]


def test_category_string(get_phone_cat: Category, get_game_mouse: Category) -> None:
    assert str(get_phone_cat) == "Smartphones, количество продуктов: 207 шт."
    assert str(get_game_mouse) == "Game Mouse, количество продуктов: 281 шт."


def test_adding_not_product(get_game_mouse: Category) -> None:
    with pytest.raises(TypeError):
        get_game_mouse.add_product("Not a product")  # type: ignore[arg-type]
