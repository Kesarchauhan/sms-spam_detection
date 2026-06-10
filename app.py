import streamlit as st
import torch
import pandas as pd
import numpy as np

from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

from lime.lime_text import LimeTextExplainer

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Explainable SMS Spam Detection",
    page_icon="📩",
    layout="wide"
)

# =====================================================
# MODEL CONFIG
# =====================================================

MODEL_PATH = "Kesar2020/SMS_Spam_Detection"

# =====================================================
# LOAD MODEL
# =====================================================

@st.cache_resource
def load_model():

    tokenizer = DistilBertTokenizerFast.from_pretrained(
        MODEL_PATH
    )

    model = DistilBertForSequenceClassification.from_pretrained(
        MODEL_PATH
    )

    model.eval()

    return tokenizer, model

tokenizer, model = load_model()

# =====================================================
# LIME EXPLAINER
# =====================================================

explainer = LimeTextExplainer(
    class_names=["Ham", "Spam"]
)

# =====================================================
# PREDICTION FUNCTION FOR LIME
# =====================================================

def predict_proba_distilbert(texts):

    inputs = tokenizer(
        texts,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():

        outputs = model(**inputs)

        probs = torch.softmax(
            outputs.logits,
            dim=1
        )

    return probs.cpu().numpy()

# =====================================================
# HEADER
# =====================================================

st.title("📩 Explainable SMS Spam Detection")

st.markdown("""
This application detects whether an SMS message is **Spam** or **Ham**
using a fine-tuned DistilBERT model and provides explanations using
**LIME (Local Interpretable Model-Agnostic Explanations)**.
""")

# =====================================================
# TABS
# =====================================================

tab1, tab2 = st.tabs(
    ["Detector", "About"]
)

# =====================================================
# DETECTOR TAB
# =====================================================

with tab1:

    if "sms_text" not in st.session_state:
        st.session_state.sms_text = ""

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📛 Load Spam Example"):

            st.session_state.sms_text = (
                "Congratulations! "
                "You have won a free iPhone. "
                "Click here now."
            )

            st.rerun()

    with col2:

        if st.button("✅ Load Ham Example"):

            st.session_state.sms_text = (
                "Hey, are we meeting at 4 PM today?"
            )

            st.rerun()

    sms_text = st.text_area(
        "Enter SMS Message",
        key="sms_text",
        height=180,
        placeholder="Type or paste an SMS message..."
    )

    if st.button("🔍 Analyze Message"):

        if sms_text.strip() == "":

            st.warning(
                "Please enter an SMS message."
            )

        else:

            inputs = tokenizer(
                sms_text,
                return_tensors="pt",
                truncation=True,
                padding=True,
                max_length=128
            )

            with torch.no_grad():

                outputs = model(**inputs)

            probs = torch.softmax(
                outputs.logits,
                dim=1
            )

            prediction = torch.argmax(
                probs,
                dim=1
            ).item()

            confidence = probs[0][prediction].item()

            label = (
                "SPAM"
                if prediction == 1
                else "HAM"
            )

            st.divider()

            st.subheader("Prediction Result")

            if prediction == 1:

                st.error(
                    f"🚨 Prediction: {label}"
                )

            else:

                st.success(
                    f"✅ Prediction: {label}"
                )

            st.metric(
                "Confidence",
                f"{confidence*100:.2f}%"
            )

            st.divider()

            generate_lime = st.checkbox(
                "Generate LIME Explanation"
            )

            if generate_lime:

                st.subheader(
                    "🔍 Explainability (LIME)"
                )

                with st.spinner(
                    "Generating explanation..."
                ):

                    explanation = (
                        explainer.explain_instance(
                            sms_text,
                            predict_proba_distilbert,
                            num_features=8,
                            num_samples=30
                        )
                    )

                    explanation_df = pd.DataFrame(
                        explanation.as_list(),
                        columns=[
                            "Word",
                            "Importance"
                        ]
                    )

                    st.dataframe(
                        explanation_df,
                        use_container_width=True
                    )

                    st.bar_chart(
                        explanation_df.set_index(
                            "Word"
                        )
                    )

                st.info(
                    """
                    LIME highlights the words that most influenced
                    the model's prediction for this specific SMS.
                    """
                )

# =====================================================
# ABOUT TAB
# =====================================================

with tab2:

    st.header("About This Project")

    st.markdown("""
### Model

- DistilBERT
- Fine-tuned for SMS Spam Detection

### Explainability

- LIME (Local Interpretable Model-Agnostic Explanations)

### Dataset

- SMS Spam Collection Dataset

### Labels

- HAM = Legitimate Message
- SPAM = Unwanted / Fraudulent Message

### Research Context

This project was developed as part of a dissertation on
Explainable Artificial Intelligence (XAI) and Natural Language Processing (NLP).

The objective was to combine the predictive power of transformer-based models
with explainability techniques to improve transparency and trust in AI systems.
""")
