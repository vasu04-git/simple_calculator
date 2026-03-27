from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def calculator():
    result=None

    if request.method=="POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form['operation']

        if operation == "add":
            result = num1 + num2
        elif operation == "subtact":
            result = num1 - num2
        elif operation == "Multiply":
            result == num1*num2
        elif operation == "divide":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "cannot divide by Zero"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

