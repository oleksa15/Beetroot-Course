import requests
import json
import time


def main():
    data = get_json()
    comments = extract_info(data)
    save_json(comments)


def get_json() -> dict:
    page = 'https://api.pushshift.io/reddit/comment/search/'
    r = requests.get(page)
    return r.json()


def extract_info(data: dict) -> dict:
    comments_dict = {'comments': []}

    data_key = data.get('data')
    for el in data_key:
        temp = {}
        temp['author'] = el.get('author')
        temp['comment'] = el.get('body')
        temp['link'] = el.get('permalink')

        epoch_time = el.get('created_utc')
        temp['time'] = time.ctime(epoch_time)

        comments_dict.get('comments').append(temp)

    return comments_dict


def save_json(data: dict) -> None:
    with open('comments.txt', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    main()