
# preprocess.py

import os
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset
from configs.config import MODEL_NAME, DATASET_NAME, CACHE_DIR

def download_model(model_name, cache_dir):
    print(f"Downloading model: {model_name}")
    AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
    AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir)

def download_dataset(dataset_name, cache_dir):
    print(f"Downloading dataset: {dataset_name}")
    dataset = load_dataset(dataset_name, split="validation", cache_dir=cache_dir)
    dataset.to_json(os.path.join(cache_dir, f"{dataset_name}_val.json"))

if __name__ == "__main__":
    os.makedirs(CACHE_DIR, exist_ok=True)
    download_model(MODEL_NAME, CACHE_DIR)
    download_dataset(DATASET_NAME, CACHE_DIR)
