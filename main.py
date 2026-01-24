import csv
import matplotlib.pyplot as plt

def Cargar_datos(fichero):
    DiccionarioAlumnos = {}
    notas = open(fichero, "r", encoding="utf-8", newline='')
    try:
        reader = csv.reader(notas, delimiter=',')
        next(reader)
        for row in reader:
            alumno = row[0].strip().capitalize()
            nota_str = row[2].strip()
            try:
                if "," in nota_str:
                    continue
                nota = float(nota_str)
            except ValueError:
                continue
            if alumno not in DiccionarioAlumnos:
                DiccionarioAlumnos[alumno] = {'notas': [nota]}
            else:
                DiccionarioAlumnos[alumno]['notas'].append(nota)
    finally:
        notas.close()
    return DiccionarioAlumnos

def Cargar_becas(fichero, diccionario):
    with open(fichero, "r", encoding="utf-8") as becas:
        for linea in becas:
            if ':' not in linea:
                continue

            alumno, estaBecado = linea.split(':', 1)
            alumno = alumno.strip().capitalize()
            estaBecado = estaBecado.strip().upper()

            if alumno in diccionario:
                diccionario[alumno]['becado'] = estaBecado
    return diccionario


def Crear_grafica(diccionario):
    nombres = []
    medias = []
    print("Alumno -- NotaMedia -- Estado -- Beca")
    for nombre, datos in diccionario.items():
        media = round(sum(datos['notas']) / len(datos['notas']), 2)
        datos['media'] = media
        beca_status = " (Beca)" if datos.get('becado') == "SI" else ""
        nombres.append(nombre + beca_status)
        medias.append(media)

        if media >= 5:
            datos['estado'] = 'APROBADO'
        else:
            datos['estado'] = 'SUSPENSO'
        print(f"{nombre} -- {datos['media']} -- {datos['estado']} -- {datos.get('becado', 'NO')}")

    colores = ['green' if m >= 5 else 'red' for m in medias]
    plt.bar(nombres, medias, color=colores)
    plt.xticks(rotation=90, ha='right')
    plt.axhline(y=5, color='blue', linestyle='-')
    plt.title('Notas segun Alumnos. Alejandro Jiménez')
    plt.tight_layout()
    plt.savefig('notes_graph.png')
    plt.show()

dict_notas = Cargar_datos('ej30notasdaw.csv')
dict_notas_becas = Cargar_becas('ej30becas.txt', dict_notas)
Crear_grafica(dict_notas_becas)
