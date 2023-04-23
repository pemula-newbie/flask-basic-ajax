'''
	AIM4 - Flask - [A] Basic - [06] AJAX
	
	Orbit Future Academy - AI Mastery - KM Batch 4
	Tim Deployment
	2023
'''

# =[Modules dan Packages]========================
from flask import Flask,render_template,request,jsonify
from flask_ngrok import run_with_ngrok

# =[Variabel Global]=============================
app = Flask(__name__, static_url_path='/static')

# =[Routing]=====================================
@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/api/setnama",methods=['POST'])
def apiSetNama():
	data_nama = ""
	if request.method=='POST':
		data_nama = request.form['data']
		return jsonify({
			"data": data_nama,
		})

# =[Main]========================================
if __name__ == '__main__':
    run_with_ngrok(app)
    app.run()