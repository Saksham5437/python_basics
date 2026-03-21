def main():
    num = get_num()
    hello(num)

def get_num():
    while True:
        n = int(input("What's the number? "))
        if n > 0:
            break
    return n

def hello(n):
    for _ in range(n):
        print("hello")


main()