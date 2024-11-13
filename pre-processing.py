import pandas as pd
import json, time

excel_file_path = "/Users/ruahkim/coding/ai-test/openai-fine-tuning/docs/44.음식분류_AI_데이터_영양DB.xlsx"


# 데이터셋 로드
df = pd.read_excel(excel_file_path, engine="openpyxl")

# # 데이터셋을 json 형식으로 변환하여 저장
with open("health_food_data.jsonl", "w") as f:
    for _, row in df.iterrows():
        prompt = f"{row['음 식 명']}의 칼로리와 영양 정보를 알려주세요."

        # completion에 영양 정보 포함한 응답 생성
        completion = (
            f"중량: {row['중량(g)']}g, 에너지: {row['에너지(kcal)']}kcal, "
            f"탄수화물: {row['탄수화물(g)']}g, 당류: {row['당류(g)']}g, "
            f"지방: {row['지방(g)']}g, 단백질: {row['단백질(g)']}g, "
            f"칼슘: {row['칼슘(mg)']}mg, 나트륨: {row['나트륨(mg)']}mg, "
            f"인: {row['인(mg)']}mg, 칼륨: {row['칼륨(mg)']}mg, "
            f"마그네슘: {row['마그네슘(mg)']}mg, 철: {row['철(mg)']}mg, "
            f"아연: {row['아연(mg)']}mg, 콜레스테롤: {row['콜레스테롤(mg)']}mg, "
            f"트랜스지방: {row['트랜스지방(g)']}g"
        )
        chat_data = {
            "messages": [
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": completion},
            ]
        }
        f.write(json.dumps(chat_data, ensure_ascii=False) + "\n")
