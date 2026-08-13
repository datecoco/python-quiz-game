import json
# Life is short, you need Python.

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
        self.has_played = False

        self.load_data()

    # 숫자 입력 공통 처리
    def get_number(self, message, minimum, maximum):
        while True:
            user_input = input(message).strip()

            if user_input == "":
                print("빈 값은 입력할 수 없습니다.")
                continue

            try:
                number = int(user_input)

            except ValueError:
                print("숫자를 입력해주세요.")
                continue

            if minimum <= number <= maximum:
                return number

            print(
                minimum,
                "~",
                maximum,
                "사이의 숫자를 입력해주세요."
            )

    # 문자 입력 공통 처리
    def get_text(self, message):
        while True:
            text = input(message).strip()

            if text != "":
                return text

            print("빈 값은 입력할 수 없습니다.")

    # 기본 퀴즈 사용
    def use_default_quizzes(self):
        self.quiz_list = list(default_quizzes)
        self.best_score = 0
        self.has_played = False

    # 데이터 불러오기
    def load_data(self):
        try:
            with open(
                "state.json",
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)

            self.quiz_list = []

            for quiz_data in data["quizzes"]:
                quiz = Quiz(
                    quiz_data["question"],
                    quiz_data["choices"],
                    quiz_data["answer"]
                )

                self.quiz_list.append(quiz)

            self.best_score = data.get(
                "best_score",
                0
            )

            self.has_played = data.get(
                "has_played",
                self.best_score > 0
            )

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

            self.use_default_quizzes()
            self.save_data()

        except (
            json.JSONDecodeError,
            KeyError,
            TypeError,
            OSError
        ):
            print("저장 파일이 손상되었거나 읽을 수 없습니다.")
            print("기본 퀴즈 데이터로 복구합니다.")

            self.use_default_quizzes()
            self.save_data()

    # 데이터 저장
    def save_data(self):
        quiz_data = []

        for quiz in self.quiz_list:
            quiz_data.append({
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer
            })

        data = {
            "quizzes": quiz_data,
            "best_score": self.best_score,
            "has_played": self.has_played
        }

        try:
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

            return True

        except OSError:
            print("데이터 저장 중 오류가 발생했습니다.")
            return False

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

        for i, quiz in enumerate(
            self.quiz_list,
            start=1
        ):
            print()
            print("----------------------------------------")
            print("[문제", i, "]")

            quiz.show()

            answer = self.get_number(
                "정답 번호 : ",
                1,
                4
            )

            if quiz.check_answer(answer):
                print("정답입니다!")
                score += 1
            else:
                print("오답입니다.")
                print(
                    "정답은",
                    quiz.answer,
                    "번입니다."
                )

        result = (
            score * 100
            // len(self.quiz_list)
        )

        self.has_played = True

        print()
        print("========================================")
        print(
            "결과:",
            len(self.quiz_list),
            "문제 중",
            score,
            "문제 정답!"
        )
        print("점수:", result, "점")

        if result > self.best_score:
            self.best_score = result
            print("새로운 최고 점수입니다!")

        print("========================================")

        self.save_data()

    # 퀴즈 추가
    def add_quiz(self):
        print()
        print("새로운 퀴즈를 추가합니다.")

        question = self.get_text(
            "문제를 입력하세요 : "
        )

        choices = []

        for i in range(1, 5):
            choice = self.get_text(
                str(i) + "번 선택지 : "
            )

            choices.append(choice)

        answer = self.get_number(
            "정답 번호 (1~4) : ",
            1,
            4
        )

        new_quiz = Quiz(
            question,
            choices,
            answer
        )

        self.quiz_list.append(new_quiz)

        self.save_data()

        print("퀴즈가 추가되었습니다.")

    # 퀴즈 목록
    def show_quiz_list(self):
        print()
        print("===== 퀴즈 목록 =====")

        if len(self.quiz_list) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print(
            "총",
            len(self.quiz_list),
            "개의 퀴즈가 있습니다."
        )

        print()

        for i, quiz in enumerate(
            self.quiz_list,
            start=1
        ):
            print(i, quiz.question)

    # 최고 점수 확인
    def show_score(self):
        print()

        if not self.has_played:
            print("아직 퀴즈를 풀지 않았습니다.")
            return

        print(
            "현재 최고 점수는",
            self.best_score,
            "점입니다."
        )

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

    # 게임 실행
    def run(self):
        try:
            while True:
                self.show_menu()

                menu = self.get_number(
                    "번호를 선택하세요 : ",
                    1,
                    5
                )

                if menu == 1:
                    self.play_quiz()

                elif menu == 2:
                    self.add_quiz()

                elif menu == 3:
                    self.show_quiz_list()

                elif menu == 4:
                    self.show_score()

                elif menu == 5:
                    self.save_data()

                    print("퀴즈를 저장했습니다.")
                    print("프로그램을 종료합니다.")

                    break

        except (KeyboardInterrupt, EOFError):
            print()
            print("입력이 중단되었습니다.")
            print(
                "현재 데이터를 저장하고 "
                "안전하게 종료합니다."
            )

            self.save_data()


game = QuizGame()
game.run()