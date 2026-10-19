def check_confirm(message="Вы уверены? (y/n): "):
    while True:
        answer = input(message).lower()
        if answer in ['y', 'yes', 'н', 'да']:
            return True
        if answer in ['n', 'no', 'т', 'нет']:
            return False
        print("Пожалуйста, введите 'y' (да) или 'n' (нет).")