# 🧑‍⚕️ Multiple Disease Prediction System

This web application uses machine learning models to predict the likelihood of **Diabetes**, **Heart Disease**, and **Parkinson's Disease** based on user input. It is built using **Python** and **Streamlit**, providing an intuitive and fast health risk assessment tool.

---

## 🚀 Demo

To run the app locally:

```bash
streamlit run app.py
````

---

## 📌 Features

* 🩸 **Diabetes Prediction**
* ❤️ **Heart Disease Detection**
* 🧠 **Parkinson's Disease Classification**
* ⚡ Real-time predictions using trained ML models
* 🖥️ Simple, clean, and responsive UI via Streamlit

---

## 📊 Models Used

The following machine learning algorithms were used to train disease classifiers:

* Logistic Regression
* Random Forest
* Support Vector Machine (SVM)

All models were trained on publicly available datasets, saved using `pickle`, and loaded in the app for real-time predictions.

---

## 🧠 Tech Stack

| Technology     | Role                    |
| -------------- | ----------------------- |
| Python         | Programming Language    |
| Streamlit      | Web Interface Framework |
| scikit-learn   | Machine Learning        |
| pandas / numpy | Data Processing         |
| pickle         | Model Serialization     |

---

## 🗂️ Project Structure

```
├── app.py                      # Main Streamlit app
├── saved_models/               # Directory for pre-trained models
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   └── parkinsons_model.sav
├── README.md                   # Project README
```

---

## 🛠️ Installation

Make sure you have Python 3.7 or above installed. Then, install the required packages:

```bash
pip install streamlit scikit-learn pandas numpy
```

To run the app:

```bash
streamlit run app.py
```

---

## 📚 Dataset Sources

* **Diabetes**: [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
* **Heart Disease**: [Heart Disease UCI Dataset](https://www.kaggle.com/datasets/ronitf/heart-disease-uci)
* **Parkinson’s Disease**: [Parkinson’s Dataset](https://www.kaggle.com/datasets/nidaguler/parkinsons-disease-dataset)

---

## 🤝 Contributing

Contributions are welcome!
If you have suggestions for improvements or find any bugs, feel free to open an issue or submit a pull request.

---

## 📝 License

This project is licensed under the **MIT License**.
Feel free to use and modify for personal or academic purposes.

