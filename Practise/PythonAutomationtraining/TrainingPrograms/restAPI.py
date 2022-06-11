from flask import Flask,jsonify
app = Flask(__name__)
@app.route("/", methods=["GET"])
def function():
   return jsonify({"message": "welcome to Python"}), 200
if __name__ == "__main__":
   app.run(host="0.0.0.0", debug=True, port=6000)
