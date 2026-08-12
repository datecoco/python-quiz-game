# 📚 나만의 책 퀴즈 게임

Python으로 제작한 기반 문학 퀴즈 게임입니다.

프로그래밍 학습을 위해 `Quiz`와 `QuizGame` 클래스를 활용하고,
JSON 파일 저장 기능을 통해 프로그램 종료 후에도 퀴즈 데이터와 최고 점수를 유지하도록 구현했습니다.

---

## 📖 퀴즈 주제 선정 이유

최근에 작고하신 히가시노 게이고 작가를 추모하며, 개인적으로 좋아하는 고전작가들로 퀴즈를 만들었습니다.

선정 작가:

- 히가시노 게이고
- 조지 오웰
- 프란츠 카프카
- 어니스트 헤밍웨이
- 헤르만 헤세

---

## 🚀 실행 방법

Python 3.10 이상 환경에서 실행합니다.

```bash
python3 main.py
```

## ✨ 기능 목록
| 기능 | 설명 |
|---|---|
| 🎯 퀴즈 풀기 | 등록된 문학 퀴즈를 출제하고 정답 여부를 확인합니다. |
| ➕ 퀴즈 추가 | 사용자가 새로운 퀴즈를 직접 등록합니다. |
| 📋 퀴즈 목록 | 현재 등록된 모든 퀴즈 목록을 확인합니다. |
| 🏆 최고 점수 확인 | 저장된 최고 점수를 확인합니다. |
| 💾 데이터 저장 | `state.json` 파일에 퀴즈와 점수를 저장합니다. |
| 📂 데이터 불러오기 | 프로그램 실행 시 저장된 데이터를 불러옵니다. |


## 📁 파일 구조

```text
python-practice
├── main.py
├── state.json
├── README.md
├── RESULT.md
├── LEARNING.md
└── screenshots
    ├── menu.png
    ├── play.png
    ├── add_quiz.png
    ├── list.png
    └── score.png
```

## 💾 데이터 파일 설명
프로그램 데이터를 저장하는 JSON 파일입니다.

| 항목 | 설명 |
|---|---|
| quizzes | 퀴즈 문제, 선택지, 정답 데이터 |
| best_score | 최고 점수 데이터 |

프로그램 종료 시 저장되고, 다시 실행하면 기존 데이터를 불러옵니다.



## 📸 실행 화면 스크린샷 구성

| 구분 | 스크린샷 |
|---|---|
| 메인 메뉴 | [📷 메뉴 화면 보기](screenshots/menu.png) |
| 퀴즈 풀기 | [📷 퀴즈 플레이 화면 보기](screenshots/play.png) |
| 퀴즈 추가 | [📷 퀴즈 추가 화면 보기](screenshots/add_quiz.png) |
| 퀴즈 목록 | [📷 퀴즈 목록 화면 보기](screenshots/list.png) |
| 최고 점수 | [📷 최고 점수 화면 보기](screenshots/score.png) |
| Python 버전 | [📷 Python 버전 확인](screenshots/ver.png) |
| Git 브랜치 | [📷 Git 브랜치 확인](screenshots/-b.png) |
| Git 작업 기록 | [📷 Git Log 확인](screenshots/git_log.png) |
> Clone / Pull 실습 완료


## 📑 프로젝트 문서

- [✅ 최종 결과물 및 증빙](RESULT.md)
- [📚 과제 목표](LEARNING.md)