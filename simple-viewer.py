from flask import Flask,render_template,Response 
app = Flask(__name__)


@app.route('/')
def root():
     return render_template("index.html") 

@app.route('/QIDO/studies')
def cond_main():
    cond=open('static/payload1.json','r')
    # type application/dicom+json
    return Response(cond.read(),mimetype='application/dicom+json')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000, threaded=True )
