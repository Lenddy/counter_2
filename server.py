from flask import Flask, session,render_template,redirect
app= Flask(__name__)
#use the secreate key
app.secret_key = "secret"


#always save your files
#use the decorator
#shows counter
@app.route("/")
def show_counter():
    if "number_of_visits" in session: 
        session["number_of_visits"] += 1
    else:
        session["number_of_visits"] = 1
    return render_template("index.html")


#errased teh count
@app.route("/destroy_session", methods = ["post"])
def destroy_session():
    session.clear()
    # session.pop("name of the key")  clears a specific key name
    # if "number_of_visits" in session:           this also works
    #     session["number_of_visits"] = 0
    return redirect("/")


#increace the count by 3
@app.route("/add_to_count" , methods = ["post"])
def add_to_count():
#you have to set this to 2 because it is already incrementin by 1 in line 13
    session["number_of_visits"] += 2
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True)