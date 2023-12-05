def triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "impossible"
    if a == b == c:
        return "équilateral"
    elif a == b or b == c or a == c:
        return "isocel"
    else:
        return "scalene"