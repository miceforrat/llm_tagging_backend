import requests
import json
import openai
url2 = "http://10.58.0.4:8000/v1/chat/completions"

OPEN_API_KEY = "FAKE_KEY"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"{OPEN_API_KEY}"  # 替换 YOUR_OPEN_API_KEY 为你的实际 API key
}


def post_msg_llm(message, url, temperature=0.30): # 0.60
    data = {
        "model": "Qwen-14B",
        "messages": [{"role": "user", "content": f"{message}"}],
        "temperature": temperature,
        "max_tokens": 8192
    }

    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    print(response.text)
    json_res = json.loads(response.text)
    choices = json_res["choices"]
    last_choice = choices[-1]
    output = last_choice["message"]['content']
    return output


# model的名字可以是任何字符串
def other_post(content):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{content}"}
        ],
        stream=False,
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
