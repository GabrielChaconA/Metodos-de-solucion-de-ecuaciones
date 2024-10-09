import sympy as sp

# Clase para el cálculo del error relativo
class Error_Relativo:
    def Error_Relativo(self, x1, x2):
        if x1 == 0:  # Evitar división por cero
            return abs(x2)  # Devolvemos el valor absoluto de x2 como error si x1 es 0
        else:
            return abs(((x1 - x2) / x1) * 100)  # Cálculo del error relativo estándar

# Clase para implementar el método de Newton-Raphson
class newton:
    def newton(self):
        # Definir las variables simbólicas
        x, y, z = sp.symbols('x y z')

        # Puntos iniciales más cercanos a los valores esperados
        punto = {x: 0.5, y: 0.02, z: -0.5}
        puntos = sp.Matrix([[0.5], [0.02], [-0.5]])
        contador = 0
        valor1, valor2, valor3 = False, False, False
        Flag = True

        # Crear la matriz 3x1 con las ecuaciones dadas (adaptadas de la imagen)
        matriz = sp.Matrix([
            [3*x - sp.cos(y*z) - 0.5],  # Primera ecuación (adaptada con valor independiente 0.5)
            [x**2 - 625*y**2],          # Segunda ecuación (sin valor independiente, igual a 0)
            [sp.exp(-x*y) + 20*z - 9.472]  # Tercera ecuación (adaptada con valor independiente -9.472)
        ])

        # Derivar cada término de la matriz con respecto a x, y y z
        matriz_derivada_x = matriz.jacobian([x, y, z])

        # Instancia para calcular el error relativo
        instance_errorRelativo = Error_Relativo()

        while Flag:
            print(f"\nIteración {contador}\n")
            
            # Evaluar la matriz y las derivadas en el punto actual
            matriz_evaluada = matriz.subs(punto)
            matriz_derivada_evaluada = matriz_derivada_x.subs(punto)
            
            # Redondear resultados
            matriz_evaluada = matriz_evaluada.applyfunc(lambda elem: round(elem, 4))
            matriz_derivada_evaluada = matriz_derivada_evaluada.applyfunc(lambda elem: round(elem, 4))
            
            print(f"Matriz derivada evaluada: \n{matriz_derivada_evaluada}")
            print(f"Matriz simbólica evaluada: \n{matriz_evaluada}")

            # Matriz 3x1 con constantes del sistema (igualada a 0)
            matriz_3x1 = -matriz_evaluada

            # Resolver el sistema con LUsolve
            soluciones = matriz_derivada_evaluada.LUsolve(matriz_3x1)
            soluciones = soluciones.applyfunc(lambda elem: round(elem, 4))

            print(f"h1: {soluciones[0]}, h2: {soluciones[1]}, h3: {soluciones[2]}")

            # Actualizar los valores de los puntos
            h_previa = soluciones
            puntos = soluciones + puntos

            print(f"X' = {puntos[0,0]}, Y' = {puntos[1,0]}, Z' = {puntos[2,0]}")

            # Actualizar el diccionario para los siguientes valores
            punto = {x: puntos[0,0], y: puntos[1,0], z: puntos[2,0]}

            # Cálculo del error relativo
            v1 = instance_errorRelativo.Error_Relativo(h_previa[0, 0], puntos[0, 0])
            v2 = instance_errorRelativo.Error_Relativo(h_previa[1, 0], puntos[1, 0])
            v3 = instance_errorRelativo.Error_Relativo(h_previa[2, 0], puntos[2, 0])

            print(f"Error relativo: v1 = {v1:.4f}, v2 = {v2:.4f}, v3 = {v3:.4f}")

            # Verificación de condiciones de paro
            if (v1 < 0.005 or v1 == 0) and not valor1:
                valor1 = True
                valor_correcto = puntos[0, 0]
                print(f"\nValor de X encontrado: {valor_correcto} en iteración {contador}")
            if (v2 < 0.005 or v2 == 0) and not valor2:
                valor2 = True
                valor_correcto2 = puntos[1, 0]
                print(f"\nValor de Y encontrado: {valor_correcto2} en iteración {contador}")
            if (v3 < 0.005 or v3 == 0) and not valor3:
                valor3 = True
                valor_correcto3 = puntos[2, 0]
                print(f"\nValor de Z encontrado: {valor_correcto3} en iteración {contador}")

            # Si se encuentran los tres valores correctos, salir del ciclo
            if valor1 and valor2 and valor3:
                print(f"Valores finales: X = {valor_correcto}, Y = {valor_correcto2}, Z = {valor_correcto3}")
                Flag = False

            contador += 1

        return None


