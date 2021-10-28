from flask import Flask,render_template,request
import requests
import pickle
import numpy as np
import sklearn

from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('file.pkl','rb'))

@app.route('/',methods=['GET'])
def Home(): 
  return render_template('index.html')  

standard_to = StandardScaler()

@app.route('/predict',methods = ['POST'])

def predict():
    Fuel_Type_Diesel =0
    if request.method == 'POST':
        year = int(request.form['Year'])
        mileage = int(request.form['mileage'])
        tax = float(request.form['Tax'])
        mpg = float(request.form['mpg'])
        engineSize = float(request.form['EngineSize'])
        trans = request.form['Transmission']
        if trans == 'Automatic':
            transmission_Automatic = 1
            transmission_Manual = 0
            transmission_Other = 0
            transmission_Semi_Auto = 0
        elif trans == 'Manual':
            transmission_Automatic = 0
            transmission_Manual = 1
            transmission_Other = 0
            transmission_Semi_Auto = 0
        elif trans == 'Other':
            transmission_Automatic = 0
            transmission_Manual = 0
            transmission_Other = 1
            transmission_Semi_Auto = 0
        elif trans == 'SemiAuto':
            transmission_Automatic = 0
            transmission_Manual = 0
            transmission_Other = 0
            transmission_Semi_Auto = 1
        
		
			
        fu = request.form['FuelType']
        if fu == 'Diesel':
            fuelType_Diesel = 1
            fuelType_Electric = 0
            fuelType_Hybrid = 0
            fuelType_Other = 0 
            fuelType_Petrol = 0
        elif fu == 'Electric':
            fuelType_Diesel = 0
            fuelType_Electric = 1
            fuelType_Hybrid = 0
            fuelType_Other = 0 
            fuelType_Petrol = 0
        elif fu == 'Hybrid':
            fuelType_Diesel = 0
            fuelType_Electric = 0
            fuelType_Hybrid = 1
            fuelType_Other = 0 
            fuelType_Petrol = 0
        elif fu == 'Other':
            fuelType_Diesel = 0
            fuelType_Electric = 0
            fuelType_Hybrid = 0
            fuelType_Other = 1
            fuelType_Petrol = 0
        elif fu == 'petrol':
            fuelType_Diesel = 0
            fuelType_Electric = 0
            fuelType_Hybrid = 0
            fuelType_Other = 0 
            fuelType_Petrol = 1
        ma = request.form['Make']
        if ma == 'BMW':
           ma_BMW = 1
           ma_Ford = 0
           ma_Hyundai = 0
           ma_Audi = 0
           ma_Skoda = 0
           ma_Toyota = 0
           ma_vw = 0
        elif ma == 'Ford':
           ma_BMW = 0
           ma_Ford = 1
           ma_Hyundai = 0
           ma_Audi = 0
           ma_Skoda = 0
           ma_Toyota = 0
           ma_vw = 0	
        elif ma == 'Hyundai':
           ma_BMW = 0
           ma_Ford = 0
           ma_Hyundai = 1
           ma_Audi = 0
           ma_Skoda = 0
           ma_Toyota = 0
           ma_vw = 0	
        elif ma == 'Audi':
           ma_BMW = 0
           ma_Ford = 0
           ma_Hyundai = 0
           ma_Audi = 1
           ma_Skoda = 0
           ma_Toyota = 0
           ma_vw = 0	
        elif ma == 'Skoda':
           ma_BMW = 0
           ma_Ford = 0
           ma_Hyundai = 0
           ma_Audi = 0
           ma_Skoda = 1
           ma_Toyota = 0
           ma_vw = 0	
        elif ma == 'Toyota':
           ma_BMW = 0
           ma_Ford = 0
           ma_Hyundai = 0
           ma_Audi = 0
           ma_Skoda = 0
           ma_Toyota = 1
           ma_vw = 0	
        elif ma == 'vw':
           ma_BMW = 0
           ma_Ford = 0
           ma_Hyundai = 0
           ma_Audi = 0
           ma_Skoda = 0
           ma_Toyota = 0
           ma_vw = 1	
        		   
        prediction = model.predict([[year,mileage,tax,mpg,engineSize,transmission_Automatic,transmission_Manual,transmission_Other,transmission_Semi_Auto,fuelType_Diesel,fuelType_Electric,fuelType_Hybrid,fuelType_Other,fuelType_Petrol,ma_BMW,ma_Ford,ma_Hyundai,ma_Audi,ma_Skoda,ma_Toyota,ma_vw]])
        output = round(prediction[0],2)
        if output < 0:
            return render_template('index.html',prediction_text='Sorry! Price cant be calculated')
        else:
            return render_template('index.html', prediction_text='The price is ${} '.format(output))
    else:
        return render_template('index.html')   
if __name__ == '__main__':
    app.run(debug=True)