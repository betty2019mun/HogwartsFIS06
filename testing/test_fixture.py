import pytest


@pytest.fixture()
def login():
    print("登录操作")
    print("获取 token")
    username = "Tom"
    password = "123456"
    token = "token1723432dfewre"
    # yield关键字可以激活fixture的teardown功能
    # yield相当于return，返回数据可以直接跟在yield后面
    yield [username, password, token]
    print("注销操作")


# 需要提前登录
# 在测试用例中传入fixture方法名
def test_case1(login):
    # 获取fixture方法的返回值，直接调用fixture方法名
    print(f"用户信息为：{login}")
    print("测试用例1")


# 不需要提前登录
def test_case2(connectDB):
    print("测试用例2")


# 需要提前登录
# 在测试用例中传入fixture方法名
def test_case3(login):
    print("测试用例3")


# 需要提前登录
@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")
