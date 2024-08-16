

def suma(x, y):
    suma = x + y
    return suma

def resta(x, y):
    resta = x - y
    return resta

def multi(x, y):
    multi = x * y
    return multi

def div(x, y):
    div = x / y
    return div

if __name__ == "__main__":

    resultado = 0

    while True:

        

        print('Seleccione la operación que desea realizar> ')
        
        print('1) Suma \n')
        print('2) Resta \n')
        print('3) Multiplicación \n')
        print('4) División \n')
        z= int(input("Opción: "))
        print('\n')
        x = int(input("Ingresa el primer numero> "))
        y = int(input("Ingresa el segundo numero> "))


        match z: 
            case 1:
                resultado= suma(x,y)
            case 2:
                resultado= resta(x,y)
            case 3:
                resultado= multi(x,y)
            case 4:
                resultado= div(x,y)

            case _:
                print('La operación seleccionada no existe')
        
        print('El resultado es: ', resultado)
        print('\n')
        b= input('Desea realizar una nueva operación? s/n: ')

        if b=='s':
            continue
        elif b=='n':
            break

        
        

