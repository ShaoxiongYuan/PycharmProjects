import tensorflow as tf
import os
import matplotlib.pyplot as plt

tf.compat.v1.disable_eager_execution()


def img_read(filelist):
    file_queue = tf.compat.v1.train.string_input_producer(filelist)

    reader = tf.compat.v1.WholeFileReader()
    k, v = reader.read(file_queue)

    img = tf.image.decode_jpeg(v)

    img_resized = tf.image.resize(img, [200, 200])
    img_resized.set_shape([200, 200, 3])
    img_bat = tf.compat.v1.train.batch([img_resized],
                                       batch_size=10,
                                       num_threads=1)
    return img_bat


if __name__ == "__main__":

    dir_name = "./test_img/"
    file_names = os.listdir(dir_name)
    file_list = []
    for f in file_names:
        file_list.append(os.path.join(dir_name, f))
    imgs = img_read(file_list)

    with tf.compat.v1.Session() as sess:
        coord = tf.train.Coordinator()
        threads = tf.compat.v1.train.start_queue_runners(sess, coord=coord)

        imgs = imgs.eval()

        coord.request_stop()
        coord.join(threads)

    print(imgs.shape)

    plt.figure("Img Show", facecolor="lightgray")
    for i in range(10):
        plt.subplot(2, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(imgs[i].astype("int32"))
    plt.tight_layout()
    plt.show()
