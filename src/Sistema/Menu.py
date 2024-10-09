from Metodos.metodo_jacobi import metoodo_jacobi
from Metodos.metodo_seidel import metodo_seidel
from Metodos.newton_Raphson import newton
from Metodos.metodo_puntoFijo import metodo_puntoFijo
class Menu:
    def Menu(self):
        instance_metodoJacobi = metoodo_jacobi()
        instance_metodoSeidel = metodo_seidel()
        instance_metodoNewton = newton()
        instance_puntoFijo = metodo_puntoFijo()
        flag = True
        """ anwer = input("Elige un metodo:Jacobi(1) Seidel(2) Gauss(3) PuntoFijo(4)\n") """
        while (flag):
          anwer = input("Escoja su metodo (1)JACOBI (2) SEIDEL (3)NEWTON RAPHSON (4)PUNTO  FIJO\n")
          if anwer == "1" :
            instance_metodoJacobi.matriz_jacobi()
          elif anwer == "2":
           instance_metodoSeidel.matriz_seidel()
          elif anwer == "3":
           instance_metodoNewton.newton()
          elif anwer == "4":
            instance_puntoFijo.metodo_puntoFijo()
          else:
           flag = False
          
         
        return 