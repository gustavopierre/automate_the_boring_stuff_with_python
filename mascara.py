

def maskify(cc):
    if len(cc) >= 4:
        last = cc[-4:-1]+cc[-1]
        return '#'*(len(cc)-4) + last
    else:
        return cc

print(maskify("4556364607935616"))

print(maskify(     "64607935616"))
print(maskify(               "1"))
print(maskify(                ""))