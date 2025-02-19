import requests

# API 配置
API_URL = "http://localhost:3001/api/v1/workspace/new"
API_KEY = "S4VHQZK-9WW4PVQ-HR0DJ8Y-462H32P"  # 替换为您的 API 密钥

headers = {
    "Accept": "application/json",  # 正确的写法
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 创建工作区的数据
workspace_data = {
    "name": "My New Workspace",
    "similarityThreshold": 0.7,
    "openAiTemp": 0.7,
    "openAiHistory": 20,
    "openAiPrompt": "Custom prompt for responses",
    "queryRefusalResponse": "Custom refusal message",
    "chatMode": "chat",
    "topN": 4
}

# 发送请求
response = requests.post(API_URL, json=workspace_data, headers=headers)

# 处理响应
if response.status_code == 200:
    print("Workspace created successfully:", response.json())
else:
    print("Error creating workspace:", response.status_code, response.text)
