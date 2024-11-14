from init import *
import pandas as pd
import json


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
file_id = "file-qGjAqVzbmSj4eFRD6m4xRxw0"
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
if status.status == "succeeded":
    fine_tuned_model = status.fine_tuned_model
    print(f"fine_tuned model : {fine_tuned_model}")

    # 모델을 사용하여 예측 수행
    # 프롬프트 설정
    messages = [
        {
            "role": "user",
            # "content": "당뇨환자가 식당에서 먹어도 되는 음식 종류를 골라주세요",
            "content": "비빔밥의 영양성분은 어떻게 되나요?",
        }
    ]
    completion = openai.chat.completions.create(
        model=fine_tuned_model, messages=messages, max_tokens=500, temperature=0.98
    )
    print(f"Model Response : {completion.choices[0].message.content.strip()}")

# Model Response : 중탄고지 식단 영양소비율 기준에 따르면 한 그릇(510.5g)의 비빔밥 영양성분은 에너지 650.62kcal, 탄수화물 121.04399999999998g, 당류 7.819g, 지방 10.388000000000002g, 단백질 19.795999999999994g, 칼슘 65.89999999999999mg, 나트륨 1328.93mg, 인 321.23mg, 칼륨 606.6mg, 마그네슘 32.375mg, 철 4.669999999999999mg, 아연 2.8935mg, 콜레스테롤 22.08mg, 트랜스지방 0g  입니다. 부엌에서 조리한 7,000여종의 식품 중 영양가가 높습니다.
