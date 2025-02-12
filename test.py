def contains_369(num):
    """숫자에 3,6,9 중 하나라도 포함되어 있으면 True 반환"""
    return any(digit in '369' for digit in str(num))

def correct_answer(num):
    """숫자에 3,6,9가 있으면 '짝', 없으면 숫자 문자열 반환"""
    return "짝" if contains_369(num) else str(num)

my_turn = True  # True면 사용자의 차례, False면 컴퓨터 차례

for num in range(1, 100):
    if my_turn:
        user_input = input(f"{num}번, 당신 차례입니다 (3,6,9 포함이면 '짝'): ")
        if user_input != correct_answer(num):
            print("패배!")
            break
    else:
        # 컴퓨터는 항상 정답을 출력함
        print(f"{num}번, 컴퓨터 차례입니다: {correct_answer(num)}")
    
    my_turn = not my_turn  # 차례 교대




