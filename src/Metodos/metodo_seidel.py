import numpy as np
from Metodos.Utils.Error_Relativo import Error_Relativo
class metodo_seidel:
    def matriz_seidel(self):
         A = np.array([[4, 1, 2], 
              [3, 5, 1], 
              [1, 1, 3]])
         B= np.array([[4],[7],[3]])
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
         w=1.2
         Flag = True
         contador = 0
         y,y2,y3= 0,0,0
         C = np.array([[0],[0],[0]])
         C = np.array(C, dtype=float)


         while(Flag):
        
         
          
          multi =(D1@C)+B
          C[0,0] = round(((1-w)*y)+((w*(multi[0,0]))),4)
          multi =(D1@C)+B
          print("X{}: {}".format(contador, C[0,0]))
          
          C[1,0] = round(((1-w)*y2)+((w)*((multi[1,0]))),4)
          multi =(D1@C)+B
          print("X{}: {}".format(contador, C[1,0]))
          C[2,0] = round(((1-w)*y3)+((w)*((multi[2,0]))),4)
          multi =(D1@C)+B
          print("X{}: {}".format(contador, C[2,0]))

          y,y2,y3= C[0,0],C[1,0], C[2,0]
          C = np.array([[y],[y2],[y3]])
          
          if contador == 0: 
           x= C[0,0]
           x2= C[1,0]
           x3= C[2,0]
          if contador >=1:
            print("ERROR RELATIVO:")
            v1 =C[0,0]
            v2= C[1,0]
            v3 = C[2,0]
            print(instance_errorRelativo.Error_Relativo(v1,x))
            print(instance_errorRelativo.Error_Relativo(v2,x2))
            print(instance_errorRelativo.Error_Relativo(v3,x3))
            x= C[0,0]
            x2= C[1,0]
            x3= C[2,0]
            if instance_errorRelativo.Error_Relativo(v1,x) < 0.005:
               valor1= True
               valor_correcto = v1
            if instance_errorRelativo.Error_Relativo(v2,x2) < 0.005:
               valor2 =True
               valor_corrercto2= v2
            if instance_errorRelativo.Error_Relativo(v3,x3) < 0.005:
               valo3 = True
               valor_correcto3 = v3
            if valor1 and valor2 and valo3:
               print("[{}, {} ,{}]".format(valor_correcto,valor_corrercto2,valor_correcto3))
               Flag = False
          contador += 1
         
