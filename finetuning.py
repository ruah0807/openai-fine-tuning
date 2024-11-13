from init import *
import pandas as pd
import json

excel_file_path = "/Users/ruahkim/coding/ai-test/openai-fine-tuning/docs/44.음식분류_AI_데이터_영양DB.xlsx"


# 데이터셋 로드
# df = pd.read_excel(excel_file_path, engine="openpyxl")

# # # 데이터셋을 json 형식으로 변환하여 저장
# with open("health_food_data.jsonl", "w") as f:
#     for _, row in df.iterrows():
#         prompt = f"{row['음 식 명']}의 칼로리와 영양 정보를 알려주세요."

#         # completion에 영양 정보 포함한 응답 생성
#         completion = (
#             f"중량: {row['중량(g)']}g, 에너지: {row['에너지(kcal)']}kcal, "
#             f"탄수화물: {row['탄수화물(g)']}g, 당류: {row['당류(g)']}g, "
#             f"지방: {row['지방(g)']}g, 단백질: {row['단백질(g)']}g, "
#             f"칼슘: {row['칼슘(mg)']}mg, 나트륨: {row['나트륨(mg)']}mg, "
#             f"인: {row['인(mg)']}mg, 칼륨: {row['칼륨(mg)']}mg, "
#             f"마그네슘: {row['마그네슘(mg)']}mg, 철: {row['철(mg)']}mg, "
#             f"아연: {row['아연(mg)']}mg, 콜레스테롤: {row['콜레스테롤(mg)']}mg, "
#             f"트랜스지방: {row['트랜스지방(g)']}g"
#         )
#         chat_data = {
#             "messages": [
#                 {"role": "user", "content": prompt},
#                 {"role": "assistant", "content": completion},
#             ]
#         }
#         f.write(json.dumps(chat_data, ensure_ascii=False) + "\n")


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
if status.status == "succeeded":
    fine_tuned_model = status.fine_tuned_model
    print(f"fine_tuned model : {fine_tuned_model}")

    # 모델을 사용하여 예측 수행
    # 프롬프트 설정
    messages = [
        {
            "role": "user",
            "content": "당뇨환자가 식당에서 먹어도 되는 음식 종류를 골라주세요",
        }
    ]
    completion = openai.chat.completions.create(
        model=fine_tuned_model, messages=messages, max_tokens=300
    )
    print(f"Model Response : {completion.choices[0].message.content.strip()}")
