
# inference.py

import os
import json
import time
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from configs.config import MODEL_NAME, CACHE_DIR, DATASET_NAME

def load_model_and_tokenizer(model_name, cache_dir):
    tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
    model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir, torch_dtype=torch.float16, device_map="auto")
    return model.eval(), tokenizer

def load_inputs(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [item["ctx"] + " " + item["endings"][0] for item in data[:10]]  # 10개 샘플만

def run_inference(model, tokenizer, inputs, device="cuda"):
    total_time = 0.0
    for text in inputs:
        input_ids = tokenizer(text, return_tensors="pt").to(device)
        start = time.time()
        _ = model.generate(**input_ids, max_new_tokens=50)
        end = time.time()
        total_time += (end - start)
    avg_time = total_time / len(inputs)
    print(f"total inference time per input: {total_time:.4f} seconds")
    print(f"Avg inference time per input: {avg_time:.4f} seconds")

if __name__ == "__main__":
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, tokenizer = load_model_and_tokenizer(MODEL_NAME, CACHE_DIR)
    input_path = os.path.join(CACHE_DIR, f"{DATASET_NAME}_val.json")
    inputs = load_inputs(input_path)
    run_inference(model, tokenizer, inputs, device=device)
