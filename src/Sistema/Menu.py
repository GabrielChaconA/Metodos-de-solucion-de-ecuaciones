from Metodos.metodo_jacobi import metoodo_jacobi
from Metodos.metodo_seidel import metodo_seidel
from Metodos.newton_Raphson import newton
class Menu:
    def Menu(self):
        instance_metodoJacobi = metoodo_jacobi()
        instance_metodoSeidel = metodo_seidel()
        instance_metodoNewton = newton()
        anwer = input("Elige un metodo:Jacobi(1) Seidel(2) Gauss(3)\n")
        if anwer == "1" :
         instance_metodoJacobi.matriz_jacobi()
        if anwer == "2":
         instance_metodoSeidel.matriz_seidel()
        if anwer == "3":
         instance_metodoNewton.newton()
         
        return 