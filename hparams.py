import math
import numpy as np
import torch


class BBBHparams(object):
    def __init__(self) -> None:
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")


def mnist_hp():
    hp = BBBHparams()
    hp.n_epochs = 10

    hp.n_input = 784
    hp.n_output = 10
    hp.hidden_units = 30

    hp.batch_size = 10000

    hp.classes = 10
    hp.n_samples = 3
    # hp.test_samples = 10

    hp.pi = 0.5
    # hp.sigma_prior1 = torch.FloatTensor([math.exp(-0)])
    # hp.sigma_prior2 = torch.FloatTensor([math.exp(-6)])
    hp.sigma_prior1 = 1
    hp.sigma_prior2 = 0.3
    hp.noise_tol = .03

    hp.task = 'classification'
    hp.prior = "gaussian"
    hp.activation = 'relu'

    return hp


def reg_hp():
    hp = BBBHparams()
    hp.noise = 0.03
    hp.n_epochs = 9000

    hp.n_input = 1
    hp.n_output = 1
    hp.hidden_units = 9

    hp.train_size = 60
    hp.val_size = 30
    # hp.test_size = 30
    hp.n_train_batches = 3
    hp.batch_size = int(hp.train_size / hp.n_train_batches)

    hp.pred_samples = 1000
    hp.eval_samples = 10

    # hp.sigma_prior1 = torch.FloatTensor([math.exp(-0)])
    # hp.sigma_prior2 = torch.FloatTensor([math.exp(-6)])
    hp.sigma_prior1 = 6
    hp.sigma_prior2 = 3
    hp.pi = 0.5
    hp.noise_tol = .03
    hp.prior = "gaussian"

    hp.n_samples = 3
    hp.learning_rate = 0.01
    hp.task = 'regression'
    hp.activation = 'sigmoid'

    hp.plot_progress = False
    hp.plot_loss = False

    # MoG ground truth
    hp.m1 = 1.2
    hp.s1 = 0.3
    hp.m2 = 2.4
    hp.s2 = 0.6

    return hp


def reg_ncp():
    hp = reg_hp()
    hp.n_epochs = 3000

    hp.sigma_x = 0.3
    hp.sigma_y = 0.3

    hp.pred_samples = 300

    return hp


def reg_2d_hp():
    hp = reg_hp()
    hp.n_input = 2
    hp.hidden_units = 15

    hp.n_epochs = 3000
    hp.learning_rate = 0.01
    hp.pred_samples = 1000

    hp.sigma_prior1 = 6
    hp.prior = "gaussian"

    hp.grid = np.mgrid[-3.3:3.3:0.3, -3.3:3.3:0.3]

    # Gaussian ground truth
    hp.mean = np.array([0., 1.])
    hp.covariance = np.array([[1, 0.8], [0.8, 1]])

    return hp


def nav_hp():
    hp = reg_hp()

    hp.n_input = 2

    hp.learning_rate = 0.01
    hp.n_epochs = 3000
    hp.hidden_units = 30

    hp.bound = 6.0
    hp.grid = np.mgrid[0:hp.bound + 0.6:0.6, 0:hp.bound + 0.6:0.6]
    hp.init_state = torch.tensor([0.3, 0.6])
    hp.goal_state = torch.tensor([5.4, 5.4])

    hp.sigma_prior1 = 3
    hp.noise = 0.3
    hp.activation = 'linear'

    return hp


def colab_hparams():
    hp = BBBHparams()
    hp.n_samples = 3
    hp.sigma_prior = float(np.exp(-3))
    hp.learning_rate = 0.001
    hp.batch_size = 1000

    return hp
