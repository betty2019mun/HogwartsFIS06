import pytest
import yaml

from python_code.calc import Calculator

with open('./datas/calc.yaml') as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)


def test_a():
    print("测试用例a")


# def func():
#    print("普通函数")


class TestCalc:
    def setup_class(self):
        print("开始计算")
        # 实例化计算器的类,加self将局部变量改造成实例变量
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a,b,expect",
        add_datas, ids=myid
    )
    @pytest.mark.add
    def test_add(self, a, b, expect):
        # 实例化计算器的类
        # calc = Calculator()
        # 调用add方法
        result = self.calc.add(a, b)
        # 加浮点数判断
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == expect
        pass

    # def test_add2(self,a,b,expect):
    #     # 实例化计算器的类
    #     # calc = Calculator()
    #     # 调用add方法
    #     result = self.calc.add(0.5, 2.7)
    #     # 得到结果之后，需要写断言
    #     assert result == 3.2
    #     pass
    #
    # def test_add3(self,a,b,expect):
    #     # 实例化计算器的类
    #     # calc = Calculator()
    #     # 调用add方法
    #     result = self.calc.add(-1.5, 8)
    #     # 得到结果之后，需要写断言
    #     assert result == 6.5
    #     pass
    @pytest.mark.div
    def test_div(self):
        print("test_div")

    @pytest.mark.sub
    def test_sub(self):
        print("test_sub")

    @pytest.mark.mul
    def test_mul(self):
        print("test_mul")
