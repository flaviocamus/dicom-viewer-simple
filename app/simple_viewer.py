from flask import Flask,render_template,Response,request
import os 
import requests


app = Flask(__name__)


ORTHANC = 'http://orthanc:orthanc@localhost:8042'

@app.route('/')
def root():
     return render_template("index.html") 

@app.route('/QIDO/studies',methods=["GET"])
def cond_main():
    #params
    limit=request.args.get('limit')

    print( os.path.dirname(os.path.realpath(__file__)))
    cond=open( os.path.dirname(os.path.realpath(__file__)) +'/static/payload2.json','r')
    # type application/dicom+json
    return Response(cond.read(),mimetype='application/dicom+json')
    #return  os.path.dirname(os.path.realpath(__file__))

@app.route('/dicom-web/studies/<study>/metadata')
def wado_meta(study):
    #wado root
    print("received study: "+study)
    #flask reverse proxy , https://medium.com/customorchestrator/simple-reverse-proxy-server-using-flask-936087ce0afb
    if request.method=='GET':
        argu=request.args.to_dict()
        r_argu=""
        #for key in argu.keys():
        #    r_argu =r_argu+ key+"="+argu[key]+'&'
        path='/dicom-web/studies/'+study+"/metadata"
        print("proxy to: "+ORTHANC+path)
        resp = requests.get(ORTHANC+path)
        response =resp.content
        print(str(response),resp.status_code)
    return Response(resp.content  , mimetype='application/dicom+json')

@app.route('/dicom-web/studies/<study>/series/<serie>/instances/<instance>/frames/<frame>')
def wado_root(study,serie,instance,frame):
    #wado root
    print("received study: "+study)
    #flask reverse proxy , https://medium.com/customorchestrator/simple-reverse-proxy-server-using-flask-936087ce0afb
    if request.method=='GET':
        argu=request.args.to_dict()
        r_argu=""
        #for key in argu.keys():
        #    r_argu =r_argu+ key+"="+argu[key]+'&'
        path='/dicom-web/studies/'+study+"/series/" + serie + "/instances/"+instance+"/frames/"+frame
        print("proxy to: "+ORTHANC+path)
        resp = requests.get(ORTHANC+path)
        response =resp.content
        print(resp.status_code,resp.headers)
    return Response(resp.content  , mimetype='application/dicom+json')

@app.route('/WADOuri')
def wadouri():
    return "wadouri"

#proxies_
@app.route('/dicom-web/studies',methods=['GET'])
def point1():
    #flask reverse proxy , https://medium.com/customorchestrator/simple-reverse-proxy-server-using-flask-936087ce0afb
    if request.method=='GET':
        argu=request.args.to_dict()
        r_argu=""
        for key in argu.keys():
            r_argu =r_argu+ key+"="+argu[key]+'&'
        path='/dicom-web/studies?'+r_argu
        print("proxy to: "+ORTHANC+path)
        resp = requests.get(ORTHANC+path)
        response =resp.content
        print(str(response),resp.status_code)
    return Response(resp.content  , mimetype='application/dicom+json')
   
if __name__ == '__main__':
    app_port = int(os.environ.get("PORT", 5000 ))
    app.run(host="0.0.0.0", debug=True, port=app_port, threaded=True )
