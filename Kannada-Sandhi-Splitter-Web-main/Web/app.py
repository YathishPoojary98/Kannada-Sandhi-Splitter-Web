from flask import Flask, render_template, redirect, url_for,request,flash, session
from flask_session import Session
from flask import make_response
from flask_cors import CORS
from Splitter.correct_sandhi_mod import *
from Splitter.utf2wx import convert
app = Flask(__name__,template_folder='template')
app.secret_key = "super secret key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
CORS(app)

@app.route("/")
def index():
	if session.get("name")==None and session.get("institution") == None:
		return redirect(url_for("login"))
	return render_template('index.html')
        
        
        
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        session["institution"] = request.form.get("institution")
        return redirect(url_for("index"))
    return render_template("login.html")
    
    
@app.route("/logout")
def logout():
    session["name"] = None
    session["institution"] = None
    return redirect(url_for("index"))


@app.route('/result', methods=['GET', 'POST'])
def result():
   message = None
   if request.method == 'POST':
        res_dict = {}
        word = request.form.get('inputword')
        word = word.replace(' ','')
        wx = convert(word)
        res = sandhi_splitter(wx,4)
        if res[0]==0:
        	s = "ಸಂಧಿ ಪದ ಛೇದ ಸಫಲವಾಗಲಿಲ್ಲ"
        elif res[0] == 1:
        	s = "ಸಂಧಿ ಪದ ಛೇದ ಸಫಲವಾಗಿದೆ"
        
        res_dict[1]=s
        res_dict[2] = word
        if res[1] != '':
        	padas = (res[1].split("=>")[1]).split('+')
        
        	purvapada = padas[0]
        	uttarapada = padas[1]
        	res_dict[3] = purvapada
        	res_dict[4] = uttarapada
        	res_dict[5] = (res[1].split("=>")[0]).replace('\n','')
        else:
        	for i in range(3,6):
        		res_dict[i]=''
        return render_template('result.html', res_dict=res_dict)
        

@app.route('/feedback',methods=['GET','POST'])
def feedback():
	if request.method == 'POST':
		#print("Here")
		#print(request.form.keys())
		#for x in request.form.keys():
			#print(type(x))
		#print(list(request.form.values()))
		data = request.form
		#print(data)
		flag = 0
		purva = data["data[purvapada]"]
		uttara = data["data[uttarapada]"]
		sandhi = data["data[sandhi]"]
		word = data["data[inputword]"]
		name = data["data[name]"]
		inst = data["data[inst]"]
		if (purva != '' and uttara != '' and sandhi != ''):
		
			writestring = f"ಹೆಸರು : {name}\nಸಂಸ್ಥೆ : {inst}\nಕನ್ನಡ ಪದ : {word}\nಪೂರ್ವಪದ : {purva}\nಉತ್ತರಪದ : {uttara}\nಸಂಧಿ : {sandhi}\n\n"
			def writetofile(s):
				try:
					with open("feedbacks.txt","a") as f:
						f.write(s)
					return 1
				except:
					return 0
			flag = writetofile(writestring)
		
		if flag==1:
			res = "success"
		else:
			res =  "failure"
		return res
	return render_template('feedback.html')

@app.route('/out',methods=['GET','POST'])
def out():
	if request.method == 'POST':
		#print("Here")
		#print(request.form.keys())
		#for x in request.form.keys():
			#print(type(x))
		#print(list(request.form.values()))
		data = request.form
		#print(data)
		cval = data["data[cval]"]
		if cval != "ಇಲ್ಲ":
			purva = data["data[purvapada]"]
			uttara = data["data[uttarapada]"]
			sandhi = data["data[sandhi]"]
			word = data["data[inputword]"]
			name = data["data[name]"]
			inst = data["data[inst]"]
			writestring = f"ಹೆಸರು : {name}\nಸಂಸ್ಥೆ : {inst}\nಕನ್ನಡ ಪದ : {word}\n{purva}\n{uttara}\n{sandhi}\nfeedback : {cval}\n\n"
		else:
			word = data["data[inputword]"]
			name = data["data[name]"]
			inst = data["data[inst]"]
			writestring = f"ಹೆಸರು : {name}\nಸಂಸ್ಥೆ : {inst}\nಕನ್ನಡ ಪದ : {word}\nfeedback : {cval}\n\n"
		def writetofile(s):
			try:
				with open("correctoutputs.txt","a") as f:
					f.write(s)
				return 1
			except:
				return 0
		flag = writetofile(writestring)
		
		if flag==1:
			res = "success"
		else:
			res =  "failure"
		return res
		
	return render_template('out.html')


if __name__ == "__main__":
    app.run(debug = True, port=0, host='0.0.0.0')
