import tensorflow as tf
import os


def csv_read(filelist):
    # 构建文件队列
    file_queue = tf.train.string_input_producer(filelist)
    # 创建读取器，读取数据并解码
    reader = tf.TextLineReader()
    k, v = reader.read(file_queue)
    # 解码
    records = [['None'], ['None']]
    example, label = tf.decode_csv(v, record_defaults=records)
    # 批处理
    example_bat, label_bat = tf.train.batch([example, label], batch_size=9, num_threads=1)
    return example_bat, label_bat


if __name__ == '__main__':
    dir_name = './test_data/'
    file_names = os.listdir(dir_name)
    file_list = []
    for f in file_names:
        file_list.append(os.path.join(dir_name, f))

    example, label = csv_read(file_list)

    with tf.Session() as sess:
        coord = tf.train.Coordinator()  # 线程协调器
        # 返回一组线程
        threads = tf.train.start_queue_runners(sess, coord=coord)
        print(sess.run([example, label]))
        # 等待线程结束回收资源
        coord.request_stop()
        coord.join()
