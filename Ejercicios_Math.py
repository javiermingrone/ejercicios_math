import math

"""

En la librería Math disponemos de varias funciones que nos permiten realizar funciones aritméticas, funciones trigonométricas, Funciones Hiperbólicas, Funciones logarítmicas y potencias. 
Revisemos algunas  funciones: 

floor(x) → Redondeo hacia abajo, devolverá el entero mayor menor o igual a x 
ceil(x) → Redondeo hacia arriba, devolverá el entero menor que sea mayor o igual que x.  
fabs(x)→ Valor absoluto, devolverá el valor absoluto de x.
Factorial(x)→ calcular el factorial de un número utilizando la función). Un factorial es el producto de un entero y de todos los enteros positivos más pequeños que él. 
            Se suele utilizar en combinaciones y permutaciones.

sin(x)→ Devuelve el Seno 
cos(x)→ Devuelve el Coseno 
tan(x)→ Devuelve la Tangente 
hypot(a,b)→ Devuelve la Hipotenusa  
Para las inversas tenemos asen(x), acos(x), atan(x)    

Sqrt(x)→ Calcular la raíz cuadrada  
Pow(x,y)→ numero de x elevado a la potencia de y.  
Log(x,10)→ logaritmo base 10  
Log(x,2)→ logaritmo base 2  

"""

# Usando la función ceil
param_ceiling = 1.001
resultado_ceil = math.ceil(param_ceiling)
print("Resultado de ceil(1.001):", resultado_ceil)

# Usando la función floor
param_floor = 1.001
resultado_floor = math.floor(param_floor)
print("Resultado de floor(1.001):", resultado_floor)

# Usando la función factorial
param_factorial = 10
resultado_factorial = math.factorial(param_factorial)
print("Resultado de factorial(10):", resultado_factorial)

# Usando la función gcd
param_gcd1 = 10
param_gcd2 = 125
resultado_gcd = math.gcd(param_gcd1, param_gcd2)
print("Resultado de gcd(10, 125):", resultado_gcd)

# Usando la función pow
param_pow1 = 12.5
param_pow2 = 2.8
resultado_pow1 = math.pow(param_pow1, param_pow2)
print("Resultado de pow(12.5, 2.8):", resultado_pow1)

param_pow3 = 144
param_pow4 = 0.5
resultado_pow2 = math.pow(param_pow3, param_pow4)
print("Resultado de pow(144, 0.5):", resultado_pow2)

# Usando la función sqrt
param_sqrt = 144
resultado_sqrt = math.sqrt(param_sqrt)
print("Resultado de sqrt(144):", resultado_sqrt)
