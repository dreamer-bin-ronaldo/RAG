import requests

# API 配置
API_URL = "http://localhost:3001/api/v1/workspace/new"
API_KEY = "S4VHQZK-9WW4PVQ-HR0DJ8Y-462H32P"  # 替换为您的 API 密钥

headers = {
    "Accept": "application/json",
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

# 发送请求创建工作区
response = requests.post(API_URL, json=workspace_data, headers=headers)

# 处理响应
if response.status_code == 200:
    workspace_info = response.json()
    workspace_id = workspace_info['workspace']['id']
    print("Workspace created successfully:", workspace_info)
    
    # 上传文档
    document_data = {
        "workspaceId": workspace_id,
        "document": {
            "title": "My Document",
            "content": "这是我的文档内容，包含一些有用的信息。"
        }
    }

    document_url = "http://localhost:3001/api/v1/workspace/{workspace_id}/document/upload"  # 替换为文档上传 API URL
    document_response = requests.post(document_url, json=document_data, headers=headers)

    if document_response.status_code == 200:
        print("Document uploaded successfully:", document_response.json())
    else:
        print("Error uploading document:", document_response.status_code, document_response.text)

    # 向 AnythingLLM 提问并获取答案
    def ask_question(question):
        question_data = {
            "workspaceId": workspace_id,
            "query": question
        }

        qa_url = "http://localhost:3001/api/v1/query"  # 替换为问答 API URL
        qa_response = requests.post(qa_url, json=question_data, headers=headers)

        if qa_response.status_code == 200:
            return qa_response.json().get("answer")
        else:
            print("Error asking question:", qa_response.status_code, qa_response.text)
            return None

    # 示例：询问问题
    question = "文档中提到了哪些关键信息？"
    answer = ask_question(question)
    if answer:
        print("Answer:", answer)

else:
    print("Error creating workspace:", response.status_code, response.text)
