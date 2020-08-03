# -*- encoding=utf8 -*-
__author__ = "ShaoxiongYuan"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


def get_red_package():
    """
    发现红包，就立马执行点击操作
    :return:
    """
    # 1.获取消息列表元素
    msg_list_elements_pre = poco("android.widget.RelativeLayout").children()

    # 1.1 由于msg_list_elements属于UIObjectProxy对象，不能使用reverse进行反转
    # 利用For把消息取反
    msg_list_elements = []

    for item in msg_list_elements_pre:
        msg_list_elements.insert(0, item)

    # 2.从后面的消息开始遍历
    for msg_element in msg_list_elements:

        # 2.1 微信红包标识元素
        red_key_element = msg_element.offspring('com.tencent.mm:id/al7')

        # 2.2 是否已经领取元素
        has_click_element = msg_element.offspring('com.tencent.mm:id/r0')

        # 2.3 红包【包含：收到的红包和自己发出去的红包】
        if red_key_element:
            print('发现一个红包')
            if has_click_element.exists() and (
                    has_click_element.get_text() == 'Opened' or has_click_element.get_text() == 'None left'):
                print('已经领取过了，略过~')
                continue
            else:
                # 抢这个红包
                print('新红包，抢抢抢~')
                msg_element.click()
                click_element = poco("com.tencent.mm:id/den")
                if click_element.exists():
                    click_element.click()
                keyevent('BACK')
        else:
            continue


if __name__ == '__main__':
    auto_setup(__file__)
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    wechat = poco(name='WeChat')

    folder_loc = input('微信在哪个文件夹？请输入名称：')
    if folder_loc:
        while True:
            folder_names = poco(name='com.huawei.android.launcher:id/folder_icon_name')
            folder_preview = poco(name='com.huawei.android.launcher:id/preview_background')
            if folder_names.exists():
                for name, folder in zip(folder_names, folder_preview):
                    if name.get_text() == folder_loc:
                        folder.click()
                        break
                if wechat.exists():
                    break
            # poco('Scroll View').swipe('left')

    # 1.打开微信
    wechat.click()

    # 2.输入要抢的群
    # target = input('要抢哪个群:')
    target = '抢红包'

    # 3.获取消息列表名称
    item_elements = poco(name='com.tencent.mm:id/e3x')
    if item_elements.exists():
        names = list(map(lambda x: x.get_text(), item_elements))
        print(names)
        if target in names:
            index = names.index(target)
            # 点击进入群聊
            item_elements[index].click()
            while True:
                get_red_package()
                print('休眠1秒钟，继续刷新页面，开始抢红包。')
                sleep(1)
        else:
            print('找不到这个群')
    else:
        print('找不到这个群')
