import pytest

from src.helpers import GoodsIter


def test_iteration_phones(get_phone_iterator: GoodsIter) -> None:
    iter(get_phone_iterator)
    assert get_phone_iterator.index_count == 0
    assert next(get_phone_iterator).name == "Tecno 15"
    assert next(get_phone_iterator).name == "Ulefone 13T"
    assert next(get_phone_iterator).name == "Vivo iQ Z9"
    with pytest.raises(StopIteration) as exc_info:
        next(get_phone_iterator)
    assert str(exc_info.value) == ""


def test_iteration_mice(get_mouse_iterator: GoodsIter) -> None:
    iter(get_mouse_iterator)
    assert get_mouse_iterator.index_count == 0
    assert next(get_mouse_iterator).name == "Genius U75"
    assert next(get_mouse_iterator).name == "Zelotes T50"
    with pytest.raises(StopIteration) as exc_info:
        next(get_mouse_iterator)
    assert str(exc_info.value) == ""
