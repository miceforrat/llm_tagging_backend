import requests
import json

headers = {
    "Content-Type": "application/json",
}



def test_summarize_words_limit():
    url = "http://127.0.0.1:5000/summarize/words/limit_nums"
    data = {
        "content" : "人工智能是计算机科学的重要分支,旨在模拟、扩展和辅助人类智能。近年来,中国在政策扶持下的人工智能产业发展迅猛,成为全球人工智能产业的领导者之一。人工智能在医疗、教育、交通、工业生产等领域有广泛的应用,但同时也存在一些挑战,如就业压力、信息泄露风险和道德伦理问题。为此,需要加强对职业教育和培训的投入,建立健全的法律法规体系,引导企业和社会树立正确的价值观,确保人工智能技术的健康、可持续发展。未来,中国将继续加大人工智能领域的研究投入,推动人工智能技术与实体经济的深度融合,为全面建设社会主义现代化国家提供支撑。"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(response.text)


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


def test_summarize_article():
    url = "http://127.0.0.1:5000/summarize/article"
    data = {
        "content": "这款轻柔云端毛衣采用优质羊毛混纺面料，为您带来无与伦比的柔软和温暖。其经典的圆领设计，搭配时尚的宽松版型，既适合日常穿着，也可作为办公室的温馨选择。精致的编织工艺确保了毛衣的耐穿性，同时提供了舒适的贴身感觉。",
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(response.text)



if __name__ == "__main__":
    test_summarize_words_limit()
    # test_summarize_words()
    # test_tagging()
    # test_summarize_article()
