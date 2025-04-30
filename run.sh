#!/bin/bash
set -e

echo "[INFO] Preprocessing started..."
python preprocess.py

echo "[INFO] Inference started..."
python inference.py > /logs/inference_result.log 2>&1

echo "[INFO] Done. Log saved to /logs/inference_result.log"
