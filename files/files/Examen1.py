# EXAMEN N 1, CRIPTOGRAFIA Y SEGURIDAD INFORMATICA, MIGUEL GUILLEN 
# Cedula: 29877776
# n = 76
# m = 77
# a = 87

# Primera Pregunta: Determina todos los enteros x tales que:

# x ≡ 87 (mod 77)
# partiendo del concepto de congruencia en aritmetica modular, la congruencia de esta ecuacion significa que x y 87 dejan el mismo residuo al dividir entre 77, es decir que x--87 es divisible por 77, por lo tanto x -87 = 77Z, donde Z es un entero, despejando x nos queda la siguiente formula X = 77Z + 87
valores_Z = range(0, 15)  
print("-------RESULTADOS PRIMERA PREGUNTA--------")
for Z in valores_Z:
    x = 77 * Z + 87
    print(f'Para Z = {Z}, x = {x}')
print("partiendo del concepto de congruencia en aritmetica modular, la congruencia de esta ecuacion significa que x y 87 dejan el mismo residuo al dividir entre 77, es decir que x--87 es divisible por 77, por lo tanto x -87 = 77Z, donde Z es un entero, despejando x nos queda la siguiente formula X = 77Z + 87")
# Segunda Pregunta: Encuentra todas las soluciones de la congruencia lineal
# 3x ≡ 5 (mod 87)
print("-----------------RESULTADOS SEGUNDA PREGUNTA-----------------")

# Buscar el inverso de 3 modulo 87
a = 3
m = 87
inverso = None

# Probar valores de y desde 1 hasta m-1
for y in range(1, m):
    if (a * y) % m == 1:
        inverso = y
        break

if inverso is not None:
    print(f'El inverso de 3 modulo 87 es {inverso}')
else:
    print('No se encontró un inverso multiplicativo, ya que l buscar el inverso multiplicativo de 3 modulo 87, se puede observar que no existe solucion \n, debido a que necesitamos tambien el MCD de 3 y 87 divida a 5, como el MCD de 3 y 87 es 3, no divide a 5, por lo tanto no existe solucion alguna')

# al buscar el inverso multiplicativo de 3 modulo 87, se puede observar que no existe solucion, debido a que necesitamos tambien el MCD de 3 y 87 divida a 5, como el MCD de 3 y 87 es 3, no divide a 5, por lo tanto no existe solucion alguna

# 3) Calcula los restos de
# a) (87 + 1)(77+1) mod 76
# b) (76 + 10)(87+10) mod 77
# c) (77 + 10)(87+5) mod 76
# d) (76 + 3)(77+2) mod 87
print("-----------------RESULTADOS TERCERA PREGUNTA-----------------")

# tan sencillo como definir una funcion que me calcule el modulo de la operacion, definiendo cada parametro para que a, sea el valor, b sea el exponente y mod sea el modulo
def calc_mod(a, b, mod):
    return (a**b) % mod

# a) (87 + 1)^(77 + 1) mod 76
result_a = calc_mod(87 + 1, 77 + 1, 76)

# b) (76 + 10)^(87 + 10) mod 77
result_b = calc_mod(76 + 10, 87 + 10, 77)

# c) (77 + 10)^(87 + 5) mod 76
result_c = calc_mod(77 + 10, 87 + 5, 76)

# d) (76 + 3)^(77 + 2) mod 87
result_d = calc_mod(76 + 3, 77 + 2, 87)

print(f"Resultado a: {result_a}")
print(f"Resultado b: {result_b}")
print(f"Resultado c: {result_c}")
print(f"Resultado d: {result_d}")


# 4. Resolver
print("-----------------RESULTADOS CUARTA PREGUNTA-----------------")

# a) Calcula el inverso multiplicativo de (n + 1) m ́odulo 131, si existe.
print("-----------------RESULTADOS A-----------------")
# Utilizando la misma forma anteriormente para encontrar si existe un inverso multiplicativo podremos encontrar el inverso multiplicativo de (76 + 1) modulo 131, donde encontraremos que existe solucion para este caso
for y in range(1, 131):
    if (77 * y) % 131 == 1:
        inverso = y
        break

if inverso is not None:
    print(f'El inverso de 77 modulo 131 es {inverso}')
else:
    print('No se encontró un inverso multiplicativo')

# b) Determina si el numero 2n + 3m es congruente con 3 modulo a.
print("-----------------RESULTADOS B-----------------")

# verificamos si 2n + 3m es congruente con 3 modulo 87
def is_congruent(a, b, mod):
    return (a % mod) == (b % mod)

# Valores dados
a = (2 * 76) + (3 * 77)
b = 3
mod = 87

# Verificar si son congruentes
congruence = is_congruent(a, b, mod)

if congruence:
    print(f"{a} es congruente con {b} módulo {mod}.")
else:
    print(f"{a} no es congruente con {b} módulo {mod}.")

# encuentra el numero con el que es congruente
def find_congruence(a, mod):
    return a % mod

# Encontrar el resultado de la congruencia
congruence_result = find_congruence(a, mod)

print(f"{a} es congruente con {congruence_result} módulo {mod}.")

# 5) Aplica congruencias para responder los siguientes planteamientos:
print("-----------------RESULTADOS QUINTA PREGUNTA-----------------")
# a) Supongamos que estamos en noviembre, ¿qu ́e mes ser ́a en 1000 meses?
# Para resolver este problema, se puede hacer uso de la aritmetica modular definiendo 1000 mod 12, donde 12 es el numero de meses en un año
print("-----------------RESULTADOS A-----------------")
meses = 1000 % 12
print(f"En 1000 meses estaremos en el mes {meses}(marzo)")
# b) Si hoy es domingo ¿que dıa ser ́a en 15 dıas? ¿y en 26 dıas? ¿y en 234 dıas? ¿y en
# 1000 dıas?
# si comenzamos en domingo, y queremos saber que dia es dentro de 15 dias, podemos definir 15 mod 7, donde 7 es el numero de dias en una semana, comenzando como 1 = lunes, 2 = martes, 3 = miercoles, 4 = jueves, 5 = viernes, 6 = sabado, 7 = domingo
print("-----------------RESULTADOS B-----------------")
dia_15 = 15 % 7
print(f"En 15 dias sera el dia {dia_15}(lunes)")
dia_26 = 26 % 7
print(f"En 26 dias sera el dia {dia_26}(viernes)")
dia_234 = 234 % 7
print(f"En 234 dias sera el dia {dia_234}(miercoles)")
dia_1000 = 1000 % 7
print(f"En 1000 dias sera el dia {dia_1000}(sabado)")
# c) Si en este momento son las 9am, ¿qu ́e hora ser ́a dentro de 50 horas?
print("-----------------RESULTADOS C-----------------")
# si queremos saber que hora es dentro de 50 horas, podemos definir 50 mod 24, donde 24 es el numero de horas en un dia y donde 9 es la hora actual, por lo tanto sera dos horas despues de la 9am
hora = 50 % 24
print(f"Dentro de 50 horas seran las {hora+9}am")