
# 📚 과제 목표 및 학습 내용

이 프로젝트를 진행하면서 Python 기초 문법부터 클래스와 객체,
파일 입출력, Git을 활용한 버전 관리까지 학습했습니다.

각 항목은 단순히 기능을 구현하는 것뿐만 아니라,
프로젝트에서 실제로 사용한 내용을 기준으로 정리했습니다.

---

# 1. Python 기초

## ✅ 변수

변수는 데이터를 저장하고 필요할 때 다시 사용하기 위한 이름입니다.

프로젝트에서는 퀴즈의 점수, 사용자 입력, 문제 등의 데이터를
변수에 저장하여 사용했습니다.

예:

```python
score = 0
menu = input("번호를 선택하세요 : ")
```


## ✅ int / str / bool / list / dict

| 자료형    | 의미                    | 프로젝트 활용         |
| ------ | --------------------- | --------------- |
| `int`  | 정수                    | 점수, 정답 번호       |
| `str`  | 문자열                   | 문제, 선택지, 사용자 입력 |
| `bool` | 참/거짓                  | 퀴즈 플레이 여부       |
| `list` | 여러 데이터를 순서대로 저장       | 퀴즈 목록, 선택지      |
| `dict` | Key와 Value 형태로 데이터 저장 | JSON 저장 데이터     |


프로젝트에서 다음과 같이 여러 자료형을 사용했습니다.

```
score = 0

question = "다음 중 조지 오웰의 작품은?"

choices = [
    "동물농장",
    "이방인",
    "노인과 바다",
    "데미안"
]

data = {
    "quizzes": quiz_data,
    "best_score": self.best_score
}
```

## ✅ if / elif / else

조건에 따라 프로그램이 서로 다른 동작을 수행하도록 사용합니다.

퀴즈 게임에서는 메뉴 선택에 따라 실행할 기능을 결정했습니다.

```
if menu == 1:
    self.play_quiz()

elif menu == 2:
    self.add_quiz()

elif menu == 3:
    self.show_quiz_list()

elif menu == 4:
    self.show_score()

elif menu == 5:
    break

```

## ✅ for / while

for는 정해진 데이터나 범위를 반복할 때 사용하고,
while은 특정 조건이 만족될 때까지 반복할 때 사용합니다.

프로젝트에서는 퀴즈를 순서대로 출제할 때 for를 사용했습니다.

```
for i, quiz in enumerate(self.quiz_list, start=1):
    quiz.show()

메뉴를 계속 표시하기 위해서는 while을 사용했습니다.

while True:
    self.show_menu()
```


## ✅ 함수와 매개변수 / 반환값

함수는 반복되는 기능을 하나의 단위로 만들어 재사용할 수 있게 합니다.

프로젝트에서는 정답을 확인하는 기능을 메서드로 만들었습니다.

```
def check_answer(self, user_answer):
    return user_answer == self.answer
```

user_answer는 매개변수이며,
정답 여부를 True 또는 False로 반환합니다.

# 2. 클래스와 객체

## ✅ 클래스란?

클래스는 관련된 데이터와 기능을 하나로 묶기 위한 설계도입니다.

이 프로젝트에서는 두 개의 클래스를 사용했습니다.

Quiz : 하나의 퀴즈 데이터를 관리
QuizGame : 전체 퀴즈 게임을 관리

## ✅ __init__과 self

__init__은 객체가 생성될 때 처음 실행되는 메서드입니다.

```
def __init__(self, question, choices, answer):
    self.question = question
    self.choices = choices
    self.answer = answer
```

self는 생성된 객체 자기 자신을 의미합니다.

따라서 각각의 Quiz 객체가 자신만의 문제, 선택지,
정답 데이터를 가질 수 있습니다.

## ✅ 속성과 메서드

속성(attribute)은 객체가 가지고 있는 데이터이고,
메서드(method)는 객체가 수행할 수 있는 기능입니다.

Quiz의 속성
```
self.question
self.choices
self.answer
```
Quiz의 메서드
```
show()
check_answer()
QuizGame의 메서드
play_quiz()
add_quiz()
show_quiz_list()
show_score()
load_data()
save_data()
run()
```

# 3. 파일 입출력

## ✅ 파일 읽기와 쓰기

Python의 open()을 이용하여 파일을 읽거나 쓸 수 있습니다.

프로젝트에서는 state.json을 읽을 때:

```
with open(
    "state.json",
    "r",
    encoding="utf-8"
) as file:
```

저장할 때:

```
with open(
    "state.json",
    "w",
    encoding="utf-8"
) as file:
```

을 사용했습니다.

## ✅ JSON

JSON은 데이터를 Key와 Value 구조로 표현할 수 있는
텍스트 기반 데이터 형식입니다.

이 프로젝트에서는 프로그램을 종료해도 퀴즈와 최고 점수를
유지하기 위해 state.json을 사용했습니다.
```
{
    "quizzes": [],
    "best_score": 100,
    "has_played": true
}
```
Python 객체를 JSON으로 저장할 때는 json.dump()를 사용하고,
JSON 데이터를 불러올 때는 json.load()를 사용했습니다.

## ✅ try / except

프로그램 실행 중 발생할 수 있는 오류 때문에
프로그램 전체가 갑자기 종료되지 않도록 예외 처리를 사용했습니다.

```
try:
    number = int(user_input)

except ValueError:
    print("숫자를 입력해주세요.")

파일을 불러올 때 발생할 수 있는 오류도 처리했습니다.

except FileNotFoundError:
    print("저장 파일이 없습니다.")
```

# 4. Git 기초
## ✅ Git이란?

Git은 코드의 변경 이력을 기록하고 관리하는
버전 관리 시스템입니다.

이번 프로젝트에서는 기능 하나를 구현할 때마다 커밋하여
프로그램이 만들어지는 과정을 단계별로 기록했습니다.

## ✅ 주요 Git 명령어
| 명령어            | 역할                    |
| -------------- | --------------------- |
| `git init`     | 현재 폴더를 Git 저장소로 시작    |
| `git add`      | 변경된 파일을 커밋할 대상으로 등록   |
| `git commit`   | 변경사항을 하나의 버전으로 기록     |
| `git push`     | 로컬 커밋을 GitHub에 업로드    |
| `git pull`     | GitHub의 최신 변경사항을 가져옴  |
| `git checkout` | 다른 브랜치로 이동하거나 브랜치를 생성 |
| `git clone`    | 원격 저장소를 컴퓨터에 복제       |

## ✅ Branch

브랜치는 기존 코드를 유지하면서
별도의 작업 공간에서 새로운 기능을 개발할 수 있게 합니다.

이번 프로젝트에서는:

```
git checkout -b feature/play-quiz
```

명령으로 새로운 브랜치를 생성했습니다.

작업 완료 후:

```
git checkout main
git merge feature/play-quiz
```

을 이용하여 main 브랜치에 병합했습니다.

## ✅ Clone

다른 컴퓨터에서 GitHub 프로젝트 전체를 가져오기 위해 사용했습니다.
```
git clone https://github.com/datecoco/python-quiz-game.git
```
이를 통해 집, 회사, 교육장 등 서로 다른 환경에서도
동일한 프로젝트를 이어서 작업할 수 있었습니다.

## ✅ Pull

GitHub에 새로운 변경사항이 있을 경우:
```
git pull
```
을 이용하여 현재 컴퓨터의 프로젝트를 최신 상태로 업데이트했습니다.