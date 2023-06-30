for i in range(3):
    a = list(map(int, input().split()))
    b = []
    h = a[3] - a[0]
    m = a[4] - a[1]
    s = a[5] - a[2]
    if s < 0:
        s += 60
        m -= 1
    if m < 0:
        m += 60
        h -= 1
    print(h, m, s)