from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model and columns
model = pickle.load(open('model.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Create array of zeros
        query = np.zeros(len(columns))

        # 2. Extract continuous features
        ram = int(request.form.get('ram'))
        weight = float(request.form.get('weight'))
        touchscreen = int(request.form.get('touchscreen'))
        ips = int(request.form.get('ips'))
        cpu_speed = float(request.form.get('cpu_speed'))
        ssd = int(request.form.get('ssd'))
        hdd = int(request.form.get('hdd'))

        # --- PPI CALCULATION ---
        inches = float(request.form.get('inches'))
        resolution = request.form.get('resolution')
        x_res = int(resolution.split('x')[0])
        y_res = int(resolution.split('x')[1])
        ppi = ((x_res**2 + y_res**2)**0.5) / inches

        # Assign values
        query[columns.index('Ram')] = ram
        query[columns.index('Weight')] = weight
        query[columns.index('Touchscreen')] = touchscreen
        query[columns.index('IPS')] = ips
        query[columns.index('ppi')] = ppi 
        query[columns.index('Cpu_speed')] = cpu_speed
        query[columns.index('SSD')] = ssd
        query[columns.index('HDD')] = hdd

        # 3. Handle Categorical features
        categorical_features = {
            'Company': request.form.get('company'),
            'TypeName': request.form.get('typename'),
            'OpSys': request.form.get('opsys'),
            'Cpu_brand': request.form.get('cpu_brand'),
            'Gpu_brand': request.form.get('gpu_brand'),
            'Screen_Type': request.form.get('screen_type')
        }

        for prefix, value in categorical_features.items():
            column_name = f"{prefix}_{value}"
            if column_name in columns:
                query[columns.index(column_name)] = 1

        # 4. Predict
        prediction = model.predict(query.reshape(1, -1))[0]
        
        # Calculate Currencies
        price_eur = round(np.exp(prediction), 2)
        price_usd = round(price_eur * 1.08, 2)  # Approx EUR to USD
        price_inr = round(price_eur * 90.50, 2) # Approx EUR to INR

        # Pass all three to the frontend
        return render_template('index.html', eur=price_eur, usd=price_usd, inr=price_inr)

    except Exception as e:
        return render_template('index.html', error=f"Error processing input: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
