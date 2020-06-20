# 人脸(水果)识别示例：预测
import paddle
import paddle.fluid as fluid
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from global_var import *

place = fluid.CPUPlace()
infer_exe = fluid.Executor(place)
inference_scope = fluid.core.Scope()
model_freeze_dir = "model_freeze/"


# 加载数据
def load_image(path):
    img = paddle.dataset.image.load_and_transform(path, 240, 240, False).astype("float32")
    img = img / 255.0
    return img


infer_imgs = []

# 类别0
test_img = "../../data/Magnetic/MT_Blowhole/Imgs/exp6_num_4841.jpg"
# 类别1
# test_img = "../../data/Magnetic/MT_Break/Imgs/exp2_num_271384.jpg"
# 类别2
# test_img = "../../data/Magnetic/MT_Crack/Imgs/exp1_num_32128.jpg"
# 类别3
# test_img = "../../data/Magnetic/MT_Fray/Imgs/exp1_num_20362.jpg"
# 类别4
# test_img = "../../data/Magnetic/MT_Free/Imgs/exp3_num_344580.jpg"
# test_img = "../../data/Magnetic/MT_Free/Imgs/exp6_num_293912.jpg"
# 类别5
# test_img = "../../data/Magnetic/MT_Uneven/Imgs/exp1_num_45007.jpg"

infer_imgs.append(load_image(test_img))
infer_imgs = np.array(infer_imgs)
print("infer_imgs.shape:", infer_imgs.shape)

with fluid.scope_guard(inference_scope):
    [inference_program, feed_target_names, fetch_targets] = \
        fluid.io.load_inference_model(model_freeze_dir, infer_exe)

    # 开始预测
    results = infer_exe.run(inference_program,
                            feed={feed_target_names[0]: infer_imgs},
                            fetch_list=fetch_targets)
    print("results:", results)

    result = results[0]
    print(result.shape)
    max_index = np.argmax(result)
    for k, v in name_dict.items():
        if max_index == v:
            print("预测结果: 类别编号[%d], 名称[%s], 概率[%.4f]" % (max_index, k, result[0][max_index] * 100))

    # 显示原图
    img = Image.open(test_img)
    plt.imshow(img)
    plt.show()
