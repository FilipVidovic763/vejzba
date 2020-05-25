from NapadOrkova import Knight
from GameUnitError import GameUnitError




if __name__ == '__main__':
    print('Stvorimo viteza...')
    knight = Knight('Boromir')
    knight.health_meter = 10
    knight.show_health()

    try:
        knight.heal(heal_by=100,full_healing=False)
    except GameUnitError as e:
        print(e)
        print(e.error_message)
    
    knight.show_health()