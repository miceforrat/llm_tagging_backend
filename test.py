import requests
import json
from testing_text import history_list, chemistry_list, math_list, food_list, clothing_list, game_list, se_list, ml_list, os_list, travelling_list, csdn_list, little_red_book_list
from summarizing import input_num
import random

headers = {
    "Content-Type": "application/json",
}

GPT_TEXT_LIST = ["history_list", "chemistry_list", "math_list", "food_list", "clothing_list", "game_list", "se_list", "ml_list", "os_list", "travelling_list"]
tag_list = ["历史", "化学", "数学", "食物", "服装", "游戏", "学术诚信", "旅游景点"]


def test_summarize_words_limit_or_not(list, index):
    print("原始文本：" + list[index])
    print("原始文本长度：" + str(input_num(list[index])))
    url = "http://127.0.0.1:5000/summarize/words"
    url_limit = "http://127.0.0.1:5000/summarize/words/limit_nums"
    data = {
        "content": list[index]
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


def test_tagging(list, index, tag_list):
    url = "http://127.0.0.1:5000/tagging"
    data = {
        "content": '''
        对于大作业，最重要的一件事就是不要抄袭！我们会通过检查 git 提交记录、代码查重等方式判断你是否有抄袭的嫌疑。对于被判定为抄袭的同学，我们将会私下约你进行面查并根据结果作出相应的惩罚（如根据情况严重程度扣除一个 Lab 的分数或全部大作业分数）。
关于代码查重的识别能力，请参见 《代码抄袭：那些让985学生沉默，211学生流泪的真相》。
请注意，并不只有抄袭别人的代码才是违背学术诚信的行为。更多请参见 MIT 对于学术诚信的定义。
    ''',
        "words": tag_list
    }
    # print("原始文本：" + list[index])
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(response.text)


def test_tagging_score(list, index, tag_list):
    url = "http://127.0.0.1:5000/tagging/score"
    data = {
        "content": list[index],
        "words": tag_list
    }
    print("原始文本：" + list[index])
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(response.text)


def test_summarize_article(list, index):
    url = "http://127.0.0.1:5000/summarize/article"
    data = {
        "content": list[index],
    }
    print("原始文本：" + list[index])
    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(response.text)


if __name__ == "__main__":  
    # for list in GPT_TEXT_LIST:
    #     print(list)
    #     cur_list = locals()[list]
    #     for i in range(0, len(cur_list)):
    #         test_summarize_words_limit_or_not(cur_list, i)
    #     print()

    # for i in range(0, len(travelling_list)):
    #     test_tagging(travelling_list, i, tag_list)

    test_tagging(travelling_list, 0, tag_list)

    # random_list = []
    # for list in GPT_TEXT_LIST:
    #     cur_list = locals()[list]
    #     random_list.extend(cur_list)
    # random.shuffle(random_list)
    # for i in range(0, len(random_list)):
    #     test_tagging_score(random_list, i, tag_list)
    #     test_tagging(random_list, i, tag_list)

    # test_summarize_words_limit()
    # test_summarize_words()
    # test_tagging()
    # test_summarize_article()
