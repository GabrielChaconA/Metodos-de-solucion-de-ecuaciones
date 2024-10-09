import numpy as np
from Metodos.Utils.Error_Relativo import Error_Relativo
class metoodo_jacobi:
    def matriz_jacobi(self):
        ##Procedimiento
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
        
        self.metodo_jacobi(T,C)
        return None
    

    def metodo_jacobi(self,T,C):
        valor1 , valor2 , valo3 = False, False, False
        instance_errorRelativo = Error_Relativo()
        m_inicio = np.array([[0],[0],[0]])
        Flag = True
        x,x2,x3 = 0,0,0
        contador = 0
        while Flag:
         x1 = (T @  m_inicio)+C
         m_inicio = x1
         print("JACOBI")
         print(" {}     +  \n  {}".format(T,m_inicio))
         
         if contador == 0: 
          print(m_inicio[0,0])
          x= m_inicio[0,0]
          x2= m_inicio[1,0]
          x3= m_inicio[2,0]
         if contador >=1:
            print("ERROR RELATIVO:")
            v1 =m_inicio[0,0]
            v2= m_inicio[1,0]
            v3 = m_inicio[2,0]
            
            if instance_errorRelativo.Error_Relativo(v1,x) < 0.005 and valor1 == False :
               valor1= True
               valor_correcto = v1
            if instance_errorRelativo.Error_Relativo(v2,x2) < 0.005 and valor2 == False  :
               valor2 =True
               valor_corrercto2= v2
            if instance_errorRelativo.Error_Relativo(v3,x3) < 0.005 and valo3 == False:
               valo3 = True
               valor_correcto3 = v3
            if valor1 and valor2 and valo3:
               print("[{}, {} ,{}]".format(valor_correcto,valor_corrercto2,valor_correcto3))
               Flag = False
            
            print(instance_errorRelativo.Error_Relativo(v1,x))
            print(instance_errorRelativo.Error_Relativo(v2,x2))
            print(instance_errorRelativo.Error_Relativo(v3,x3))
            x= m_inicio[0,0]
            x2= m_inicio[1,0]
            x3= m_inicio[2,0]

         contador += 1
       

        return None