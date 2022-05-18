# Proyecto-MongoDB

Como podemos ver en este proyecto hemos importado un json en nustra base de datos de MongoDB.

Y hemos realizado los siguientes apartados de ejercicios y consultas.

# EJERCICIOS

	1 Importar con mongoimport el correspondiente json

	2 Insertar con insertOne y insertMany varios documentos.

		2.1 insertOne
		2.2 insertMany

	3 Eliminar documentos utilizando deleteOne y deleteMany

		3.1 deleteOne
		3.2 deleteMany

	4 Actualizar documentos utilizando updateOne, updateMany y replaceOne

		4.1 updateOne
		4.2 updateMany
		4.3 replaceOne


# CONSULTAS

## 5 consultas de datos simples:

	1 Busca el personcapituloaje cuyo nombre es Zoom Encounters y tiene hora de salida del episodio (airtime) a las 10:45.

	2 Obtener los 4 primeros capitulos que empiezen por R.

	3 Contar los capitulos con runtime menor de 16 y de type regular.

	4 Mostrar los capitulos cuyo type sea las regular.

	5 Obtener de menor a mayor los airdate cuyo number este entre 25 y 39.

## 3 consultas con arrays.

	6 Crear un array en el capitulo con id 1853149 donde podamos almacenar la crítica, que en este caso será "excellente", "buena" e "interesante".

	7 Actualiza el airdate del dia 22 al 23 del id 1853145.

	8 Eliminar el runtime y dejarlo como null del capitulo cuyo nombre es "The Scootbop Bop".

## 3 consultas con documentos embebidos.

	9 Obtener todos los id que aparezcan entre las horas del airtime 10:30 y 12:30.

	10 Obtener todos los capitulos cuyo type sea regular.

	11 Eliminar los capitulos que tengan por number 3 y 7.

## 1 consulta de agrupación.

	12 Muestra el mayor number de cada airtime igual a las 17:00.
