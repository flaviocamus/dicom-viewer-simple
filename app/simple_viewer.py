from flask import Flask,render_template,Response 
import os 
app = Flask(__name__)


@app.route('/')
def root():
     return render_template("index.html") 

@app.route('/QIDO/studies')
def cond_main():
    print( os.path.dirname(os.path.realpath(__file__)))
    cond=open( os.path.dirname(os.path.realpath(__file__)) +'/static/payload1.json','r')
    # type application/dicom+json
    return Response(cond.read(),mimetype='application/dicom+json')
    #return  os.path.dirname(os.path.realpath(__file__))


if __name__ == '__main__':
    app_port = int(os.environ.get("PORT", 5000 ))
    app.run(host="0.0.0.0", debug=True, port=app_port, threaded=True )
