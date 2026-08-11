import json


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

        self.quiz_list = []
        self.best_score = 0

        self.load_data()



    # JSON 불러오기
    def load_data(self):

        try:

            with open(
                "state.json",
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)


            for quiz in data["quizzes"]:

                self.quiz_list.append(
                    Quiz(
                        quiz["question"],
                        quiz["choices"],
                        quiz["answer"]
                    )
                )


            self.best_score = data["best_score"]

            print(
                "저장된 데이터를 불러왔습니다.",
                "(",
                len(self.quiz_list),
                "개 퀴즈 / 최고점수",
                self.best_score,
                "점)"
            )


        except FileNotFoundError:


            print("저장 파일이 없습니다.")
            print("기본 퀴즈를 사용합니다.")

            self.quiz_list = default_quizzes




    # JSON 저장
    def save_data(self):

        quiz_data = []


        for quiz in self.quiz_list:

            quiz_data.append(
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer
                }
            )


        data = {

            "quizzes": quiz_data,
            "best_score": self.best_score

        }


        with open(
            "state.json",
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )



    # 퀴즈 풀기
    def play_quiz(self):

        score = 0


        for i, quiz in enumerate(self.quiz_list, start=1):

            print()
            print("--------------------------------")
            print("[문제", i, "]")

            quiz.show()


            answer = int(
                input("정답 번호 : ")
            )


            if quiz.check_answer(answer):

                print("정답입니다!")
                score += 1

            else:

                print("오답입니다.")



        result = score * 100 // len(self.quiz_list)


        print()
        print(
            "결과:",
            len(self.quiz_list),
            "문제 중",
            score,
            "문제 정답!"
        )

        print(
            "점수:",
            result,
            "점"
        )



        if result > self.best_score:

            self.best_score = result

            print(
                "새로운 최고 점수입니다!"
            )



    # 퀴즈 추가
    def add_quiz(self):

        print()
        print("새로운 퀴즈를 추가합니다.")


        question = input("문제를 입력하세요 : ")

        choices = []


        for i in range(1,5):

            choice = input(
                str(i) + "번 선택지 : "
            )

            choices.append(choice)



        answer = int(
            input("정답 번호 : ")
        )


        new_quiz = Quiz(
            question,
            choices,
            answer
        )


        self.quiz_list.append(new_quiz)

        self.save_data()


        print("퀴즈가 추가되었습니다.")



    # 목록
    def show_quiz_list(self):

        print()
        print("===== 퀴즈 목록 =====")


        for i, quiz in enumerate(self.quiz_list, start=1):

            print(
                i,
                quiz.question
            )



    # 점수 확인
    def show_score(self):

        print()

        print(
            "현재 최고 점수는",
            self.best_score,
            "점입니다."
        )



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



    def run(self):

        while True:

            self.show_menu()

            menu = input(
                "번호를 선택하세요 : "
            )


            if menu == "1":

                self.play_quiz()


            elif menu == "2":

                self.add_quiz()


            elif menu == "3":

                self.show_quiz_list()


            elif menu == "4":

                self.show_score()


            elif menu == "5":

                self.save_data()

                print(
                    "퀴즈를 저장했습니다."
                )

                print(
                    "프로그램을 종료합니다."
                )

                break


            else:

                print(
                    "잘못 입력했습니다."
                )




game = QuizGame()
game.run()