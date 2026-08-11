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
        "다음 중 히가시노 게이고의 작품은?",
        [
            "용의자 X의 헌신",
            "1984",
            "데미안",
            "변신"
        ],
        1
    ),

    Quiz(
        "다음 중 조지 오웰의 작품은?",
        [
            "동물농장",
            "이방인",
            "노인과 바다",
            "데미안"
        ],
        1
    ),

    Quiz(
        "다음 중 프란츠 카프카의 작품은?",
        [
            "변신",
            "위대한 개츠비",
            "설국",
            "오만과 편견"
        ],
        1
    ),

    Quiz(
        "다음 중 어니스트 헤밍웨이의 작품은?",
        [
            "노인과 바다",
            "데미안",
            "1984",
            "동물농장"
        ],
        1
    ),

    Quiz(
        "다음 중 헤르만 헤세의 작품은?",
        [
            "데미안",
            "변신",
            "이방인",
            "위대한 개츠비"
        ],
        1
    )
]



class QuizGame:

    def __init__(self):
        self.quiz_list = default_quizzes
        self.best_score = 0


    # 퀴즈 풀기
    def play_quiz(self):

        if len(self.quiz_list) == 0:
            print("등록된 퀴즈가 없습니다.")
            return


        score = 0

        print()
        print("========================================")
        print("퀴즈를 시작합니다!")
        print("총", len(self.quiz_list), "문제")
        print("========================================")


        for i, quiz in enumerate(self.quiz_list, start=1):

            print()
            print("----------------------------------------")
            print("[문제", i, "]")

            quiz.show()


            while True:

                try:
                    answer = int(input("정답 번호 : "))

                    if 1 <= answer <= 4:
                        break
                    else:
                        print("1~4 사이 숫자를 입력하세요.")

                except ValueError:
                    print("숫자를 입력하세요.")



            if quiz.check_answer(answer):
                print("정답입니다!")
                score += 1

            else:
                print("오답입니다.")



        print()
        print("========================================")
        print(
            "결과:",
            len(self.quiz_list),
            "문제 중",
            score,
            "문제 정답!"
        )
        print("========================================")



    # 퀴즈 추가
    def add_quiz(self):

        print()
        print("새로운 퀴즈를 추가합니다.")


        question = input("문제를 입력하세요 : ")

        choice1 = input("1번 선택지 : ")
        choice2 = input("2번 선택지 : ")
        choice3 = input("3번 선택지 : ")
        choice4 = input("4번 선택지 : ")


        while True:

            try:

                answer = int(input("정답 번호 : "))

                if 1 <= answer <= 4:
                    break

                else:
                    print("1~4 사이 숫자를 입력하세요.")

            except ValueError:
                print("숫자를 입력하세요.")



        new_quiz = Quiz(
            question,
            [
                choice1,
                choice2,
                choice3,
                choice4
            ],
            answer
        )


        self.quiz_list.append(new_quiz)

        print("퀴즈가 추가되었습니다.")



    # 메뉴
    def show_menu(self):

        print()
        print("========================================")
        print("          나만의 책 퀴즈 게임")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")



    # 실행
    def run(self):

        while True:

            self.show_menu()

            menu = input("번호를 선택하세요 : ").strip()


            if menu == "1":

                self.play_quiz()


            elif menu == "2":

                self.add_quiz()


            elif menu == "5":

                print("프로그램을 종료합니다.")
                break


            else:

                print("현재 준비 중인 기능입니다.")




game = QuizGame()
game.run()