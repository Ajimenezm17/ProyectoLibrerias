# Comandos para crear el entorno virtual y las librerias que estan en nuetro requeriments.txt    
  
**1º Comando:**    
  
PS C:\Python\ProyectoLibrerias> python -m venv practica_diccionarios    
  
    
**2º Comando:**    
  
PS C:\Python\ProyectoLibrerias> .\practica_diccionarios\Scripts\Activate.ps1    
    
Tras el segundo comando veremos que la activacion ha ido bien ya que mostrara el     nombre de nuestro entorno    
(practica_diccionarios) PS C:\Python\ProyectoLibrerias>     
   
Vamos con la instalacion de la librerias.    
**3º Comando:**    
(practica_diccionarios) PS C:\Python\ProyectoLibrerias> python -m pip install -r   requirements.txt    
    
Vamos a ver la lista de librerias que tenemos descargadas.    
**4º Comando:**   
(practica_diccionarios) PS C:\Python\ProyectoLibrerias> python -m pip list    
  
Package         Version    
--------------- -----------    
contourpy       1.3.3    
cycler          0.12.1    
fonttools       4.61.1    
kiwisolver      1.4.9    
matplotlib      3.10.8    
numpy           2.4.1    
packaging       26.0    
pillow          12.1.0    
pip             25.3    
pyparsing       3.3.2    
python-dateutil 2.9.0.post0    
six             1.17.0    
Como podemos comprobar se nos ha instalado Matplotlib.    


Codigo:
---------------
Esta dividido en 3 funciones.

1. Cargar_datos
Se encarga de abrir el archivo, recorrer cada fila depurando los errores que puedan existir con el nombre o la nota segun los parametros del enunciado del trabajo y por ultimo guardar los datos en un diccionario

2. Cargar becas
Se encarga de abri el archivo de becas , recorrer cada linea del archivo y añadir
al diccionario de cada alumno si esta becado o no

3.  Crear_Grafica
Se encarga de recorrer los diccionarios , calcular media y asigna si el estado del alumno es aprobado o suspenso, imprime los datos de los alumnos por consola y crea 
un grafico de barras 