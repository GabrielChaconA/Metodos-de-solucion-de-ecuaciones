import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Sistema.Menu import Menu
##Archivo a ejecuar 
def main():
    instanciaMenu = Menu()
    instanciaMenu.Menu()


if __name__ == "__main__":
    main()
