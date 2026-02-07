from pytest import CaptureFixture

from src.product import Product


def test_print_product(get_expensive_mouse: Product, capsys: CaptureFixture[str]) -> None:
    product_one = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    captured = capsys.readouterr()
    assert captured.out == "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)\n"
    assert product_one.name == "Samsung Galaxy S23 Ultra"
