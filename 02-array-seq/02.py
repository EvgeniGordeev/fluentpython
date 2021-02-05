import bisect

symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii2 = list(filter(lambda c: c > 127, map(ord, symbols)))
print("divmod(5,2)=%s" % (divmod(5, 2),))


def grade(score, breakpoints=(60, 70, 80, 90), grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


grades = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(grades)
