from src.product import Product


def test_get_tecno(get_tecno: Product) -> None:
    assert get_tecno.name == "Tecno 15"
    assert get_tecno.description == "Budget variant with performance"
    assert get_tecno.price == 1569.0
    assert get_tecno.quantity == 23


def test_get_ulefone(get_ulefone: Product) -> None:
    assert get_ulefone.name == "Ulefone 13T"
    assert get_ulefone.description == "Bright led flashlight"
    assert get_ulefone.price == 1849.0
    assert get_ulefone.quantity == 150


def test_get_vivo(get_vivo: Product) -> None:
    assert get_vivo.name == "Vivo iQ Z9"
    assert get_vivo.description == "Capacity 6800mAh and faceID"
    assert get_vivo.price == 2441.0
    assert get_vivo.quantity == 34


def test_get_genius(get_genius: Product) -> None:
    assert get_genius.name == "Genius U75"
    assert get_genius.description == "Nice ergonomics"
    assert get_genius.price == 25.0
    assert get_genius.quantity == 180


def test_get_zelotes(get_zelotes: Product) -> None:
    assert get_zelotes.name == "Zelotes T50"
    assert get_zelotes.description == "Vertical mouse"
    assert get_zelotes.price == 35.0
    assert get_zelotes.quantity == 101
