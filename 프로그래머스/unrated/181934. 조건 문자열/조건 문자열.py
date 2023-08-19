def solution(ineq, eq, n, m):
    if eq=="=":
        if ineq=="<":
            return int(n<=m)
        elif ineq==">":
            return int(n>=m)
    elif eq=="!":
        if ineq=="<":
            return int(n<m)
        elif ineq==">":
            return int(n>m)