from flask import Flask,render_template,request
import pandas as pd
from src.data_preprocessing import preprocess
from src.prediction import prediction
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def main():
    if request.method == 'POST':
        area_sqft=int(request.form['area_sqft'])
        bedrooms=int(request.form['bedrooms'])
        bathrooms=int(request.form['bathrooms'])
        age_of_house=int(request.form['age_of_house'])
        distance_from_city=int(request.form['distance_from_city'])
        dict = {'Area_sqft': [area_sqft], 'Bedrooms': [bedrooms], 'Bathrooms': [bathrooms],
                'Age_of_house': [age_of_house], 'Distance_from_city_km': [distance_from_city]}
        df = pd.DataFrame(dict)
        pp_df = preprocess(df)
        predicted_price_array = prediction(pp_df)
        predicted_price=float(predicted_price_array[0])
        predicted_price=round(predicted_price,2)
        return render_template('final.html', predicted_price=predicted_price)
    else:
        return render_template('form.html')
@app.route('/res')
def result():
    return render_template('final.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)