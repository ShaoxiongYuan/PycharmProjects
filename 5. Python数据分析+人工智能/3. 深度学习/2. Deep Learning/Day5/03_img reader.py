import tensorflow as tf
import os
import matplotlib.pyplot as plt


def img_read(filelist):
    # 1. 构建文件队列
    file_queue = tf.train.string_input_producer(filelist)
    # 2. 构建reader读取文件内容，默认读取一张图片
    reader = tf.WholeFileReader()
    k, v = reader.read(file_queue)
    # 3. 对每行内容进行解码
    img = tf.image.decode_jpeg(v)  # 每行两个值
    # 4. 批处理, 图片需要处理成统一大小
    img_resized = tf.image.resize(img, [200, 200])  # 200*200
    img_resized.set_shape([200, 200, 3])
    img_bat = tf.train.batch([img_resized],
                             batch_size=10,
                             num_threads=1)
    return img_bat


if __name__ == "__main__":
    # 1. 找到文件，构造一个列表
    dir_name = "./test_img/"
    file_names = os.listdir(dir_name)
    file_list = []
    for f in file_names:
        file_list.append(os.path.join(dir_name, f))  # 拼接目录和文件名
    imgs = img_read(file_list)
    # 开启session运行结果
    with tf.Session() as sess:
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess, coord=coord)
        # print(sess.run([imgs])) # 打印读取的内容

        imgs = imgs.eval()
        # 回收线程
        coord.request_stop()
        coord.join(threads)

    # 显示图片
    print(imgs.shape)

    plt.figure("Img Show", facecolor="lightgray")
    for i in range(10):
        plt.subplot(2, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(imgs[i].astype("int32"))
    plt.tight_layout()
    plt.show()
