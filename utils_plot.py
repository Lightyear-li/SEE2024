from utils_imports import *
from matplotlib.collections import LineCollection


def plot_normal(df, x, y, title="", xlabel='xlabel', ylabel='ylabel', color='tab:red', subplot='111', dpi=100):
    if subplot == '111':
        plt.figure(figsize=(10,5))
        plt.plot(x, y, color=color)
        plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
        plt.show()
    else:
        if int(subplot[-1]) == 1:
            plt.figure(figsize=(10,5))

        plt.subplot(int(subplot))
        plt.plot(x, y, color=color)
        plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)

        if int(subplot[-1]) == int(subplot[0]) * int(subplot[1]):
            plt.show()



def plot_gradient_colormap(x, y, title="", xlabel='xlabel', ylabel='ylabel', colormap='viridis_r', dpi=100):
    xy = np.stack((x, y), axis=1)
    segments = np.stack((xy[:-1], xy[1:]), axis=1)

    colors = color_map(x[:-1], colormap)
    colors = color_map(y[:-1], colormap)
    line_segments = LineCollection(segments, colors=colors, linewidths=5, cmap=colormap)

    fig = plt.figure(figsize=(10,5))
    ax = plt.axes()
    ax.add_collection(line_segments)
    ax.scatter(1,1,s=0)
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()
    


def color_map(data, cmap):
    dmin, dmax = np.nanmin(data), np.nanmax(data)
    cmo = plt.cm.get_cmap(cmap)
    cs, k = list(), 256/cmo.N
    
    for i in range(cmo.N):
        c = cmo(i)
        for j in range(int(i*k), int((i+1)*k)):
            cs.append(c)
    cs = np.array(cs)
    data = np.uint8(255*(data-dmin)/(dmax-dmin))
    
    return cs[data]



def plot_model(x_test, y_test, y_pred, title="", xlabel='xlabel', ylabel='ylabel', color_test='tab:red', color_pred='blue', dpi=100):
    plt.figure(figsize=(10,5))
    plt.plot(x_test, y_test, c=color_test, label='test')
    plt.plot(x_test, y_pred, c=color_pred, label='pred')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()