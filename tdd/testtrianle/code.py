def determine_triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Impossible"
    if a == b == c:
        return "Équilatéral"
    elif a == b or b == c or a == c:
        return "Isocèle"
    else:
        return "Scalène"