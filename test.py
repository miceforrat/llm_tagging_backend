import requests
import json
from testing_text import history_list, chemistry_list, math_list, food_list, clothing_list, game_list, se_list, ml_list, os_list, travelling_list, csdn_list
from summarizing import input_num

headers = {
    "Content-Type": "application/json",
}

GPT_TEXT_LIST = ["history_list", "chemistry_list", "math_list", "food_list", "clothing_list", "game_list", "se_list", "ml_list", "os_list", "travelling_list"]



def test_summarize_words_limit_or_not(list, index):
    print("原始文本：" + list[index])
    print("原始文本长度：" + str(input_num(list[index])))
    url = "http://127.0.0.1:5000/summarize/words"
    url_limit = "http://127.0.0.1:5000/summarize/words/limit_nums"
    data = {
        "content" : list[index]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    response_limit = requests.post(url_limit, headers=headers, data=json.dumps(data), verify=False)
    print("没有数量限制的tag：" + response.text)
    print("有数量限制的tag：" + response_limit.text + "\n")



def test_summarize_words_limit():
    url = "http://127.0.0.1:5000/summarize/words/limit_nums"
    data = {
        "content" : "人工智能作为战略性新兴产业，在我国发展迅速，其在医疗、教育、交通等多领域的应用日益广泛，但也存在就业挑战、信息安全和伦理问题等挑战，需要加强法律法规和职业教育投入，引导企业和社会健康发展的同时，为我国经济社会发展提供有力支撑。"
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
    # for list in GPT_TEXT_LIST:
    #     print(list)
    #     cur_list = locals()[list]
    #     for i in range(0, len(cur_list)):
    #         test_summarize_words_limit_or_not(cur_list, i)
    #     print()

    for i in range(0, len(csdn_list)):
        test_summarize_words_limit_or_not(csdn_list, i)

    # test_summarize_words_limit()
    # test_summarize_words()
    # test_tagging()
    # test_summarize_article()
