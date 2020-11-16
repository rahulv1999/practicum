from flask import Flask,render_template,send_from_directory,request,redirect
from Duffing2 import duffing
from livereload import Server

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

alpha = -1       # -1
beta = 1         # 1
delta = 0.3       # 0.3
gam = 0.15    # 0.15
w = 1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/obj')
def obj():
    return render_template('obj.html')

@app.route('/obj_gif',methods=['POST'])
def obj_gif():
    alpha = float(request.form.get("alpha1"))/1    # -1
    beta = float(request.form.get("beta1"))/1         # 1
    delta = float(request.form.get("gamma1"))/1      # 0.3
    gam = float(request.form.get("delta1"))/1   # 0.15
    w = float(request.form.get("w1"))/1
    duffing(alpha,beta,delta,gam,w)
    data = f" α : {alpha} ,β : {beta} ,γ : {gam} ,δ : {delta}, ω : {w}"
    return render_template('submit.html',data = data )

@app.route('/theory')
def theory():
    return render_template('theory.html')

@app.route('/proc')
def proc():
    return render_template('proc.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')
@app.route('/ref')
def ref():
    return render_template('ref.html')

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()