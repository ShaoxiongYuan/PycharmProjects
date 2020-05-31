import cv2
import paddlehub as hub

# 加载模型库
stylepro_artistic = hub.Module(name="stylepro_artistic")
# 进行风格迁移
im = stylepro_artistic.style_transfer(
    images=[{
        # 原图
        'content': cv2.imread("scenery.jpg"),
        # 风格图
        'styles': [cv2.imread("style.jpg")]
    }],
    # 透明度
    alpha=0.1
)
# 从返回的数据中获取图片的ndarray对象
im = im[0]['data']
# 保存结果图片
cv2.imwrite('result.jpg', im)
