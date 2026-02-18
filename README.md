### Electric Motor Temperature Prediction Using Machine Learning

This project aims to predict the temperature of an electric motor based on operational and environmental parameters. The solution helps in predictive maintenance, preventing overheating, and improving motor reliability in industrial systems.

By analyzing historical motor data, machine learning models were trained to accurately estimate motor temperature.


 ##  Project Demo Video

[Watch Demo Video](projectvideo.mp4)

## Project Demo Video

[Watch Demo Video](demo-video/project-demo.mp4)


## Team Details

| Role | Name |
|------|------|
| Team ID | LTVIP2026TMIDS74581 |
| Team Leader | Satya Siva Sai Ganesh Valluri |
| Team Member | Marise Radha Vaishnawe|
| Team Member | Velagala Jyothi Ayyappa Swarupa Reddy |
| Team Member | Kommanapalli Yeswanth Ganesh |

##  Project Structure
```


Electric-Motor-Temperature-Prediction/
│
├── dataset/
│   └── measures_v2.csv                      # Motor temperature dataset
│
├── notebooks/
│   ├── 01_data_loading.ipynb               # Data loading & exploration
│   ├── 03_data_preprocessing.ipynb         # Data cleaning & preprocessing
│   └── 04_model_building.ipynb             # Model training & evaluation
│
├── model/
│   └── motor_temperature_model.pkl         # Trained Random Forest model
│
├── Flask/
│   ├── templates/
│   │   └── index.html                      # Web input form page
│   ├── static/                             # (Optional CSS folder)
│   ├── app.py                              # Flask application file
│   ├── requirements.txt                    # Project dependencies
│   └── motor_temperature_model.pkl         # Model used by Flask
│
├── IBM_scoring_endpoint/                   # IBM deployment (optional)
│   └── (IBM related files)
│
└── README.md                               # Project documentation

```

##  Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python |
| ML Libraries | NumPy, Pandas, Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Model | Random Forest Regressor, Linear Regression |
| Web Framework | Flask |
| Environment | Jupyter Notebook |


##  Project Setup

### 1️ Clone the Repository

```bash
git clone https://github.com/yeswanthganesh/Electric-Motor-Temperature-Prediction.git
```

---

### 2️ Create & Activate Virtual Environment

```bash
python -m venv .venv
```

Activate:

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / Mac**
```bash
source .venv/bin/activate
```

---

### 3️ Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is missing, install manually:

```bash
pip install flask numpy pandas scikit-learn joblib matplotlib seaborn gunicorn
```

---

### 4️ Run Jupyter Notebooks (Model Training)

```bash
jupyter notebook
```

Open and execute:

- `01_data_loading.ipynb`
- `03_data_preprocessing.ipynb`
- `04_model_building.ipynb`

This will generate:

```
motor_temperature_model.pkl
```

---

### 5️ Run the Flask Application

Navigate to Flask folder:

```bash
cd Flask
```

Start the server:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

