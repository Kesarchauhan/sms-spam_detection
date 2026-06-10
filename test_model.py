from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification
)

MODEL_PATH = "Kesar2020/SMS_Spam_Detection"

tokenizer = DistilBertTokenizerFast.from_pretrained(
    MODEL_PATH
)

model = DistilBertForSequenceClassification.from_pretrained(
    MODEL_PATH
)

print("Model Loaded Successfully!")