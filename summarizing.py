import json

import utils
from prompts import get_summarize_words_prompt
from utils import post_msg_llm, url2, extract_list
from tagging import modified_choosing_task


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

