def solution(before, after):
    answer = 0
    before=list(before)
    before.sort()
    after=list(after)
    after.sort()
    if before==after:
        return 1
    else:
        return 0