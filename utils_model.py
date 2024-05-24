from utils_imports import *

from sklearn import metrics
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor,ExtraTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.ensemble import RandomForestRegressor,BaggingRegressor,GradientBoostingRegressor,AdaBoostRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split

import tensorflow as tf
from keras.models import Model,Sequential
from keras.layers import LSTM,Dense,Conv1D,Flatten,SimpleRNN,GRU
from keras.layers import Reshape,MaxPooling1D,BatchNormalization,Dropout
from keras.metrics import RootMeanSquaredError
from keras.callbacks import EarlyStopping,Callback



hidden_dim = [32,16]
epoch_whole = 300
batch_size = 32

def model_RNN(model,train_x):
    model.add(SimpleRNN(hidden_dim[0],return_sequences=True,input_shape=(1,train_x.shape[-1])))
    model.add(SimpleRNN(hidden_dim[1]))

def model_MLP(model,train_x):
    model.add(Dense(hidden_dim[0],activation='relu',input_shape=(1,train_x.shape[-1])))
    model.add(Flatten())
    model.add(Dense(hidden_dim[1],activation='relu'))

def model_LSTM(model,train_x):
    model.add(LSTM(hidden_dim[0],return_sequences=True,input_shape=(1,train_x.shape[-1])))
    model.add(LSTM(hidden_dim[1]))

def model_GRU(model,train_x):
    model.add(GRU(hidden_dim[0],return_sequences=True,input_shape=(1,train_x.shape[-1])))
    model.add(GRU(hidden_dim[1]))

def model_CNN(model,train_x):
    model.add(Conv1D(hidden_dim[0],kernel_size=3,padding='causal',strides=1,activation='relu',dilation_rate=1,input_shape=(train_x.shape[-1])))
    model.add(Conv1D(hidden_dim[1],kernel_size=3,padding='causal',strides=1,activation='relu',dilation_rate=2))
    model.add(Flatten())


def set_seed():
    os.environ['PYTHONHASHSEED'] = '0'
    np.random.seed(1)
    rn.seed(12345)
    tf.random.set_seed(123)