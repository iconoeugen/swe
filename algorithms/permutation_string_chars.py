#!/usr/bin/python


def allperm(inputstr):
    for i in range(len(inputstr)):
        yield(inputstr[i])
        for s in allperm(inputstr[:i] + inputstr[i+1:]):
            yield(inputstr[i] + s)


def perms(str, ans = ""):
    if len(str) == 0:
        yield ans
        return

    for i in range(len(str)):
        yield from perms(str[:i] + str[i+1:], ans + str[i])

def subs_perms(str, ans = ""):
    if len(str) == 0:
        return

    for i in range(len(str)):
        yield ans + str[i]
        yield from perms(str[:i] + str[i+1:], ans + str[i])

def permuteSol(A, idx = 0):
    if idx == len(A)-1:
        yield A[:]

    for i in range(idx, len(A)):
        A[idx], A[i] = A[i], A[idx]
        yield from permuteSol(A, idx+1)
        A[idx], A[i] = A[i], A[idx]

if __name__ == "__main__":
    #print("{}".format([ s for s in allperm("abc")]))
    #print("{}".format([ s for s in subs_perms("abc")]))
    print("{}".format([ s for s in permuteSol(["a", "b", "c"])]))
