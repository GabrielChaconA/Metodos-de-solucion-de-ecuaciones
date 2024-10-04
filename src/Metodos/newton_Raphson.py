import numpy as np
import sympy as sp
from Metodos.Utils.Error_Relativo import Error_Relativo
class newton:
   def newton(self):
        
    # Definir la variable simbólica x
     x = sp.Symbol('x')
     y = sp.Symbol('y')
     z = sp.Symbol('z')
     Flag = True
     punto = {x: 1, y: 2, z: 3}
     puntos = sp.Matrix([[1],[2],[3]])
     contador = 0
     valor1 , valor2 , valo3 = False, False, False

# Crear la matriz 3x3 con valores x^3
     matriz = sp.Matrix([[x**3, y**3, -z**3], [x**2, y**2, -z**2], [x, y, -z]])

     matriz_simbolica = matriz
           # Derivar cada término de la matriz con respecto a x, y y z
     matriz_derivada = matriz_simbolica.applyfunc(lambda elem: sp.diff(elem, x))
     matriz_derivada_y = matriz_simbolica.applyfunc(lambda elem: sp.diff(elem, y))
     matriz_derivada_z = matriz_simbolica.applyfunc(lambda elem: sp.diff(elem, z))

        # Evaluar las derivadas en un punto específico, por ejemplo, (x=1, y=2, z=3)
     while(Flag):
    
       matriz_derivada_evaluada = (matriz_derivada.subs(punto) + matriz_derivada_y.subs(punto) + matriz_derivada_z.subs(punto))
       matriz_simbolicaa_evaluada = matriz_simbolica.subs(punto)*-1
       print("matriz simbolica evaluanda : \n {}".format(matriz_simbolicaa_evaluada))
       matriz_derivada_evaluada = matriz_derivada_evaluada.applyfunc(lambda elem: round(elem, 4))
       matriz_simbolicaa_evaluada = matriz_simbolicaa_evaluada.applyfunc(lambda elem: round(elem, 4))
      


       print("\n {}={}".format(matriz_derivada_evaluada, matriz_simbolicaa_evaluada))


       matriz_3x1 = sp.Matrix([129, 9.75, 9.49])
       matriz_3x1 = matriz_3x1.applyfunc(lambda elem: round(elem, 4))
  

       matriz_suma = matriz_simbolicaa_evaluada
  
       matriz_suma_lista = matriz_suma.tolist()



       suma_filas = [sum(fila) for fila in matriz_suma_lista]
     

       sumaF = sp.Matrix(suma_filas)
       suma_filas= sumaF+ matriz_3x1

       matriz_suma_filas = sp.Matrix(suma_filas)
    
     
     
  
       print("\n Resultante \n {}={}".format(matriz_derivada_evaluada,matriz_suma_filas))
       matriz_derivada_evaluada= sp.Matrix(matriz_derivada_evaluada)
       soluciones = matriz_derivada_evaluada.LUsolve(matriz_suma_filas)
       soluciones = matriz_derivada_evaluada.LUsolve(matriz_suma_filas).applyfunc(lambda elem: round(elem, 4))
      
      

       print("h1: {} h2: {} h3: {}".format(soluciones[0,0],soluciones[1,0],soluciones[2,0]))
       
       h_previa = soluciones
      
       soluciones = soluciones + puntos
       h= soluciones
      
      
       print("X´: {} Y´: {} Z´: {}".format(soluciones[0,0],soluciones[1,0],soluciones[2,0]))

       
       punto = { x: soluciones[0,0], y: soluciones[1,0], z: soluciones[2,0]}
       puntos = soluciones

       instance_errorRelativo = Error_Relativo()
       

       
       print("ERROR RELATIVO:")
       v1 =abs((h_previa[0,0]/h[0,0])*100)
       v2=abs((h_previa[1,0]/h[1,0])*100)
       v3 = abs((h_previa[2,0]/h[2,0])*100)

       print(v1)
       print(v2)
       print(v3)
       
       if (v1 < 0.005 or v1 == 0) and  valor1 == False:
         valor1= True
         
         valor_correcto = h[0,0]
         print("\n*********************VALOR XENCONTRADO: {} iteracion{}".format(valor_correcto, contador))
       if (v2< 0.005 or v2== 0) and valor2 ==False:
         valor2 =True
         valor_corrercto2= h[1,0]
         print("\n******************VALOR y ENCONTRADO: {} iteracion {}".format(valor_corrercto2, contador))
       if ( v3< 0.005 or v3 == 0) and valo3 ==False:
         valo3 = True
         
         valor_correcto3 = h[2,0]
         print("\n*****************VALOR z ENCONTRADO: {} iteracion {}".format(valor_correcto3, contador))

       if valor1 and valor2 and valo3:
         print("[{}, {} ,{}]".format(valor_correcto,valor_corrercto2,valor_correcto3))
         Flag = False
       

       print("\n Iteracion {} \n".format(contador))
       contador += 1 
      
       


      


            
    


