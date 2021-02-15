import pytest


@pytest.fixture()
def connectDB():
    print("test_demo1 中的 connect DB")


# 测试函数
def test_a(connectDB):
    print("sub_demo test_a")


# 测试类
class TestA:
    # 测试方法
    def test_b(self):
        print("sub_demo test_b")
