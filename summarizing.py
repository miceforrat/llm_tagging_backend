import json

import utils
from prompts import get_summarize_words_prompt,get_summarize_article_prompt, get_summarize_words_prompt_limit
from utils import post_msg_llm, url2, extract_list
from tagging import modified_choosing_task


def input_num(input_text):
    return len(input_text)


def summarize_task_limit(input_text):
    if input_num(input_text) < 200:
        get_prompt = get_summarize_words_prompt_limit(input_text)
    else:
        get_prompt = get_summarize_words_prompt(input_text)
    print(input_num(input_text))
    print(get_prompt)
    get_response = post_msg_llm(get_prompt, url2)
    purify = extract_list(get_response)
    print(purify)
    get_list = json.loads(purify)
    return get_list, get_response


def summarize_task(input_text):
    get_prompt = get_summarize_words_prompt(input_text)
    print(get_prompt)
    get_response = post_msg_llm(get_prompt, url2)
    purify = extract_list(get_response)
    print(purify)
    get_list = json.loads(purify)
    return get_list, get_response


def modified_summarize_task(input_text):
    initial_list, list_raw = summarize_task(input_text)
    return modified_choosing_task(input_text, input_list=initial_list, epochs=2)


def summarize_article(input_text):
    get_prompt = get_summarize_article_prompt(input_text)
    get_response = post_msg_llm(get_prompt, url2)
    return get_response
