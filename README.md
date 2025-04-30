# workload_inference
worldclass project workload definition about inference
   
# 워크로드 정의 표
워크로드 수행 시 `configs/config.py` 를 수정합니다. 모델 이름, 추론 데이터셋을 지정합니다.   아래 표를 제공합니다.   

|모델|데이터 출처|설명|
|:------:|:---:|:---:|
|[meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)|[Hellaswag](https://huggingface.co/datasets/Rowan/hellaswag)|상식 추론 과제용 데이터셋|
|[mistralai/Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)|[TruthfulQA](https://huggingface.co/datasets/domenicrosati/TruthfulQA)|거짓 정보 없이 답하는지 평가|
|[codellama/CodeLlama-7b-Instruct-hf](https://huggingface.co/codellama/CodeLlama-7b-Instruct-hf)|[HumanEval](https://huggingface.co/datasets/openai/openai_humaneval)|코드 정답률 평가|


# 워크로드 실행 방식
워로드는 docker, shell 두 방식을 활용합니다.   

1. dockerfile 을 build 한 후 실행하여 logs 파일을 확인합니다.
```
docker build -t ai-workload-infer .
docker run --gpus all -v $(pwd)/logs:/logs ai-workload-infer
```
      
2. run.sh 를 실행합니다.
```
./run.sh
```
