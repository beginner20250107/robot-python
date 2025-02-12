

def contains_369(num):
     return any(digit in '369' for digit in str(num))

     """
    숫자에 3, 6, 9가 포함되어 있는지 확인합니다.
    
    Args:
        num (int): 검사할 숫자.
    Returns:
        bool: 3, 6, 9 중 하나라도 포함되어 있으면 True, 그렇지 않으면 False.
    """

def correct_answer(num):
    return "짝" if contains_369(num) else str(num)

    """
    숫자에 따라 정답을 반환합니다.
    숫자에 3, 6, 9가 있으면 "짝"을, 없으면 숫자를 문자열로 반환합니다.
    
    Args:
        num (int): 현재 숫자.
    Returns:
        str: "짝" 또는 숫자 문자열.
    """

def play_game():
    # my_turn 변수는 현재 턴이 사용자(True)인지 컴퓨터(False)인지를 나타냅니다.
    my_turn = True  # True: 사용자 차례, False: 컴퓨터 차례

    # 1부터 99까지 숫자에 대해 반복합니다.
    for num in range(1, 100):
        # 사용자 턴일 때
        
        if my_turn:
            # try 블록: 사용자로부터 입력을 받을 때 예외(오류)가 발생할 수 있으므로 이를 처리하기 위해 사용합니다.
            try:
                # input() 함수: 사용자에게 입력을 요청합니다.
                # f-string (f"{num}번, ...")을 사용하여 현재 숫자를 화면에 표시합니다.
                # .strip() 메서드는 입력된 문자열의 앞뒤 공백을 제거하여, 실수로 입력된 공백이 문제를 일으키지 않도록 합니다.
                user_input = input(f"{num}번, 당신 차례입니다 (3,6,9 포함이면 '짝'): ").strip()

            # except 구문: 사용자가 입력 도중 Ctrl+C (KeyboardInterrupt)나 입력이 끝났을 때 발생할 수 있는 EOFError가 발생하면,
            # 예외 처리를 하여 프로그램이 비정상 종료되지 않고, 적절한 메시지를 출력한 후 반복문을 종료합니다.
            except (EOFError, KeyboardInterrupt):
                print("\n게임이 중단되었습니다.")
                break

            # 사용자가 입력한 값(user_input)과 현재 숫자에 대한 정답(correct_answer(num))을 비교합니다.
            # 만약 값이 다르면, "패배!"를 출력하고 return을 통해 play_game() 함수를 종료합니다.
            if user_input != correct_answer(num):
                print("패배!")
                return  # return은 현재 함수를 종료하는 역할을 합니다.
        else:
            # 컴퓨터 턴일 때: 컴퓨터는 항상 정답을 올바르게 출력합니다.
            print(f"{num}번, 컴퓨터 차례입니다: {correct_answer(num)}")
        
        # 턴 전환: 현재 턴이 사용자라면 컴퓨터 턴으로, 컴퓨터라면 사용자 턴으로 변경합니다.
        # 'not my_turn'은 my_turn의 값(True면 False, False면 True)을 반전시킵니다.
        my_turn = not my_turn
    else:
        # for 루프가 중간에 break 없이 정상적으로 모두 완료되었을 경우에 실행됩니다.
        print("게임 클리어!")


# 아래 코드는 현재 스크립트가 직접 실행될 때만 play_game() 함수를 호출합니다.
# __name__ 은 파이썬에서 내장 변수로, 모듈이 직접 실행될 경우 "__main__" 값을 갖습니다.
# 만약 이 모듈이 다른 모듈에 의해 import된다면 __name__에는 모듈의 이름이 들어가므로,
# 이 경우 play_game() 함수가 자동으로 실행되지 않습니다..
if __name__ == "__main__":
    play_game()

