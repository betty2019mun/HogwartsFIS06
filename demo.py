a = 1


def fun():
    global a
    a = 2
    print(id(a))
    print(f"变量a的值：{a}")
    print("这是一个方法")
    # return True


# print(a)
# fun()
# print(id(a))
# print(a)
# print(fun())

if __name__ == '__main__':
    print("start")
    fun()
    print("stop")
