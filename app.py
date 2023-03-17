import pymongo
from flask import Flask, Response, request
import json
from bson.objectid import ObjectId
import os


# mongo uri for env variable
try:
    mongo_uri = os.environ["MONGO_URI"]
    mongo = pymongo.MongoClient(mongo_uri, serverSelectionTimeoutMS=1000)
except:
    print("Error - connection error to db")


app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(host="localhost", port=27017, serverSelectionTimeoutMS=1000)
    db = mongo.user_db
    mongo.server_info() # exception trigger
except:
    print("Error - connection error to db")

@app.route("/users",methods=["POST"])

def create_user():
    try:
        user = {"name": request.form["name"],
                "email":request.form["email"],
                "password":request.form["password"]}
        dbResponse = db.users.insert_one(user)
        # for attr in dir(dbResponse):
        #     print(attr)
        return Response(
            response=json.dumps({"message":"user created", "id":f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)

@app.route("/users",methods=["GET"])

def get_user():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"]=str(user["_id"])
        return Response(
            response=json.dumps(data),
            status=500,
            mimetype="application/json"
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "cannot read users"}),
            status=500,
            mimetype="application/json"
        )

@app.route("/users/<id>", methods=["PATCH"])

def update_user(id):
    try:
        dbResponse = db.users.update_many({"_id":ObjectId(id)},
                                         {"$set":{"name":request.form["name"],
                                                  "email":request.form["email"],
                                                  "password": request.form["password"]
                                                  }})
        for attr in dir(dbResponse):
                print(f"{attr}")  # used to see the response content
        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps({"message": "Details updated"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps({"message": "Details entered were the same as before"}),
                status=200,
                mimetype="application/json"
            )


    except Exception as ex:
        return Response(
            response=json.dumps({"message": "Failed to update"}),
            status=500,
            mimetype="application/json"
        )

@app.route("/users/<id>", methods=["DELETE"])

def delete_user(id):
    try:
        dbResponse = db.users.delete_one({"_id":ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(
                response=json.dumps({"message": "User successfully deleted", "id":f"{id}"}),
                status=200,
                mimetype="application/json"
            )
        return Response(
            response=json.dumps({"message": "invalid id or the user does not exist"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        return Response(
            response=json.dumps({"message": "Failed to delete the user"}),
            status=500,
            mimetype="application/json"
        )

if __name__ == "__main__":
    app.run(port=80, debug=True)

