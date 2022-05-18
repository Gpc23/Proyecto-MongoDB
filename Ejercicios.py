# GONZALO PEÑA CALERO 1ºASIR

# EJERCICIOS

# 1 Importar con mongoimport el correspondiente json

mongoimport --db rick --collection rick --jsonArray --file rick.json

# 2 Insertar con insertOne y insertMany varios documentos.

# 2.1 insertOne

db.rick.insertOne({
  "id": 2286140,
  "url": "https://www.tvmaze.com/search?q=morty",
  "name": "Morty1",
  "season": 2,
  "number": 7,
  "type": "regular",
  "airdate": "2021-04-12",
  "airtime": "17:00",
  "airstamp": "2021-04-10T21:00:00+00:00",
  "runtime": 15,
  "rating": {
    "average": null
  },
  "image": null,
  "summary": null,
  "_links": {
    "self": {
      "href": "https://api.tvmaze.com/episodes/2286140"
    }
  }
})

# 2.2 insertMany

db.rick.insertMany(
    [
        {
        "id": 2286141,
        "url": "https://www.tvmaze.com/search?q=morty2",
        "name": "Morty2",
        "season": 4,
        "number": 8,
        "type": "regular",
        "airdate": "2021-04-13",
        "airtime": "17:00",
        "airstamp": "2021-04-10T21:00:00+00:00",
        "runtime": 15,
        "rating": {
          "average": null
        },
        "image": null,
        "summary": null,
        "_links": {
          "self": {
            "href": "https://api.tvmaze.com/episodes/2286141"
                }
            }
        },
        {
        "id": 2286142,
        "url": "https://www.tvmaze.com/search?q=morty3",
        "name": "Morty3",
        "season": 2,
        "number": 7,
        "type": "regular",
        "airdate": "2021-04-14",
        "airtime": "17:00",
        "airstamp": "2021-04-10T21:00:00+00:00",
        "runtime": 15,
        "rating": {
          "average": null
        },
        "image": null,
        "summary": null,
        "_links": {
          "self": {
            "href": "https://api.tvmaze.com/episodes/2286142"
            }
            }
        }
    ])

# 3 Eliminar documentos utilizando deleteOne y deleteMany

# 3.1 deleteOne

db.rick.deleteOne({"id":2286140})

# 3.2 deleteMany

db.rick.deleteMany({"airtime": "10:30"})



# 4 Actualizar documentos utilizando updateOne, updateMany y replaceOne

# 4.1 updateOne

db.rick.updateOne({"id":2286142},{$set:{"season": 3}})

# 4.2 updateMany

db.rick.updateMany({"runtime": 15},{$set:{"runtime": 14}})

# 4.3 replaceOne

db.rick.replaceOne({"name": "Morty3"},{"airtime": "17:05"})
