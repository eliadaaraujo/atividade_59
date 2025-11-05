# Centímetros, milímetros e quilômetros.
# Mostre todos os resultados formatados.
# Exemplo: 1.5m → 150cm | 1500mm | 0.0015km.

metros = float(input("Digite um valor em metros: "))

cm = metros * 100
mm = metros * 1000
km = metros / 1000

print(f"{metros}m → {cm}cm | {mm}mm | {km}km")
