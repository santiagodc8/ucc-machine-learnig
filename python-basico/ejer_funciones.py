'''crear una funcion que reciba como parametro el tipo de empleado y las horas laboradas.
un empleado tipo A el valor de la hora es de $15000
un empleado tipo B el valor de la hora es de $20000
un empleado tipo C el valor de la hora es de $25000
la cantidad de horas minimas laboradas es de 160 al mes y las maximas 170 al mes
descontar un 2% del valor devengado para ahorro de la cooperativa y un 8% de ley sobre
el valor devengado. La funcion debe retornar en un string el neto pagado y el total deducido'''

def func_sueldo(tipo_empleado, num_horas):
    hora_empleadoA = 15000
    hora_empleadoB = 20000
    hora_empleadoC = 25000

    if 160 <= num_horas <= 170:
        if tipo_empleado == "A":
            hora_empleado = hora_empleadoA
        elif tipo_empleado == "B":
            hora_empleado = hora_empleadoB
        elif tipo_empleado == "C":
            hora_empleado = hora_empleadoC
        else:
            print("El tipo de empleado ingresado no es válido, debe ser A, B o C")
            return

        total_valor_horas = num_horas * hora_empleado
        descuentos = total_valor_horas * 0.10
        sueldo = total_valor_horas - descuentos
        print(f"El sueldo total es: {sueldo}")
    else:
        print(f"El número {num_horas} de horas laborales no es válido")

func_sueldo("C", 160)
