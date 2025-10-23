from openai import OpenAI
import os
from dotenv import load_dotenv

# 载入 .env 文件里的 API key
load_dotenv()

# 初始化 OpenAI 客户端
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 测试模型：GPT-5-Nano
response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that summarizes text."},
        {"role": "user", "content": "Summarize what the EPLC Development Phase focuses on in one sentence."}
    ]
)

# 输出模型返回的结果
print("Model Output:")
print(response.choices[0].message.content)