import requests
import json

headers = {
    "Content-Type": "application/json",
}


def test_summarize_words():
    url = "http://127.0.0.1:5000/summarize/words"
    data = {
        "content": "这款轻柔云端毛衣采用优质羊毛混纺面料，为您带来无与伦比的柔软和温暖。其经典的圆领设计，搭配时尚的宽松版型，既适合日常穿着，也可作为办公室的温馨选择。精致的编织工艺确保了毛衣的耐穿性，同时提供了舒适的贴身感觉。"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(response.text)


def test_tagging():
    url = "http://127.0.0.1:5000/tagging"
    data = {
        "content": "这款轻柔云端毛衣采用优质羊毛混纺面料，为您带来无与伦比的柔软和温暖。其经典的圆领设计，搭配时尚的宽松版型，既适合日常穿着，也可作为办公室的温馨选择。精致的编织工艺确保了毛衣的耐穿性，同时提供了舒适的贴身感觉。",
        "words": ["羽绒服", "食物", "鹅绒", "羊毛", "运动", "毛衣", "长裤", "混纺面料", "精致编织工艺"]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(response.text)


if __name__ == "__main__":
    test_summarize_words()
    test_tagging()

