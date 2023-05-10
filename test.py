from pymongo import MongoClient

c = MongoClient()
print(c)

db = c['tp2']
# -------------------Q1------------------------
# r = db.produits.insert_one({
#     "nom": "Macbook Pro",
#     "fabriquants": "Apple",
#     "prix": "1299,99",
#     "options": [
#         {"option": "Intel Core i5"},
#         {"option": "Retina Display"},
#         {"option": "Long life battery"},
#     ]
# })
# print(r)
# -------------------Q2------------------------
# r = db.produits.insert_many([
#     {
#         "nom": "Macbook Air",
#         "fabriquants": "Apple",
#         "prix": "1099,99",
#         "ultrabook": "True",
#         "options": [
#             {"option": "Intel Core i5"},
#             {"option": "SSD"},
#             {"option": "Long life battery"},
#         ]
#     },
#     {
#         "nom": "Thinkpad X230",
#         "fabriquants": "Lenovo",
#         "prix": "999,99",
#         "ultrabook": "True",
#         "options": [
#             {"option": "Intel Core i5"},
#             {"option": "Retina Display"},
#             {"option": "Long life battery"},
#         ]
#     }
# ])
# print(r)
# -------------------Q3------------------------
# resultat = db.produits.find()
# Lres = list(resultat)
# print(Lres)
# -------------------Q4------------------------
# r = db.produits.find_one()
# print(r)
# -------------------Q5------------------------
# r = db.produits.find({"nom": "Thinkpad X230"})
# r = db.produits.find({"nom": {"$regex": "Thinkpad X230"}})
# r = db.produits.find({"nom": {"$regex": "thinkpad", "$options": "i"}})
# Lres = list(r)
# print(Lres)
# -------------------Q6------------------------
# r = db.produits.find({"prix": {"$gt": "1200"}})
# Lres = list(r)
# print(Lres)
# -------------------Q7------------------------
# r = db.produits.find_one({"ultrabook": "True"})
# Lres = list(r)
# print(Lres)
# -------------------Q8------------------------
# r = db.produits.find({"nom": ".*Macbook.*"})
## r = db.produits.find({"nom": {"$regex": "Macbook "}})
## r = db.produits.find({"nom": {"$regex": "Macbook", "$options": "i"}})
# Lres = list(r)
# print(Lres)
# -------------------Q9------------------------
# r = db.produits.find({"nom": "^Macbook.*"})
## r = db.produits.find({"nom": {"$regex": "Macbook "}})
## r = db.produits.find({"nom": {"$regex": "Macbook", "$options": "i"}})
# Lres = list(r)
# print(Lres)
# -------------------Q10-----------------------
# resultat=db.personnes.find({"diplome":True})
# Lres = list(resultat)
# print(len(Lres))
# -------------------Q11------------------------
# r = db.personnes.find()
# for x in r:
#     y = x['age']
#     y = 1+y
#     db.personnes.update_one({"_id": x['_id']}, {"$set": {"age": y}})
# print(list(r))
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

# # Connect to the MongoDB server (replace the connection string with your own if necessary)
# client = MongoClient('mongodb://localhost:27017/')

# # Choose a database and a collection
# db = client['my_database']
# collection = db['etudiants']

# # Insert a document
# document = {
#     "_id": "1234",
#     "nom": "Alami",
#     "Modules": [
#         {"id": "M101", "titre": "Métier et formation", "note": 18},
#         {"id": "M102", "titre": "Algorithmique", "note": 11},
#         {"id": "M104", "titre": "PSWS", "note": 14}
#     ]
# }
# collection.insert_one(document)

# # Query documents
# query = {"nom": "Alami"}
# results = collection.find(query)
# for result in results:
#     print(result)

# # Update a document
# filter = {"Modules.titre": "Algorithmique"}
# update = {"$set": {"Modules.$.titre": "Algo"}}
# collection.update_many(filter, update)
