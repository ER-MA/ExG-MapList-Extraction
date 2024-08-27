import requests
import json
from datetime import datetime, timedelta


# 获取原始的CurrentCs2MapStatus数据（未经处理的json格式“当前CS2地图状态”）
def get_current_exg_map_status():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }
    request_url = "https://list.darkrp.cn:9000/ServerList/CurrentCs2MapStatus"  # 当前ExG地图状态文档的请求地址
    map_status_doc = requests.get(request_url, headers=headers)  # Get文档并暂存
    return map_status_doc.json()


# 将Difficulty由数值转换为文字
def get_difficulty_name(n):
    difficulties = ["简单", "普通", "困难", "极难", "史诗", "梦魇", "绝境"]
    return difficulties[n] if 0 <= n < len(difficulties) else n


# 格式化CooldownMinute（与官网方式处理相同）
def format_minute(n):
    if n < 180:
        return f"{n:.0f}分"
    elif n < 4320:
        return f"{n / 60:.1f}时"
    else:
        return f"{n / 1440:.1f}天"


# 对原始的CurrentCs2MapStatus数据进行预处理，转为可阅读的json格式数据
def preprocess_data(json_data):
    now = datetime.now()
    processed_data = []

    for info in json_data:
        last_run_datetime = datetime.strptime(info["LastRun"], "%Y-%m-%dT%H:%M:%S")
        cooldown_end = last_run_datetime + timedelta(minutes=info["CooldownMinute"])
        cooldown_str = cooldown_end.strftime("%Y-%m-%d %H:%M:%S") if cooldown_end > now else "无"

        processed_info = {
            "Name": info["Name"],
            "CnName": info["CnName"],
            "Difficulty": get_difficulty_name(info["Difficulty"]),
            "CooldownMinute": format_minute(info["CooldownMinute"]),
            "CooldownEnd": cooldown_str,
            "Steam": info["Steam"]
        }
        processed_data.append(processed_info)

    return json.dumps(processed_data, ensure_ascii=False)

