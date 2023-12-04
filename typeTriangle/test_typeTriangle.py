# test la fonction avec pypest
import pytest

from liris23.typeTriangle.typeTriangle import triangle_type


def test_triangle_type():
    # test pour un triangle équilateral
    assert triangle_type(4, 4, 4) == "équilateral"
    assert triangle_type(8, 8, 8) == "équilateral"

    # test pour un triangle isocel
    assert triangle_type(4, 4, 6) == "isocel"
    assert triangle_type(4, 7, 4) == "isocel"

    # test pour un triangle scalene
    assert triangle_type(5, 7, 8) == "scalene"
    assert triangle_type(8, 9, 13) == "scalene"

    # test pour les traingle  impossible
    assert triangle_type(0, 0, 0) == "impossible"
    assert triangle_type(1, 1, 9) == "impossible"


if __name__ == '__name__':
    pytest.main()
