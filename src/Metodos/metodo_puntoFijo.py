import sympy as sp
import numpy as np
from Metodos.Utils.Error_Relativo import Error_Relativo

class metodo_puntoFijo:
    def metodo_puntoFijo(self):
        instance_ER = Error_Relativo()
        
        # Valores iniciales de xi, yi, zi
        xi_Inicial, yi_Inicial, zi_Inicial = 0.1, 0.1, 0.1  # Evitar ceros directos
        xi, yi, zi = xi_Inicial, yi_Inicial, zi_Inicial
        
        # Definir las variables simbólicas
        x, y, z = sp.symbols('x y z')
        conta = 0

        # Crear la matriz 3x3
        matriz = sp.Matrix([
            [0, 3*x, -sp.cos(y*z)],
            [0, x**2, -625*y**2],
            [sp.exp(-x*y), 20*z, (10*sp.pi - 3) / 3]
        ])

        Flag, valor_x, valor_y, valor_z = True, False, False, False

        while Flag:
            print(f"Iteración: {conta}")
            print(" ")

            # Evaluar la matriz en los valores actuales de xi, yi, zi
            eval_matriz = matriz.subs({x: xi, y: yi, z: zi}).evalf()

            # Redondear los resultados
            eval_matriz = eval_matriz.applyfunc(lambda elem: round(elem, 4) if elem not in {sp.nan, sp.oo, -sp.oo} else float('nan'))

            print(f"Matriz evaluada en X: {xi}, Y: {yi}, Z: {zi}:\n{eval_matriz}")
            
            # Verificar si la matriz evaluada contiene algún valor indefinido (nan)
            if eval_matriz.norm() == 0 or any([elem.has(sp.nan) for elem in eval_matriz]):
                print(f"La función no converge correctamente en X: {xi}, Y: {yi}, Z: {zi} (posible división por cero o valor indefinido).")
                Flag = False
            else:
                try:
                    # Despejar las variables x, y, z
                    despeje_x = sp.solve(3*x - sp.cos(y*z), x)
                    despeje_y = sp.solve(x**2 - 625*y**2, y)
                    despeje_z = sp.solve(sp.exp(-x*y) + 20*z - (10*sp.pi - 3) / 3, z)

                    print(f"Despeje X: {despeje_x}, Y: {despeje_y}, Z: {despeje_z}")

                    # Verificar si hay soluciones para las variables
                    if despeje_x and despeje_y and despeje_z:
                        # Usar la primera solución (si existe) para actualizar xi, yi, zi
                        xi = float(despeje_x[0].subs({x: xi, y: yi, z: zi}).evalf())
                        yi = float(despeje_y[0].subs({x: xi, y: yi, z: zi}).evalf())
                        zi = float(despeje_z[0].subs({x: xi, y: yi, z: zi}).evalf())

                        xi, yi, zi = round(xi, 4), round(yi, 4), round(zi, 4)

                    else:
                        raise ValueError("No se encontraron soluciones válidas para las ecuaciones.")

                except (ZeroDivisionError, ValueError, TypeError) as e:
                    print(f"Error al intentar despejar o evaluar: {e}")
                    Flag = False
                    continue

                print(f"Evaluación final: xi = {xi}, yi = {yi}, zi = {zi}")

                conta += 1

                # Calcular errores relativos
                xError = instance_ER.Error_Relativo(xi, xi_Inicial)
                yError = instance_ER.Error_Relativo(yi, yi_Inicial)
                zError = instance_ER.Error_Relativo(zi, zi_Inicial)

                print(f"Error relativo: xi = {xError:.4f}, yi = {yError:.4f}, zi = {zError:.4f}")

                # Verificar si los errores relativos están dentro del umbral deseado
                if xError < 0.005 and not valor_x:
                    xiFinal = xi
                    valor_x = True
                if yError < 0.005 and not valor_y:
                    yiFinal = yi
                    valor_y = True
                if zError < 0.005 and not valor_z:
                    ziFinal = zi
                    valor_z = True

                if valor_x and valor_y and valor_z:
                    print(f"Valores finales: X = {xiFinal}, Y = {yiFinal}, Z = {ziFinal}")
                    Flag = False

                # Actualizar los valores iniciales para la siguiente iteración
                xi_Inicial, yi_Inicial, zi_Inicial = xi, yi, zi

        return None


