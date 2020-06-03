def AND(x1, x2):
    w1, w2 = 0.5, 0.5
    theta = 0.7
    tmp = w1 * x1 + w2 * x2
    if tmp > theta:
        return 1
    else:
        return 0


def OR(x1, x2):
    w1, w2 = 0.5, 0.5
    theta = 0.2
    tmp = w1 * x1 + w2 * x2
    if tmp > theta:
        return 1
    else:
        return 0


def XOR(x1, x2):
    s1 = not AND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


print(AND(1, 1))
print(AND(0, 1))
print(AND(0, 0))
print(AND(1, 0))

print('*' * 20)

print(OR(1, 1))
print(OR(0, 1))
print(OR(0, 0))
print(OR(1, 0))

print('*' * 20)

print(XOR(1, 1))
print(XOR(0, 1))
print(XOR(0, 0))
print(XOR(1, 0))
