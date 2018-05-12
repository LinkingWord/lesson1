def get_answer(question, answers):
    # return answers[question.lower()]
    return answers.get(question.lower(), 'Скажи мне "Привет!" :)')


while True:
    question = input()
    answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

    print(get_answer(question, answers))

# question = input('')
# answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

# print(get_answer(question, answers))

# question = input('')
# answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

# print(get_answer(question, answers))