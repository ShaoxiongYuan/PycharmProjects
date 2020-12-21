import tensorflow as tf
import os

tf.compat.v1.disable_eager_execution()


def csv_read(filelist):
    file_queue = tf.compat.v1.train.string_input_producer(filelist)

    reader = tf.compat.v1.TextLineReader()
    k, v = reader.read(file_queue)

    records = [['None'], ['None']]
    example, label = tf.io.decode_csv(records=v, record_defaults=records)

    example_bat, label_bat = tf.compat.v1.train.batch([example, label], batch_size=9, num_threads=1)
    return example_bat, label_bat


if __name__ == '__main__':
    dir_name = './test_data/'
    file_names = os.listdir(dir_name)
    file_list = []
    for f in file_names:
        file_list.append(os.path.join(dir_name, f))

    example, label = csv_read(file_list)

    with tf.compat.v1.Session() as sess:
        coord = tf.train.Coordinator()

        threads = tf.compat.v1.train.start_queue_runners(sess, coord=coord)
        print(sess.run([example, label]))

        coord.request_stop()
        coord.join()
