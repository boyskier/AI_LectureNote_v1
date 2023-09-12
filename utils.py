import openai
def split_text_into_paragraphs(text, max_length=800):
    paragraphs = []
    start = 0
    end = 0

    while start < len(text):
        # 800자 내에서 가장 마지막 온점 찾기
        end = start + max_length
        if end >= len(text):
            end = len(text)
        else:
            while end > start and text[end] not in '.!?':
                end -= 1
            # 온점, 물음표, 느낌표 중 하나를 찾았다면 그 뒷문자까지 포함
            end += 1

        paragraph = text[start:end].strip()
        paragraphs.append(paragraph)
        start = end

    return paragraphs

def correct_text(prompt, model="gpt-3.5-turbo"):
    instruction = f"""이상한 부분을 고친 버전을 줘"""

    messages = [
        {"role": "system",
         "content": instruction},  # instruction here
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def englished_text(prompt, subject='생리학', model="gpt-4"):
    # instruction = f"""{subject}용어만 영어로 바꾸고 나머지는 한국어를 유지한 버전을 줘."""
    instruction = f"""의학 용어들은 영어로 쓰고 다른 명사나 동사 등은 한글로 써서 고쳐줘"""
    messages = [
        {"role": "system",
         "content": instruction},  # instruction here
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]



def topic_splited_text(prompt, subject='생리학', model="gpt-4"):
    instruction = f"""주어진 문단을 적절히 2문단으로 쪼개줘"""
    messages = [
        {"role": "system",
         "content": instruction},  # instruction here
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]