import sympy as sp
from Metodos.Utils.Error_Relativo import Error_Relativo
class metodo_puntoFijo:

    def metodo_puntoFijo(self):
        instance_ER = Error_Relativo()
        xi_Inicial, yi_Inicial= 0,0
        xi, yi  = 0, 0
        # Definir las variables simbólicas
        x, y = sp.symbols('x y')
        conta = 0

        # Crear ecuaciones
        equation_x = x**2 + x*y - 10  # ecuación de x
        equation_y = y + 3*x*y**2 - 57  # ecuación de y
        print(equation_x)
        print(equation_y)
        Flag ,valor,valor2= True, False, False


        while(Flag):
         print("Iteracion: {}".format(conta))
         print(" ")
         eval_equation_x = equation_x.subs({x: xi, y: yi}).evalf()  # Evaluar equation_x
         eval_equation_y = equation_y.subs({x: xi, y: yi}).evalf()  # Evaluar equation_y
         eval_equation_x = round(eval_equation_x,4)
         eval_equation_y = round(eval_equation_y,4)
         if eval_equation_x == 0 and eval_equation_y == 0:
            print("LA FUNCION DA 0 EN X:{} Y:{}".format(xi,yi))
            Flag = False 
         else:
        
        # Despejar x y y
          despeje_x = sp.solve(equation_x, x**2)
          despeje_y = sp.solve(equation_y, y**2)
          despeje_x = [sp.sqrt(sol) for sol in despeje_x]  # Raíz cuadrada de las soluciones de x
          despeje_y = [sp.sqrt(sol) for sol in despeje_y]  # Raíz cuadrada de las soluciones de y
          print("Despeje x: {} y: {}".format(despeje_x,despeje_y))
         
 
        # Evaluar en xi, yi
        # Usar la primera solución para x y y
          xi= despeje_x[0].subs({x: xi, y: yi})
          xi = round(xi,4)
          yi = despeje_y[0].subs({x: xi, y: yi})
          yi = round(yi,4)
          print("Evaluación final: xi = {:.4f}, yi = {:.4f}".format(xi, yi))

          conta+=1
          xError = instance_ER.Error_Relativo(xi,xi_Inicial)
          yError = instance_ER.Error_Relativo(yi,yi_Inicial)
        
          print("ERROR RELATIVO: xi = {:.4f}, yi = {:.4f}".format(xError,yError ))
          
          if xError < 0.0005 and valor == False:
             xiFinal = xi
             valor = True
          if yError < 0.0005 and valor2==False:
             yiFinal = yi
             valor2 = True
          if valor == True and valor2 ==True:
             print("Valores Finales: {}, {}".format(xiFinal,yiFinal))
             Flag = False 

          
          xi_Inicial =  xi
          yi_Inicial = yi
         
             
        


        return None
        



