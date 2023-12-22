import requests
import json
import openai
# url2 = "http://10.58.0.4:8000/v1/chat/completions"
url2 = "https://oneapi.xty.app"

# OPEN_API_KEY = "FAKE_KEY"
OPEN_API_KEY = "sk-2fETNisZEb2BwLGE28F5A6E2F6D648C9873cDc4aA75f5bD3"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"{OPEN_API_KEY}"  # 替换 YOUR_OPEN_API_KEY 为你的实际 API key
}
openai.api_key = "sk-2fETNisZEb2BwLGE28F5A6E2F6D648C9873cDc4aA75f5bD3"
openai.api_base = "https://oneapi.xty.app/v1"


def post_msg_llm(message, url, temperature=0.30):  # 0.60
    response = other_post(message, temperature_in=temperature)
    # data = {
    #     "model": "Qwen-14B",
    #     "messages": [{"role": "user", "content": f"{message}"}],
    #     "temperature": temperature,
    #     "max_tokens": 8192
    # }
    #
    # response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    output = response.choices[0].message.content
    # print(get_cont)
    # json_res = json.loads(get_cont, ensure_ascii=False)
    # choices = json_res["choices"]
    # last_choice = choices[-1]
    # output = last_choice["message"]['content']
    print("output:" + output)
    return output


# model的名字可以是任何字符串
def other_post(content, temperature_in=0.3):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{content}"}
        ],
        stream=False,
        temperature=temperature_in
    )
    return completion


def extract_list(string_in):
    start = string_in.find("[")
    end = string_in.rfind("]")
    return string_in[start:end+1]


def remove_not_in(list_1, list_raw):
    return list(set(list_1).intersection(set(list_raw)))


def remove_in(list_1, list_raw):
    return list(set(list_1).difference(set(list_raw)))
