from flask import Flask, render_template, request

app = Flask(__name__, template_folder='./src/views')

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
         return render_template("index.html")
    else:
        if (request.form["num1"] != "" or request.form["num2"] != ""):
            if (request.form["opc"] == "soma"):
                 return {
                      "Resultado":str(int(request.form["num1"]) + int(request.form["num2"]))
                 }
            elif (request.form["opc"] == "subt"):
                 return {
                      "Resultado":str(int(request.form["num1"]) - int(request.form["num2"]))
                 }
            elif (request.form["opc"] == "mult"):
                 return {
                      "Resultado": str(int(request.form["num1"]) * int(request.form["num2"]))
                 }
            elif (request.form["opc"] == "divi"):
                 return {
                      "Resultado":str(int(request.form["num1"]) / int(request.form["num2"]))
                 }
        else:
            return "Informe um valor válido!"
# @app.route("/<int:id>")
# def Home_id(id):
#     return str(id + 1)

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

app.run(port=8080, debug=True)
