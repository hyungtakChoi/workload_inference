# workload_inference
worldclass project workload definition about inference

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
