from init import *
import pandas as pd
import json, time


file_path = (
    "/Users/ruahkim/coding/ai-test/openai-fine-tuning/docs/health_food_data.jsonl"
)

# json파일 검증
df_jsonl = pd.read_json(
    file_path,
    lines=True,
)

# 데이터셋 업로드
# response = openai.files.create(file=open(file_path, "rb"), purpose="fine-tune")

# 파인튜닝 작업 id 확인
# file_id = response.id
# print(f"Uploaded file ID: {file_id}")
file_id = "file-file-qGjAqVzbmSj4eFRD6m4xRxw0"
# 파일 삭제
# openai.files.delete(file_id=file_id)

# 파인튜닝 작업생성
# fine_tune_response = openai.fine_tuning.jobs.create(
#     training_file=file_id, model="gpt-3.5-turbo"
# )

# 파인튜닝 아이디 확인
# fine_tune_id = fine_tune_response.id
# print(f"find_tuning_job_id: {fine_tune_id}")

fine_tune_id = "ftjob-e6ohdQ1kMpGiIOfObsyyZyif"

# 파인튜닝 상태 모니터링
status = openai.fine_tuning.jobs.retrieve(fine_tuning_job_id=fine_tune_id)
print(f"fine-tune status : {status.status}")

# 파인튜닝 완료 후 모델 사용
while status.status == "running" or status.status == "succeeded":
    fine_tuned_model = status.fine_tuned_model
    print(f"fine_tuned model : {fine_tuned_model}")
    time.sleep(1)
    # 모델을 사용하여 예측 수행
    prompt = "면역력에 좋은 음식 추천해주세요."
    completion = openai.completions.create(
        model=fine_tune_id, prompt=prompt, max_tokens=200
    )
    print(f"Model Response : {completion.choices[0].text.strip()}")
