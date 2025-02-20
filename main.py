import sys


try:
    flag_count = False
    flag_num = False
    flag_sort = False
    if '--count' in sys.argv:
        flag_count = True
    if '--num' in sys.argv:
        flag_num = True
    if '--sort' in sys.argv:
        flag_sort = True
    filename = ''
    for i in sys.argv[1:]:
        if i[:2] != '--':
            filename = i
            break
    A = open(filename).readlines()
    if flag_sort:
        A = sorted(A)
    if flag_num:
        for i in range(len(A)):
            A[i] = f'{i} {A[i]}'
    if flag_count:
        A.append(f'rows count: {len(A)}')
    for i in A:
        print(i.replace('\n', ''))
except Exception:
    print('ERROR')
