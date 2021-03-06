# Bayes By Backprop & Planning

## Model
Bayesian Neural Networks (BNNs) extend standard neural networks with posterior inference. By learning weights as probability distributions over possible values, BNNs are able to quantify epistemic uncertainty. The main BNN model used in this project `bnn3` is stored in the `models` folder. 

## Regression in 1D
Run/uncomment the function `run_reg()` in `main.py`. Can also change hyperparameter settings for 1D regression in the function `reg_hp()` in `hparams.py`.

![plot](plots/reg_1d.jpg)

## Regression in 2D
Run/uncomment the function `run_reg_2d()` in `main.py`. Can also change hyperparameter settings for 2D regression in the function `reg_2d_hp()` in `hparams.py`.

![plot](plots/reg_2d_1.jpg)
![plot](plots/reg_2d_2.jpg)

## Navigation
Run/uncomment the function `run_nav()` in `main.py`. Can also change hyperparameter settings in the function `nav_hp()` in `hparams.py`. 

![plot](plots/nav.jpg)

## Classification
Run `bbb_torch_colab.py` in the `notebooks` folder. 

![plot](plots/class.jpg)