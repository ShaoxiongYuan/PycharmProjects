import paddlehub as hub

module = hub.Module(name="pyramidbox_lite_mobile_mask")
input_dict = {"image": ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']}

# 口罩检测预测
results = module.face_detection(data=input_dict, use_multi_scale=True, shrink=0.6, )
for result in results:
    print(result)
