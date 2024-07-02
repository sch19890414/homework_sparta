import random

def get_computer_choice():
    choices = ['가위', '바위', '보']
    return random.choice(choices)

def get_player_choice():
    choice = input("가위, 바위, 보 중 하나를 선택하세요: ").strip()
    while choice not in ['가위', '바위', '보']:
        print("유효한 입력이 아닙니다.")
        choice = input("가위, 바위, 보 중 하나를 선택하세요: ").strip()
    return choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "무승부!", 'draw'
    elif player_choice == '가위':
        if computer_choice == '보':
            return "사용자 승리!", 'win'
        else:
            return "컴퓨터 승리!", 'lose'
    elif player_choice == '바위':
        if computer_choice == '가위':
            return "사용자 승리!", 'win'
        else:
            return "컴퓨터 승리!", 'lose'
    elif player_choice == '보':
        if computer_choice == '바위':
            return "사용자 승리!", 'win'
        else:
            return "컴퓨터 승리!", 'lose'

def play_game():
    wins = 0
    losses = 0
    draws = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"사용자: {player_choice}, 컴퓨터: {computer_choice}")
        
        result, outcome = determine_winner(player_choice, computer_choice)
        print(result)
        
        if outcome == 'win':
            wins += 1
        elif outcome == 'lose':
            losses += 1
        elif outcome == 'draw':
            draws += 1
        
        play_again = input("다시 하시겠습니까? (y/n): ").strip().lower()
        if play_again != 'y':
            print("게임을 종료합니다")
            print(f"승: {wins} 패: {losses} 무승부: {draws}")
            break

play_game()