import math


def verificar_cedula(cedula=""):
    if len(cedula) != 10:
        raise Exception("Error numero de cedula incompleto")
    else:
        multiplicador = [2, 1, 2, 1, 2, 1, 2, 1, 2]
        ced_array = map(lambda k: int(k), list(cedula))[0:9]
        ultimo_digito = int(cedula[9])
        resultado = []
        arr = map(lambda x, j: (x, j), ced_array, multiplicador)
        for (i, j) in arr:
            if i * j < 10:
                resultado.append(i * j)
            else:
                resultado.append((i * j)-9)
        print resultado
        if ultimo_digito == int(math.ceil(float(sum(resultado)) / 10) * 10) - sum(resultado):
            return True
        else:
            return False


print verificar_cedula("1212121212")
