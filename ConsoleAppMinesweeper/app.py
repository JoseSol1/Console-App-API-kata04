from kata04.converter_service import ConverterService

def main():
    cont= True
    while cont:
        print("Bienvenido al Convertidor de Buscaminas\n")
        print("Inserte una Matriz en el siguiente formato:\n")
        print("Ej.\n4 4\n*...\n....\n.*..\n....\n0 0")
        print("\nInserte la matriz:\n")

        lines=[]
        while True:
            line= input().strip()
            if line== "0 0":
                break
            lines.append(line)

        matrixInput= "\n".join(lines)
        convertedMatrix= ConverterService.convertMatrix(matrixInput)
        if convertedMatrix=="":
            print("\nError al convertir, verifique su entrada e intente denuevo\n")
        else:
            print("\nMatriz Convertida")
            print(convertedMatrix)

        while True:
            print("Desea continuar? (s/n)")
            stop= input().strip().lower()
            if stop!= 'n' and stop!= 's':
                print("Opcion invalida, inserte denuevo")
            elif stop== 'n':
                cont=False
                break
            elif stop == 's':
                break    
            



if __name__== "__main__":
    main()