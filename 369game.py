"""
[주석과 로직]

- def 키워드를 사용해 함수를 정의합니다.
- 게임은 1부터 99까지 진행되며, 각 숫자마다 아래와 같은 로직이 존재합니다.

[로직 개요]
1. 숫자에 3, 6, 9가 포함되어 있는지 확인하는 함수: contains_369
   - 숫자를 문자열로 변환한 후, 각 자릿수에 '3', '6', '9'가 있는지 검사.

2. 해당 숫자의 정답을 반환하는 함수: correct_answer
   - contains_369 함수를 이용해 숫자에 3,6,9가 있으면 "짝"을, 없으면 숫자 문자열을 반환.

3. 메인 게임 루프:
   - 사용자의 턴(my_turn=True)일 때: 숫자와 함께 입력을 받고, 정답과 비교하여 일치하지 않으면 게임 종료.
   - 컴퓨터의 턴일 때: 올바른 정답을 출력.
   - 각 턴마다 my_turn 변수를 토글하여 사용자와 컴퓨터가 번갈아 진행.
"""


# 숫자에 3, 6, 9가 있는지 확인하는 함수 구현
def contains_369(num):
    return any(digit in '369' for digit in str(num))

# 해당 숫자의 정답을 반환하는 함수 구현
def correct_answer(num):
    return "짝" if contains_369(num) else str(num)


# 사용자와 컴퓨터가 번갈아 게임을 진행하는 메인 루프 구현
my_turn = True  # True이면 사용자의 턴, False이면 컴퓨터의 턴

for num in range(1, 100):
    if my_turn:
        # 사용자 턴: 입력 받고 정답 비교
        user_input = input(f"{num}번, 당신 차례입니다 (3,6,9 포함이면 '짝'): ").strip()
        if user_input != correct_answer(num):
            print("패배!")
            break  # 정답이 틀리면 게임 종료
    else:
        # 컴퓨터 턴: 항상 올바른 정답 출력
        print(f"{num}번, 컴퓨터 차례입니다: {correct_answer(num)}")
    
    # 턴 전환
    my_turn = not my_turn

