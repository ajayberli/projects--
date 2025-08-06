from flask import Flask ,render_template,request,url_for
import joblib
app =Flask(__name__)

def home():
    return render_template('index.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project')
def predict():
  if request.method=='post'
  brand_name=request.form['brand_name']
  owner= request.form['owner']
  age= request.form['age']
  power=request.form['power']
  kms_driven=request.form['kms_driven']
  print("output>>>>>>",brand_name,owner,age,power,kms_driven)
  return render_template('project.html')




  if __name__=="__main__":
    app.run(debug =True)
print(__name__)