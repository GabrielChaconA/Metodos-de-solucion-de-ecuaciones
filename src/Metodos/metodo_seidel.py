import numpy as np
from Metodos.Utils.Error_Relativo import Error_Relativo
class metodo_seidel:
    def matriz_seidel(self):
         A = np.array([[1, 0, 1], 
              [-3, 4, 6], 
              [-1, -2, 3]])
         B= np.array([[6],[30],[8]])
         print(B)
         D2 = np.diag(A)
         D = np.diag(D2)
         print("Diagonal")
         print(D)
         Tx = D - A 
         print("Tx")
         print(Tx)
         D1 = np.linalg.inv(D)
         print("invesa")
         print(D1)
         print("T")
         T = D1 @ Tx
         print(T)
         print("C")
         C =D1@B
         print(C)
         self.metodo_seidel(T,C)



         return None
    def metodo_seidel(self,D1,B):
         valor1 , valor2 , valo3 = False, False, False
         instance_errorRelativo = Error_Relativo()
         w=0.5
         Flag = True
         contador = 0
         y,y2,y3= 0,0,0
         C = np.array([[0],[0],[0]])
         C = np.array(C, dtype=float)


         while(Flag):
        
         
          
          multi =(D1@C)+B
          C[0,0] = round(((1-w)*y)+((w*(multi[0,0]))),4)
          multi =(D1@C)+B
          print("X1 {}: {}".format(contador, C[0,0]))
          
          C[1,0] = round(((1-w)*y2)+((w)*((multi[1,0]))),4)
          multi =(D1@C)+B
          print("X2 {}: {}".format(contador, C[1,0]))
          C[2,0] = round(((1-w)*y3)+((w)*((multi[2,0]))),4)
          multi =(D1@C)+B
          print("X3 {}: {}".format(contador, C[2,0]))

          y,y2,y3= C[0,0],C[1,0], C[2,0]
          C = np.array([[y],[y2],[y3]])
          
          if contador == 0: 
           x= round(C[0,0],4)
           x2= round(C[1,0],4)
           x3= round(C[2,0],4)

          if contador >=1:
            print("ERROR RELATIVO:")
            v1 =round(C[0,0],4)
            v2= round( C[1,0],4)
            v3 = round( C[2,0],4)

            errx1 = round(instance_errorRelativo.Error_Relativo(v1,x),4)
            errx2 = round(instance_errorRelativo.Error_Relativo(v2,x2),4)
            errx3 = round(instance_errorRelativo.Error_Relativo(v3,x3),4)
           
            if errx1 < 0.0005:
               valor1= True
               print("Se econtro x1:{}".format(v1))
               valor_correcto = v1
            if errx2 < 0.0005:
               valor2 =True
               print("Se econtro x2:{}".format(v2))
               valor_corrercto2= v2
            if errx3 < 0.0005:
               valo3 = True
               print("Se econtro x3:{}".format(v3))
               valor_correcto3 = v3
            if valor1 and valor2 and valo3:
               print("[{}, {} ,{}]".format(valor_correcto,valor_corrercto2,valor_correcto3))
               Flag = False

            print(errx1)
            print(errx2)
            print(errx3)

            x= C[0,0]
            x2= C[1,0]
            x3= C[2,0]
          contador += 1
         
         
