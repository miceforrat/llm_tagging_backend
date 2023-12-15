example_1 = "人工智能正在逐渐改变我们的生活。从智能手机助手到自动驾驶汽车，AI技术的应用无处不在。它不仅提高了工作效率，还为我们带来了前所未有的便利。然而，随着技术的进步，我们也面临着伦理和隐私的挑战。如何平衡利益与风险，是我们必须深入思考的问题。"
tag_list1 = "[\"人工智能\",\"技术应用\",\"医疗\",\"伦理\",\"游戏\",\"隐私\",\"大数据科学\",\"军事\",\"交易\"]"
ans_tag1 = "[\"人工智能\",\"技术应用\",\"伦理\",\"隐私\"]"
ans_tag1_limit = "[\"人工智能\",\"技术应用\",\"伦理\"]"
to_score_tag1 = "[\"人工智能\",\"技术应用\",\"医疗\",\"伦理\",\"游戏\",\"隐私\",\"军事\",\"交易\"]"
score_list1 = "{'人工智能':99, '技术应用':98, '医疗':27, '伦理':90, '游戏':16, '隐私':93, '军事':28, '交易':27 }"
modified_tag_list1 = "[\"娱乐\",\"军事\",\"体育\",\"历史\",\"健康\",\"历史\",\"科技\",\"文化\",\"教育\",\"游戏\",\"生活\"]"
modified_tag_ans1 = "[\"科技\"]"

example_2 = "咖啡不仅是全球最受欢迎的饮品之一，也是一种文化象征。它的种类繁多，从浓郁的意式浓缩到轻柔的拿铁。每种咖啡都有其独特的风味和冲泡方法。咖啡文化在世界各地不断演变，从传统的咖啡馆到现代的快速咖啡连锁店，它不仅仅是一种饮品，更是一种生活方式的体现。"
tag_list2 = "[\"可乐\",\"咖啡\",\"饮品\",\"音频\",\"旅游\",\"咖啡文化演变\",\"大航海时代\",\"盐湖城\",\"生活方式表达\",\"百慕大\"]"
# tag_list2 = "[\"葡萄酒鉴赏\",\"意式烹饪法\",\"咖啡\",\"饮品文化\",\"快餐文化\",\"咖啡多样性\",\"高科技产品\",\"拿铁\",\"咖啡馆\",\"传统饮食\",\"艺术表现\"]"
ans_tag2 = "[\"咖啡\",\"饮品\",\"咖啡文化演变\",\"生活方式表达\"]"
# ans_tag2 = "[\"咖啡\",\"饮品文化\",\"咖啡多样性\",\"拿铁\",\"咖啡馆\"]"
ans_tag2_limit = "[\"咖啡\",\"咖啡文化演变\",\"生活方式表达\"]"
to_score_tag2 = "[\"可乐\",\"咖啡\",\"饮品\",\"音频\",\"旅游\",\"文化象征\",\"大航海时代\",\"盐湖城\",\"生活方式\",\"百慕大\"]"
score_list2 = "{'可乐':21, '咖啡':99, '饮品':90, '音频':13, '旅游':12, '文化象征':76, '大航海时代':18, '盐湖城':14, '生活方式':88, '百慕大':19}"
modified_tag_list2 = "[\"娱乐\",\"军事\",\"体育\",\"历史\",\"健康\",\"历史\",\"科技\",\"文化\",\"教育\",\"游戏\",\"生活\"]"
modified_tag_ans2 = "[\"文化\",\"生活\"]"

example_3 = "古埃及文明是人类历史上最辉煌的文明之一，以其金字塔、木乃伊和象形文字闻名于世。这个文明沿尼罗河发展，持续了近三千年。古埃及人对天文学、数学和建筑学有着深刻的理解和贡献。金字塔不仅是古埃及王权的象征，也展示了古埃及人惊人的工程技术和艺术成就。此外，法老和神话故事也是研究古埃及文明不可或缺的一部分。"
tag_list3 = "[\"古埃及文明\",\"虚拟现实\",\"现代生活\",\"金字塔\",\"木乃伊\",\"霸王龙\",\"翼龙\",\"古代科技与工程\",\"幼发拉底河\",\"法老\",\"人机交互\",\"尼罗河\",\"历史遗产\", \"恒河文明\"]"
# tag_list3 = "[\"古埃及文明\",\"现代科技\",\"中世纪欧洲\",\"古代工程奇迹\",\"工业革命\",\"尼罗河\",\"动力学\",\"数字时代\",\"文明史\",\"古代科学贡献\",\"海洋探索\",\"象形文字\",\"现代金字塔理论\",\"古代传说合集\",\"木乃伊\"]"
ans_tag3 = "[\"古埃及文明\",\"金字塔\",\"木乃伊\",\"历史遗产\",\"古代科技与工程\",\"法老\",\"尼罗河\"]"
# ans_tag3 = "[\"古埃及文明\",\"古代工程奇迹\",\"尼罗河\",\"文明史\",\"古代科学贡献\",\"象形文字\",\"木乃伊\"]"
ans_tag3_limit = "[\"古埃及文明\",\"历史遗产\",\"古代科技与工程\"]"
to_score_tag3 = "[\"古埃及文明\",\"虚拟现实\",\"现代生活\",\"金字塔\",\"木乃伊\",\"霸王龙\",\"翼龙\",\"象形文字\",\"幼发拉底河\",\"法老\",\"人机交互\",\"尼罗河\"]"
score_list3 = "{'古埃及文明':99, '虚拟现实':11, '现代生活':12, '金字塔':98, '木乃伊':95, '霸王龙':15, '翼龙':3, '象形文字':89, '幼发拉底河':12, '法老':93, '人机交互':13, '尼罗河':91}"
modified_tag_list3 = "[\"娱乐\",\"军事\",\"体育\",\"历史\",\"健康\",\"历史\",\"科技\",\"文化\",\"教育\",\"游戏\",\"生活\"]"
modified_tag_ans3 = "[\"历史\",\"文化\",\"科技\"]"

req1 = "请你用中文完成给文本打tag的任务，具体如下：你的输入是给定的词语列表和一段文本，这两者用分号隔开。你需要根据词语和文本的相关度，从给定的词语列表中选择适合这段文本的词语作为tag，以列表方式输出。"
req2 = "请你用中文完成给文本打tag的任务，具体如下：你的输入是给定的一段文本。请你总结适合这段文本的tag，以列表方式输出。"
req3 = "请你对给定的文本，用简短的语句概括其主要内容，不需要进行解释："
req4 = "根据以下内容，为我提取3个中文关键词："
req5 = "请根据以下内容，为我提取中文关键词："
req6 = "请你用中文完成给文本打3个tag的任务，具体如下：你的输入是给定的一段文本。请你总结适合这段文本的3个tag，以列表方式输出。"
req7 = "请你用中文完成给文本打tag的任务，具体如下：你的输入是给定的一段文本。请你总结适合这段文本的一个tag，以[\"xx\"]的形式输出。"
req8 = "请你完成根据文本内容给指定词语打分的任务。具体如下：你的输入是文本和待评分的词语列表，你需要对待评分的每个词语，根据他们和文本内容的相关度打分，然后以json格式输出。请注意，你要给所有的待评分词语打分"


def get_choosing_prompt_zero_shot(input_text, input_list):
    print(input_list)
    return f"{req7}"\
           f"{input_text};{input_list}\n"


def get_choosing_prompt(input_text, input_list):
    print(input_list)
    return f"{req1}" \
           "请你参照以下的例子进行输入输出：\n" \
           f"输入：{example_1};{modified_tag_list1}\n" \
           f"输出：{modified_tag_ans1}\n" \
           f"输入：{example_2};{modified_tag_list2}\n" \
           f"输出：{modified_tag_ans2}\n" \
           f"输入：{example_3};{modified_tag_list3}\n" \
           f"输出：{modified_tag_ans3}\n" \
           f"接下来轮到你\n" \
           f"输入：{input_text};{input_list}\n" \
           f"输出："


def get_summarize_words_prompt(input_text):
    return f"{req2}" \
          "请你参照以下的例子进行输入输出：\n" \
          f"输入：{example_1}\n" \
          f"输出：{ans_tag1}\n" \
          f"输入：{example_2}\n" \
          f"输出：{ans_tag2}\n" \
          f"输入：{example_3}\n" \
          f"输出：{ans_tag3}\n" \
          f"接下来轮到你\n" \
          f"输入：{input_text}\n" \
          f"输出："


def get_summarize_words_prompt_zero_shot(input_text):
    return f"{req5}" \
           f"{input_text}\n" \
           f"请以列表的形式给出关键词,形如[\"xx\",\"xx\",\"xx\"]"
           

def get_summarize_words_prompt_limit(input_text):
    return f"{req6}" \
           f"请参照以下的例子进行输入输出，每个输出结果都是一个大小为3的列表：\n" \
           f"输入：{example_1}\n" \
           f"输出：{ans_tag1_limit}\n" \
           f"输入：{example_2}\n" \
           f"输出：{ans_tag2_limit}\n" \
           f"输入：{example_3}\n" \
           f"输出：{ans_tag3_limit}\n" \
           f"接下来轮到你\n" \
           f"输入：{input_text}\n" \
           f"输出："
          

def get_summarize_article_prompt(input_text):
    return f"{req3}\n" \
           f"{input_text}"


def get_words_score_prompt(input_text, input_list):
    return f"{req8}\n" \
           f"请参照以下给出的例子进行输入输出：\n" \
           f"输入文本：{example_1}\n" \
           f"输入列表：{to_score_tag1}\n" \
           f"输出：{score_list1}\n" \
           f"输入文本：{example_2}\n" \
           f"输入列表：{to_score_tag2}\n" \
           f"输出：{score_list2}\n" \
           f"输入文本：{example_3}\n" \
           f"输入列表：{to_score_tag3}\n" \
           f"输出：{score_list3}\n" \
           f"接下来轮到你：\n" \
           f"输入文本：{input_text}\n" \
           f"输入列表：{input_list}\n" \
           f"输出："
