import requests
from datetime import datetime

# 从外部配置文件读取密钥（不暴露在公开仓库中）
try:
    from config import API_KEY, API_URL
except ImportError:
    print("❌ 错误：找不到 config.py 文件")
    print("👉 请复制 config.example.py 并重命名为 config.py，然后填入你的 API Key")
    exit(1)

def generate_video_script(topic):
    print(f"🎬 正在为主题 [{topic}] 生成脚本...")
    system_prompt = "你是一个专业的短视频编剧。请输出包含标题、关键词、三段式脚本的Markdown内容。"
    user_prompt = f"主题：{topic}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "model": "moonshot-v1-8k",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.8,
        "stream": False
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        print(f"🔍 HTTP 状态码: {response.status_code}")
        print(f"🔍 响应前100字符: {response.text[:100]}")
        response.raise_for_status()
        data = response.json()
        content = data['choices'][0]['message']['content']
        print("✅ 生成成功！")
        return content
    except Exception as e:
        print(f"❌ 出错了: {e}")
        if 'response' in locals():
            print(f"🔍 完整响应内容: {response.text}")
        return f"【备用】{topic} 生成失败。"

def save_script_to_file(topic, content):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_topic = "".join(c for c in topic if c.isalnum() or c in (' ', '-', '_')).rstrip()
    filename = f"{safe_topic}_{timestamp}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# 视频脚本\n生成时间：{datetime.now()}\n\n{content}")
    print(f"📁 脚本已保存至: {filename}")

print("脚本加载完毕，准备执行 main。")

if __name__ == "__main__":
    print("==== 简易视频脚本生成工具 ====")
    topic = "面试中如何展示项目经验"
    script = generate_video_script(topic)
    save_script_to_file(topic, script)
    print("🎉 流程执行完毕。")