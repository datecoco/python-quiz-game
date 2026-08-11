class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print()
        print(self.question)

        for i, choice in enumerate(self.choices, start=1):
            print(i, choice)

    def check_answer(self, user_answer):
        return user_answer == self.answer


# 기본 퀴즈 5개
default_quizzes = [
    Quiz(
        "다음 중 무라카미 하루키의 책 제목은?",
        [
            "1984",
            "오디세이아",
            "색채가 없는 다자키 쓰쿠루와 그가 순례를 떠난 해",
            "이방인"
        ],
        3
    ),

    Quiz(
        "다음 중 조지 오웰의 소설은?",
        [
            "1984",
            "데미안",
            "이방인",
            "설국"
        ],
        1
    ),

    Quiz(
        "다음 중 알베르 카뮈의 소설은?",
        [
            "이방인",
            "노인과 바다",
            "변신",
            "위대한 개츠비"
        ],
        1
    ),

    Quiz(
        "다음 중 헤르만 헤세의 작품은?",
        [
            "데미안",
            "1984",
            "설국",
            "동물농장"
        ],
        1
    ),

    Quiz(
        "다음 중 어니스트 헤밍웨이의 작품은?",
        [
            "노인과 바다",
            "변신",
            "데미안",
            "이방인"
        ],
        1
    )
]