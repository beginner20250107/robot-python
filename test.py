


""" def 는 함수를 정의할 때 사용하는 키워드입니다. 함수를 만들면 그 안에 코드를 묶어서 필요할 때 호출할 수 있습니다"""


# 숫자에 3, 6, 9가 있는지 확인
def contains_369(num):

    """ 숫자에(for digit in str(num))"""
    """ 3,6,9 중 하나라도 포함되어 있으면(any(digit in '369')"""
    """ True 반환(return any)"""
    """ return 함수 내부에서 return 뒤에 있는 값을 반환하고 함수 실행을 종료합니다."""

    return any(digit in '369' for digit in str(num))

    """ str()  은 숫자를 문자열로 변환합니다. 문자열로 바꾸면 숫자의 각 자릿수를 개별적으로 검사할 수 있습니다."""
    """ digit  은 숫자의 각 자릿수(문자열 형태)를 하나씩 나타내는 변수입니다."""
    """ any()  는 리스트나 반복 가능한 객체의 값 중 하나라도 True면 True를 반환합니다"""

# 해당 숫자의 정답(짝 or 숫자)을 반환
def correct_answer(num):

    """숫자에 3,6,9가 있으면 '짝'("짝" if contains_369(num))"""
    """없으면 숫자 문자열(else str(num))"""
    """반환, 값이 출력됨!! ( return "짝" )"""

    return "짝" if contains_369(num) else str(num)

#my_turn이 False일 때 True로 바뀌는 코드입니다
my_turn = True  

#range(1, 100): 숫자를 1부터 99까지 순서대로 반복합니다.
for num in range(1, 100):

# my_turn이 true 일 떄 실행
    if my_turn:
        user_input = input(f"{num}번, 당신 차례입니다 (3,6,9 포함이면 '짝'): ")

        """my_turn이 True일 때 사용자의 차례임을 나타냅니다.""" 
        """사용자에게 입력을 요구하고, 현재 숫자가 무엇인지 화면에 보여줍니다"""


#사용자가 입력한 값(user_input)이 정답(correct_answer(num))과 다르면 패배 처리를 합니다
        if user_input != correct_answer(num):
            print("패배!")
            break

        """ break 는 반복문을 즉시 종료합니다."""

# # my_turn이 False 일 떄 실행
# 컴퓨터는 항상 정답을 출력함
    else:
        print(f"{num}번, 컴퓨터 차례입니다: {correct_answer(num)}")
    
# my_turn이 True일 때 False로 바뀌는 코드입니다
    my_turn = not my_turn 
    





