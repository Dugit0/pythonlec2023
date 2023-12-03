x, y = 0, 0
cur_step = (0, 0)
direct = {'s': (0, -1), 'n': (0, 1), 'w': (-1, 0), 'e': (1, 0)}
while True:
    cmd = input().split()
    match cmd:
        case ['move', ('s'|'n'|'w'|'e') as dir]:
            cur_step = direct[dir]
            x += cur_step[0]
            y += cur_step[1]
        case ['move']:
            x += cur_step[0]
            y += cur_step[1]
        case ['move', *trash]:
            trash = ' '.join(trash)
            print(f'Cannot move to {trash}')
        case ['retreat']:
            x -= cur_step[0]
            y -= cur_step[1]
        case ['info', ('x'|'y'|'xy') as inf]:
            match inf:
                case 'x':
                    print(x)
                case 'y':
                    print(y)
                case 'xy':
                    print(x, y)
        case ['say', *message]:
            print(*message)
        case []:
            print(x, y)
            break

