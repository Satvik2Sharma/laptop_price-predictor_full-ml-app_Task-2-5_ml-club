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
        # 1. Create an array of zeros matching the number of features (45)
        query = np.zeros(len(columns))

        # 2. Extract continuous features from the form
        ram = int(request.form.get('ram'))
        weight = float(request.form.get('weight'))
        touchscreen = int(request.form.get('touchscreen'))
        ips = int(request.form.get('ips'))
        cpu_speed = float(request.form.get('cpu_speed'))
        ssd = int(request.form.get('ssd'))
        hdd = int(request.form.get('hdd'))

        # --- NEW PPI CALCULATION LOGIC ---
        # We catch the new user-friendly inputs from the dark theme HTML
        inches = float(request.form.get('inches'))
        resolution = request.form.get('resolution')
        
        # Split "1920x1080" into X (1920) and Y (1080)
        x_res = int(resolution.split('x')[0])
        y_res = int(resolution.split('x')[1])
        
        # Calculate the PPI dynamically for the ML model
        ppi = ((x_res**2 + y_res**2)**0.5) / inches
        # ---------------------------------

        # Assign values to the correct slots in the array
        query[columns.index('Ram')] = ram
        query[columns.index('Weight')] = weight
        query[columns.index('Touchscreen')] = touchscreen
        query[columns.index('IPS')] = ips
        query[columns.index('ppi')] = ppi # The model still gets the PPI it needs!
        query[columns.index('Cpu_speed')] = cpu_speed
        query[columns.index('SSD')] = ssd
        query[columns.index('HDD')] = hdd

        # 3. Handle Categorical features via string matching
        categorical_features = {
            'Company': request.form.get('company'),
            'TypeName': request.form.get('typename'),
            'OpSys': request.form.get('opsys'),
            'Cpu_brand': request.form.get('cpu_brand'),
            'Gpu_brand': request.form.get('gpu_brand'),
            'Screen_Type': request.form.get('screen_type')
        }

        # Find the one-hot column name and set its index to 1
        for prefix, value in categorical_features.items():
            column_name = f"{prefix}_{value}"
            if column_name in columns:
                query[columns.index(column_name)] = 1

        # 4. Predict
        prediction = model.predict(query.reshape(1, -1))[0]
        
        # Reverse the log transformation using np.exp
        final_price = round(np.exp(prediction), 2)

        return render_template('index.html', result=f"Estimated Price: €{final_price}")

    except Exception as e:
        return render_template('index.html', result=f"Error processing input: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
