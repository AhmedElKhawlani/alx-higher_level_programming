#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    L = dir(hidden_4)
    for x in L:
        if not x[:2] == '__':
            print(x)
