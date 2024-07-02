import random

def up_down_game():
    best_attempts = None

    while True:
        computer_number = random.randint(1, 100)
        attempts = 0
        player_number = None

        if best_attempts is not None:
            print(f"이전 게임 플레이어 최고 시도 횟수: {best_attempts}")

        print("1부터 100 사이의 숫자를 맞혀보세요!")

        while player_number != computer_number:
            try:
                player_number = int(input("숫자를 입력하세요: "))
                if player_number < 1 or player_number > 100:
                    print("유효한 범위 내의 숫자를 입력하세요")
                    continue

                attempts += 1

                if player_number < computer_number:
                    print("업")
                elif player_number > computer_number:
                    print("다운")
                else:
                    print(f"맞았습니다. 시도한 횟수: {attempts}")
                    if best_attempts is None or attempts < best_attempts:
                        best_attempts = attempts

            except ValueError:
                print("유효한 숫자를 입력하세요.")

        play_again = input("다시 하시겠습니까? (y/n): ").lower()
        if play_again != 'y':
            print("게임을 종료합니다")
            break

up_down_game()
