def test_determine_triangle_type():
    # Test pour un triangle équilatéral
    assert determine_triangle_type(3, 3, 3) == "Équilatéral"
    assert determine_triangle_type(6, 6, 6) == "Équilatéral"

    # Test pour un triangle isocèle
    assert determine_triangle_type(3, 3, 4) == "Isocèle"
    assert determine_triangle_type(5, 7, 5) == "Isocèle"

    # Test pour un triangle scalène
    assert determine_triangle_type(3, 4, 5) == "Scalène"
    assert determine_triangle_type(7, 8, 9) == "Scalène"

    # Test pour un triangle impossible
    assert determine_triangle_type(1, 1, 3) == "Impossible"
    assert determine_triangle_type(0, 0, 0) == "Impossible"