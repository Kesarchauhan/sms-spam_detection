<<<<<<< HEAD
# 📩 Explainable SMS Spam Detection using DistilBERT and LIME

An Explainable Artificial Intelligence (XAI) based SMS Spam Detection system built using a fine-tuned DistilBERT model and Local Interpretable Model-Agnostic Explanations (LIME).

This project demonstrates how transformer-based Natural Language Processing (NLP) models can be combined with explainability techniques to provide both accurate and interpretable spam classification.

---

## 🚀 Live Demo

Streamlit App: [Coming Soon]

---

## 🤗 Hugging Face Model

Model Repository:

https://huggingface.co/Kesar2020/SMS_Spam_Detection

---

## 📖 Project Overview

Spam messages remain a major challenge in digital communication. Traditional machine learning approaches often provide good performance but limited contextual understanding.

This project leverages DistilBERT, a lightweight transformer architecture, to classify SMS messages as:

- HAM (Legitimate Message)
- SPAM (Unwanted/Promotional Message)

To improve transparency and trustworthiness, LIME (Local Interpretable Model-Agnostic Explanations) is integrated to explain individual predictions.

---

## 🎯 Objectives

- Detect spam SMS messages with high accuracy.
- Fine-tune a transformer-based language model.
- Improve model interpretability using Explainable AI.
- Build a deployable web application for real-time predictions.

---

## 🧠 Technologies Used

### Machine Learning & NLP

- DistilBERT
- PyTorch
- Transformers (Hugging Face)

### Explainable AI

- LIME

### Deployment

- Streamlit
- Hugging Face Hub
- GitHub

### Data Processing

- Pandas
- NumPy
- Scikit-learn

---

## 📊 Dataset

SMS Spam Collection Dataset

The dataset contains labeled SMS messages categorized as:

- Ham
- Spam

The dataset is widely used for spam detection research and benchmarking.

---

## 🏗️ Methodology

### 1. Data Preprocessing

- Data cleaning
- Label encoding
- Train-test split

### 2. Model Fine-Tuning

A pre-trained DistilBERT model was fine-tuned on the SMS Spam Collection Dataset.

### 3. Prediction

The model predicts whether a given SMS is:

- HAM
- SPAM

along with a confidence score.

### 4. Explainability

LIME generates local explanations by identifying the words that contribute most to the model's prediction.

---

## 🔍 Explainable AI with LIME

LIME provides local explanations for individual predictions.

Example:

Input Message:

Congratulations! You have won a free iPhone. Click here now.

Prediction:

SPAM

LIME Explanation:

| Word | Contribution |
|--------|--------|
| free | Positive |
| won | Positive |
| Congratulations | Positive |
| Click | Positive |

This allows users to understand why the model reached its decision.

---

## 💻 Application Features

- SMS Classification
- Confidence Score
- LIME-based Explanation
- Interactive Streamlit Interface
- Hugging Face Hosted Model

---

## 📂 Project Structure

```text
SMS-Spam-Detection-XAI
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks
│   ├── Training.ipynb
│   └── XAI_Comparison.ipynb
│
└── assets
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/SMS-Spam-Detection-XAI.git

cd SMS-Spam-Detection-XAI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

- Comparative analysis with traditional machine learning models.
- Advanced explainability visualizations.
- Multi-language spam detection.
- Real-time API deployment.

---

## 🎓 Academic Context

This project was developed as part of a Bachelor of Science (Honours) in Computer Science dissertation focusing on:

**Explainable Artificial Intelligence (XAI) for NLP-based Spam Detection using Transformer Models**

The work explores the balance between predictive performance and interpretability in modern AI systems.

---

## 👤 Author

Kesar Chauhan

B.Sc. (Hons.) Computer Science

University of Delhi

---

## 📜 License

=======
# 📩 Explainable SMS Spam Detection using DistilBERT and LIME

An Explainable Artificial Intelligence (XAI) based SMS Spam Detection system built using a fine-tuned DistilBERT model and Local Interpretable Model-Agnostic Explanations (LIME).

This project demonstrates how transformer-based Natural Language Processing (NLP) models can be combined with explainability techniques to provide both accurate and interpretable spam classification.

---

## 🚀 Live Demo

Streamlit App: [Coming Soon]

---

## 🤗 Hugging Face Model

Model Repository:

https://huggingface.co/Kesar2020/SMS_Spam_Detection

---

## 📖 Project Overview

Spam messages remain a major challenge in digital communication. Traditional machine learning approaches often provide good performance but limited contextual understanding.

This project leverages DistilBERT, a lightweight transformer architecture, to classify SMS messages as:

- HAM (Legitimate Message)
- SPAM (Unwanted/Promotional Message)

To improve transparency and trustworthiness, LIME (Local Interpretable Model-Agnostic Explanations) is integrated to explain individual predictions.

---

## 🎯 Objectives

- Detect spam SMS messages with high accuracy.
- Fine-tune a transformer-based language model.
- Improve model interpretability using Explainable AI.
- Build a deployable web application for real-time predictions.

---

## 🧠 Technologies Used

### Machine Learning & NLP

- DistilBERT
- PyTorch
- Transformers (Hugging Face)

### Explainable AI

- LIME

### Deployment

- Streamlit
- Hugging Face Hub
- GitHub

### Data Processing

- Pandas
- NumPy
- Scikit-learn

---

## 📊 Dataset

SMS Spam Collection Dataset

The dataset contains labeled SMS messages categorized as:

- Ham
- Spam

The dataset is widely used for spam detection research and benchmarking.

---

## 🏗️ Methodology

### 1. Data Preprocessing

- Data cleaning
- Label encoding
- Train-test split

### 2. Model Fine-Tuning

A pre-trained DistilBERT model was fine-tuned on the SMS Spam Collection Dataset.

### 3. Prediction

The model predicts whether a given SMS is:

- HAM
- SPAM

along with a confidence score.

### 4. Explainability

LIME generates local explanations by identifying the words that contribute most to the model's prediction.

---

## 🔍 Explainable AI with LIME

LIME provides local explanations for individual predictions.

Example:

Input Message:

Congratulations! You have won a free iPhone. Click here now.

Prediction:

SPAM

LIME Explanation:

| Word | Contribution |
|--------|--------|
| free | Positive |
| won | Positive |
| Congratulations | Positive |
| Click | Positive |

This allows users to understand why the model reached its decision.

---

## 💻 Application Features

- SMS Classification
- Confidence Score
- LIME-based Explanation
- Interactive Streamlit Interface
- Hugging Face Hosted Model

---

## 📂 Project Structure

```text
SMS-Spam-Detection-XAI
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks
│   ├── Training.ipynb
│   └── XAI_Comparison.ipynb
│
└── assets
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/SMS-Spam-Detection-XAI.git

cd SMS-Spam-Detection-XAI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

- Comparative analysis with traditional machine learning models.
- Advanced explainability visualizations.
- Multi-language spam detection.
- Real-time API deployment.

---

## 🎓 Academic Context

This project was developed as part of a Bachelor of Science (Honours) in Computer Science dissertation focusing on:

**Explainable Artificial Intelligence (XAI) for NLP-based Spam Detection using Transformer Models**

The work explores the balance between predictive performance and interpretability in modern AI systems.

---

## 👤 Author

Kesar Chauhan

B.Sc. (Hons.) Computer Science

University of Delhi

---

## 📜 License

>>>>>>> 9b190ec59bc4fd3aaeca35d5cd90f5d9833da779
This project is intended for educational and research purposes.