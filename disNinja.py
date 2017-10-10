from flask import Flask, render_template
app = Flask(__name__)                    
                
@app.route('/')           
def home_page():
  return render_template('ninjaHome.html')    

@app.route('/ninja')         
def ninja_page():
    print"inside ninja display pic"
    return render_template('ninja.html')    
@app.route('/ninja/blue')
def Blue():
    return render_template("blue.html")

@app.route('/ninja/orange')
def Orange():
    return render_template("orange.html")

@app.route('/ninja/red')
def Red():
    return render_template("red.html")

@app.route('/ninja/purple')
def Purple():
    return render_template("purple.html")

@app.route('/ninja/<vararg>')
def Random(vararg):
    return render_template("notapril.html")

app.run(debug=True) 

   
