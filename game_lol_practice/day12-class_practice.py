
# from functions.shop import buy_item, title as shop_title
#from friends.chat import send_message
from hw2 import Customer

title = 'Main Module'
def turn_on():
    print('= Start game =')
    User = input('User_name을 입력하세요 : ')
    Money = input('소유하고 계신 돈을 입력하세요 : ')
    Money = int(Money)
    customer = Customer(User, Money)
    print(customer.name)
    print(type(customer.money))
    wapper = 6000
    bulgoggi_wapper = 7000
    galic_steak = 8000
    coke = 1000
    while True:
        choice = input('What would you like to do?\n  1: Burger\n  2: Coke\n  3: Packaging?\n  0: Exit\n    Input : ')
        if choice == '0':
            break
        elif choice == '1':
            burger_choice= input('What would you like to order?\n 1: wapper\n 2: bulgoggi_wapper_\n 3: galic_steak 0: Exit\n  Input : ')
            if burger_choice == '0':
                break
            elif burger_choice == '1':
                print('버거 가격은 {}입니다.'.format(wapper))
                change = customer.money - wapper
                print('거스름돈은 {}입니다.'.format(change))
            elif burger_choice == '2':
                print('버거 가격은 {}입니다.'.format(bulgoggi_wapper))
                change = customer.money - bulgoggi_wapper
                print('거스름돈은 {}입니다.'.format(change))
            elif burger_choice == '3':
                print('버거 가격은 {}입니다.'.format(galic_steak))
                change = customer.money - galic_steak
                print('거스름돈은 {}입니다.'.format(change))

        elif choice == '2':
            coke_choice= input('Do you need a coke? (y/n) : ')
            if coke_choice == 'y':
                print('콜라 가격은 {}입니다.'.format(coke))
                change_coke = change - coke
                print('거스름돈은 {}입니다.'.format(change_coke))
            elif coke_choice == 'n':
                print('거스름돈은 {}입니다.'.format(change))

        elif choice == '3':
            packaging_choice= input('Do you need a packaging? (y/n) : ')
            if packaging_choice == 'y':
                print('5분 내로 포장해드리겠습니다.')
            elif packaging_choice == 'n':
                print('자리에 앉아계시면 진동벨로 안내해드리겠습니다.')
        else:
            print('Choice not exist')
        print('-----------------------')
    print('= End game =')

if __name__ == '__main__':
    turn_on()