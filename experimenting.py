from tagging import url2
from utils import post_msg_llm
from prompts import get_choosing_prompt, get_summarize_words_prompt, req1, req2, get_summarize_article_prompt

url1 = "http://10.58.0.2:6677/v1/chat/completions"

check_out_article = "随着全球气候变化的加剧，环境保护已成为一个迫切的议题。减少碳排放、保护生物多样性和节约资源是我们面临的主要挑战。可再生能源的使用，如太阳能和风能，正在逐渐替代传统的化石燃料。此外，回收和再利用也成为减少环境污染的有效手段。每个人的一小步，如减少一次性塑料使用，都对保护我们的地球有着重要意义。"
check_out_list = "[\"环境保护\",\"修昔底德\",\"英雄联盟\",\"生物多样性\",\"黑暗之魂\",\"气候变化\",\"碳排放\",\"奥托大帝\",\"王者荣耀\",\"罗兰之歌\",\"哥伦布\",\"可再生能源\",\"伯罗奔尼撒\",\"回收再利用\",\"育碧\",\"减少塑料使用\",\"阿尔忒弥斯\",\"可持续能源转型\"]"


def experiment_1(input_text, input_list):
    intros1 = get_choosing_prompt(input_text, input_list)
    print(post_msg_llm("你好！", url2))
    print(intros1)
    # print("百川")
    # for i in range(10):
    #     print(post_msg(intros1, url1, temperature=0.1))

    print("GLM")
    for i in range(10):
        print(post_msg_llm(intros1, url2, temperature=0.7))


def experiment_2(input_text):
    intros2 = get_summarize_words_prompt(input_text)
    print(intros2)
    # print("百川")
    # for i in range(10):
    #     print(post_msg(intros2, url1, temperature=0.2))

    print("GLM")
    for i in range(10):
        print(post_msg_llm(intros2, url2))


def _0_shot():
    intros1 = f"{req1}\n" \
              f"输入文本：{check_out_article}\n" \
              f"输入list：{check_out_list}\n" \
              f"输出："
    print(intros1)
    # print(post_msg(intros1, url1))
    print(post_msg_llm(intros1, url2))

    intros2 = f"{req2}\n" \
              f"输入：{check_out_article}\n" \
              f"输出："

    print(intros2)
    # print(post_msg(intros2, url1))
    print(post_msg_llm(intros2, url2))


def experiment_3(text_in):
    intro3 = get_summarize_article_prompt(text_in)
    print(intro3)
    print(post_msg_llm(intro3, url2))


if __name__ == "__main__":
    # _0_shot()
    # experiment_1(check_out_article, check_out_list)
    # experiment_2(check_out_article)
    experiment_3(check_out_article)

