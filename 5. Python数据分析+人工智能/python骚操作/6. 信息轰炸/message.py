import time
from pynput import mouse, keyboard

time.sleep(5)
m_mouse = mouse.Controller()  # 创建一个鼠标
m_keyboard = keyboard.Controller()  # 创建一个键盘
m_mouse.position = (619, 618)  # 将鼠标移动到指定位置
m_mouse.click(mouse.Button.left)  # 点击鼠标左键你好

for i in range(5):
    m_keyboard.type('你好')  # 打字
    m_keyboard.press(keyboard.Key.enter)  # 按下enter
    m_keyboard.release(keyboard.Key.enter)  # 松开enter
    m_keyboard.type('在干什么呢？')  # 打字
    m_keyboard.press(keyboard.Key.enter)  # 按下enter
    m_keyboard.release(keyboard.Key.enter)  # 松开enter
    m_keyboard.type('吃了吗？')  # 打字
    m_keyboard.press(keyboard.Key.enter)  # 按下enter
    m_keyboard.release(keyboard.Key.enter)  # 松开enter
    time.sleep(0.5)  # 等待 0.5秒
