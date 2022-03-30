a, b, c = [float(x) for x in input().split()]

if a + b > c and a + c > b and b + c > a:
    perimetro = a + b + c
    # TODO Preencha a formula do perímeto do triangulo (soma de todos os lados).
    print(f"Perimetro = {perímeto:.1f}")
else:
    area = (((a + b) * c) / 2)
    # TODO Preencha a formula da área do trapézio: AREA = ((A + B) x C) / 2
    print(f"Area = {area:.1f}")
