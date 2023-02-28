import requests
api_address = 'https://opentdb.com/api.php?amount=1&category=18&type=boolean'

def qna():
    data_request = requests.get(url=api_address)
    question = data_request.json()['results'][0]['question']
    answer = data_request.json()['results'][0]['correct_answer']
    out = {'Question': question,
           'Answer': answer}
    return out