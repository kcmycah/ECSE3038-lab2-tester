from datetime import datetime as dt
from flask import Flask, jsonify,request

app = Flask(__name__) 

FAKE_DATABASE=[]
count = 0

#GET/Profile
@app.route("/Profile", methods =["GET"])
def getProfile():
  u = request.json["username"]
  c = request.json["color"]
  r = request.json["role"]

  global now
  now= dt.now()
  user_object = {
     "username":u,
     "color": c,
     "role": r,
     "last_updated": now
  }

  FAKE_DATABASE.append(user_object)
  return jsonify({"data":user_object})

#POST/Profile
@app.route("/profile", methods=["POST"])
def postProfile():
  u = request.json["username"]
  c = request.json["color"]
  r = request.json["role"]

  global now
  now = dt.now()
  user_object = {
     "username":u,
     "color": c,
     "role": r,
     "last_updated": now
  }

  FAKE_DATABASE.append(user_object)
  return jsonify({"data":user_object})


#PATCH/Profile
@app.route("/profile", methods=["PATCH"])
def patchProfile():
  
  for u in FAKE_DATABASE:
    if u["color"] != request.json["color"]:
       u["color"] = request.json["color"]
       return jsonify(u)


#GET/Data
@app.route("/data", methods = ["GET"])
def getdata():
  o = request.json["long"]
  a = request.json["lat"]
  p = request.json["percentage_full"]

  global count
  count += 1

  user_object = {
    "id" : count,
    "location" : "Engineering Department",
    "lat" : a,
    "long" : o,
    "percentage_full":p
  }
  
  FAKE_DATABASE.append(user_object)
  return jsonify(user_object)

#POST/Data
@app.route("/data", methods = ["POST"])
def postdata():
  o = request.json["long"]
  a = request.json["lat"]
  p = request.json["percentage_full"]

  global count
  count += 1

  user_object = {
    "id" : count,
    "location" : "Physics Department",
    "lat" : a,
    "long" : o,
    "percentage_full":p
  }
  
  FAKE_DATABASE.append(user_object)
  return jsonify(user_object)

#PATCH/Data/:id
@app.route("/data/<int:id>", methods=["PATCH"])
def patchData(id):
  
  for u in FAKE_DATABASE:
    if u["id"] == id:
      u["long"] = request.json["long"]
    return jsonify(u)

#DELETE/Data/:id
@app.route("/data/<int:id>", methods = ["DELETE"])
def deleteData(id):
  
  for u in FAKE_DATABASE:
    if u["id"] == id:
      FAKE_DATABASE.remove(u) 

    if (u["id"] != id):
      user_object = {
          "Success":"True"
          }
  return jsonify(user_object)

if __name__ == '__main__':
  app.run(debug = True,port = 3000, host = "0.0.0.0" )
