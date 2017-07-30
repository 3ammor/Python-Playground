import tensorflow as tf
from model import MultilayerPerceptron
from config import multilayer_perceptron_config
from utils import create_dirs
from trainer import MultilayerPerceptronTrainer

tf.logging.set_verbosity(tf.logging.INFO)

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('exp_dir', "/tmp/multilayer-perceptron/", """ Experiment dir to store ckpt & summaries """)
tf.app.flags.DEFINE_boolean('is_train', True, """ Whether it is a training or testing""")
tf.app.flags.DEFINE_boolean('cont_train', True, """ whether to Load the Model and Continue Training or not """)
tf.app.flags.DEFINE_boolean('train_n_test', True, """ whether to Load the Model and Continue Training or not """)


def main(_):
    config = multilayer_perceptron_config()
    model = MultilayerPerceptron(config)

    sess = tf.Session()

    trainer = MultilayerPerceptronTrainer(sess, model, FLAGS)

    trainer.train()


if __name__ == '__main__':
    tf.app.run()
