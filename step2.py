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
    
    # 读取当前文件夹下的 test.txt 文件内容
    try:
        with open("test.txt", "r", encoding="utf-8") as file:
            file_content = file.read()
    except FileNotFoundError:
        print("Error: test.txt file not found in the current directory.")
        exit()

    # 上传文档
    document_data = {
        "workspaceId": workspace_id,
        "document": {
            "title": "My Document",
            "content": file_content  # 将文件内容作为文档内容
        }
    }

    document_url = f"http://localhost:3001/api/v1/workspace/{workspace_id}/document/upload"
    document_response = requests.post(document_url, json=document_data, headers=headers)

    if document_response.status_code == 200:
        print("Document uploaded successfully:", document_response.json())
    else:
        print("Error uploading document:", document_response.status_code, document_response.text)

else:
    print("Error creating workspace:", response.status_code, response.text)
