# GONZALO PEÑA CALERO 1ºASIR

# CONSULTAS.

# 5 consultas de datos simples:

# 1 Busca el personcapituloaje cuyo nombre es Zoom Encounters y tiene hora de salida del episodio (airtime) a las 10:45.

db.rick.find({"name":"Zoom Encounters"},{"airtime": "10:45"})

# 2 Obtener los 4 primeros capitulos que empiezen por R.

db.rick.find({"name":/R/},{"name":1}).limit(4)

# 3 Contar los capitulos con runtime menor de 16 y de type regular.

db.rick.find({"type":"regular"},{"runtime":{$lt:16}}).count()

# 4 Mostrar los capitulos cuyo type sea las regular.

db.rick.find({"type": "regular"},{"name":1})

# 5 Obtener de menor a mayor los airdate cuyo number este entre 25 y 39.

db.rick.find({"number":{$gte:25,$lte:39}},{"airdate":1}).sort({"airdate":1})

# 3 consultas con arrays.

# 6 Crear un array en el capitulo con id 1853149 donde podamos almacenar la crítica, que en este caso será "excellente", "buena" e "interesante".

db.rick.update({ "id": 1853149 },{$push:{"critics":["excellent", "good", "interesting"]}})

# 7 Actualiza el airdate del dia 22 al 23 del id 1853145.

db.rick.update({"id":1853145},{$push:{[airdate:{$each:"2020-05-23"]}})

# 8 Eliminar el runtime y dejarlo como null del capitulo cuyo nombre es "The Scootbop Bop".

db.rick.update({"name":"The Scootbop Bop"},{$push:{runtime:{$each:[null]}}})

# 3 consultas con documentos embebidos.

# 9 Obtener todos los id que aparezcan entre las horas del airtime 10:30 y 12:30.

db.rick.find({"airtime":"10:30-12:30"},{"id":1})

# 10 Obtener todos los capitulos cuyo type sea regular.

db.rick.find({"type":"regular"},{"name":1})

# 11 Eliminar los capitulos que tengan por number 3 y 7.

db.rick.deleteMany({"number":"3 - 7"})

# 1 consulta de agrupación.

# 12 Muestra el mayor number de cada airtime igual a las 17:00.

db.rick.aggregate([{$group: {"_id":{"airtime":"$17:00"},"number":{$max:"$number"}}}])
