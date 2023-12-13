import json

from flask import Flask, request, jsonify
from summarizing import summarize_task, summarize_article, summarize_task_limit
from tagging import modified_choosing_task

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello world!"


# 对summarize_task任务限制tag数量
@app.route("/summarize/words/limit_nums", methods=["POST"])
def summarize_by_article_limit_nums():
    try:
        print("this is limit nums")
        to_summarize = request.get_json()['content']
        to_ret, _ = summarize_task_limit(to_summarize)
        return jsonify(to_ret[:5])
    except Exception as e:
        print(e)
        return 500


@app.route("/summarize/words", methods=["POST"])
def summarize_by_article():
    try:
        to_summarize = request.get_json()['content']
        to_ret, _ = summarize_task(to_summarize)
        return jsonify(to_ret)
    except Exception as e:
        print(e)
        return 500


@app.route("/tagging", methods=["POST"])
def tag_with_article_and_words():
    try:
        basic_content = request.get_json()['content']
        words_list = request.get_json()['words']
        print(words_list)
        to_ret = modified_choosing_task(basic_content, words_list)
        print(to_ret)
        return jsonify(to_ret)
    except Exception as e:
        print(e)
        return 500


@app.route("/summarize/article", methods=["POST"])
def simple_summarize():
    try:
        basic_content = request.get_json()['content']
        to_ret = summarize_article(basic_content)
        print(to_ret)
        return {"summary": to_ret}
    except Exception as e:
        print(e)
        return 500


@app.after_request
def after_request(response):
    if response.content_type == 'application/json':
        response.data = json.dumps(json.loads(response.data.decode("utf-8")), ensure_ascii=False)
        response.content_type = 'application/json;charset=utf-8'
    return response


if __name__ == '__main__':
    app.run()

