from src.subproducts import LawnGrass, Smartphone


def test_smartphone_init(get_smartphone_product: Smartphone) -> None:
    assert get_smartphone_product.name == "Okitel"
    assert get_smartphone_product.description == "Rough phone for travels"
    assert get_smartphone_product.price == 156.8
    assert get_smartphone_product.quantity == 81
    assert get_smartphone_product.efficiency == 85.2
    assert get_smartphone_product.model == "KT802"
    assert get_smartphone_product.memory == 128
    assert get_smartphone_product.color == "Gray/orange"


def test_grass_init(get_grass_product: LawnGrass) -> None:
    assert get_grass_product.name == "Буратино"
    assert get_grass_product.description == "Морозоустойчивая газонная трава"
    assert get_grass_product.price == 99.9
    assert get_grass_product.quantity == 183
    assert get_grass_product.country == "Россия"
    assert get_grass_product.germination_period == "6 дней"
    assert get_grass_product.color == "Изумрудный"
