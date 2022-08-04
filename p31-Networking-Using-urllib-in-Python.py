#Using urlib in python
#since HTTP is common , we have a lubrary that does all the 
#socket work for us and makes web pages look like a file

""" existe una libreria que nos deja hacer lo mismo que con e
el socket , esto para recuperar archivos y hacer una llamada 
al socket ES ELEGANTAMENTE SIMPLE"""

#MANDAR UN URL Y LEER EL CONTENIDO WEB
import urllib.request, urllib.parse, urllib.error 
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #LLAMAMOS A LA URLOPEN Y LE DAMOS LA URL
#CODIFICA , RECUPERA EN BYTES Y LOS DECODIFICA
for line in fhand:                                               #
    print(line.decode().strip())# ES COMO LEER , ABRIR ,IMPRIMIR

#------------------------



