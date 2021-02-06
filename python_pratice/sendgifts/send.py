# from gift import have_gift
import gift


# 发礼物的方法
def send():
    print("发礼物啦！")
    # have_gift = True
    gift.have_gift = True
    print(id(gift.have_gift))
    # print(id(have_gift))
