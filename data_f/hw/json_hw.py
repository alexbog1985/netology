import json


def read_json(file_path, word_max_len=6, top_words_amt=10):
    with open(file_path, 'r', encoding='utf-8') as f:
        data_json = json.load(f)
    data_list = data_json['rss']['channel']['items']
    descriptions = ''
    for data in data_list:
        descriptions += data['description']

    words = descriptions.split(' ')
    words_sorted = sorted(words, key=words.count, reverse=True)
    words_filtered = []
    for word in words_sorted:
        if len(word) > word_max_len and word not in words_filtered:
            words_filtered.append(word)
    return words_filtered[:top_words_amt]


if __name__ == '__main__':
    print(read_json('newsafr.json'))
