from turtle import color
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import argparse
import os


def dual_tests():

    for i in range(3):
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, sharey=True)
        plt.subplots_adjust(hspace=0.3)
        fig.set_figwidth(4)
        fig.set_figheight(8)
        fig.tight_layout()
        data = pd.read_csv(os.path.join('results', 'test_dual_{}.csv'.format(i)),
            delimiter=";", header=0, index_col='Time');
        data_1 = data[data.index <= 0.5]
    
        ax1.plot(data_1['a x'], data_1['a y'], color='red')
        ax1.plot(data_1['b x'], data_1['b y'], color='blue')
        ax1.set_aspect('equal', adjustable='box')
        ax1.set_title("$t = 0.50\\,\\tau$")
        ax1.set_xlabel("$x$ [m]", fontsize=18)
        ax1.set_ylabel("$y$ [m]", fontsize=18)

        ax2.plot(data['a x'][0:100], data['a y'][0:100], color='red')
        ax2.plot(data['b x'][0:100], data['b y'][0:100], color='blue')
        ax2.set_aspect('equal', adjustable='box')
        ax2.set_title("$t = 1.00\\,\\tau$")
        ax2.set_xlabel("$x$ [m]", fontsize=18)
        ax2.set_ylabel("$y$ [m]", fontsize=18)

        plt.show()

def dual_diff(nfile):
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    fig.set_figwidth(8)

    data = pd.read_csv(os.path.join('results', 'test_dual_{}.csv'.format(nfile)),
            delimiter=";", header=0, index_col='Time')

    ax1.plot(
        data.index,
        data['a x'] - (0.25 * np.cos(- 4 * data.index + np.pi))
    )
    ax1.set_ylabel('$\Delta x$ [m]', fontsize=18)
    
    ax2.plot(
        data.index,
        data['a y'] - (0.25 * np.sin(- 4 * data.index + np.pi))
    )
    ax2.set_ylabel('$\Delta y$ [m]', fontsize=18)
    ax2.set_xlabel('$t$ [$\\tau$]', fontsize=18)

    plt.show()

def sun_earth_jupiter():
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    fig.set_figwidth(8)
    fig.set_figheight(8)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_1.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[0, 0].plot(data['a x'], data['a y'], color = 'orange')
    axs[0, 0].plot(data['b x'], data['b y'], color = 'green')
    axs[0, 0].plot(data['c x'], data['c y'], color = 'red')

    axs[0, 0].set_xlabel('$x$ [au]', fontsize=18)
    axs[0, 0].set_ylabel('$y$ [au]', fontsize=18)
    axs[0, 0].set_title('$M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_10.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[0, 1].plot(data['a x'], data['a y'], color = 'orange')
    axs[0, 1].plot(data['b x'], data['b y'], color = 'green')
    axs[0, 1].plot(data['c x'], data['c y'], color = 'red')

    axs[0, 1].set_xlabel('$x$ [au]', fontsize=18)
    axs[0, 1].set_ylabel('$y$ [au]', fontsize=18)
    axs[0, 1].set_title('$10 M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_100.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 0].plot(data['a x'], data['a y'], color = 'orange')
    axs[1, 0].plot(data['b x'], data['b y'], color = 'green')
    axs[1, 0].plot(data['c x'], data['c y'], color = 'red')

    axs[1, 0].set_xlabel('$x$ [au]', fontsize=18)
    axs[1, 0].set_ylabel('$y$ [au]', fontsize=18)
    axs[1, 0].set_title('$100 M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_1000.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 1].plot(data['a x'], data['a y'], color = 'orange')
    axs[1, 1].plot(data['b x'], data['b y'], color = 'green')
    axs[1, 1].plot(data['c x'], data['c y'], color = 'red')

    axs[1, 1].set_xlabel('$x$ [au]', fontsize=18)
    axs[1, 1].set_ylabel('$y$ [au]', fontsize=18)
    axs[1, 1].set_title('$1000 M_J$', x=0.2)

    plt.show()

def sun_earth_jupiter_special():
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    fig.set_figwidth(8)
    fig.set_figheight(8)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_special_1.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[0, 0].plot(data['a x'], data['a y'], color = 'orange')
    axs[0, 0].plot(data['b x'], data['b y'], color = 'green')
    axs[0, 0].plot(data['c x'], data['c y'], color = 'red')

    axs[0, 0].set_xlabel('$x$ [au]', fontsize=18)
    axs[0, 0].set_ylabel('$y$ [au]', fontsize=18)
    axs[0, 0].set_title('$M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_special_10.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[0, 1].plot(data['a x'], data['a y'], color = 'orange')
    axs[0, 1].plot(data['b x'], data['b y'], color = 'green')
    axs[0, 1].plot(data['c x'], data['c y'], color = 'red')

    axs[0, 1].set_xlabel('$x$ [au]', fontsize=18)
    axs[0, 1].set_ylabel('$y$ [au]', fontsize=18)
    axs[0, 1].set_title('$10 M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_special_100.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 0].plot(data['a x'], data['a y'], color = 'orange')
    axs[1, 0].plot(data['b x'], data['b y'], color = 'green')
    axs[1, 0].plot(data['c x'], data['c y'], color = 'red')

    axs[1, 0].set_xlabel('$x$ [au]', fontsize=18)
    axs[1, 0].set_ylabel('$y$ [au]', fontsize=18)
    axs[1, 0].set_title('$100 M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_special_1000.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 1].plot(data['a x'], data['a y'], color = 'orange')
    axs[1, 1].plot(data['b x'], data['b y'], color = 'green')
    axs[1, 1].plot(data['c x'], data['c y'], color = 'red')

    axs[1, 1].set_xlabel('$x$ [au]', fontsize=18)
    axs[1, 1].set_ylabel('$y$ [au]', fontsize=18)
    axs[1, 1].set_title('$1000 M_J$', x=0.2)

    plt.show()

def sun_earth_jupiter_relative():
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    fig.set_figwidth(8)
    fig.set_figheight(8)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_1.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[0, 0].scatter([0], [0], marker='*', color='orange')
    axs[0, 0].plot(data['b x'] - data['a x'], data['b y'] - data['a y'], color = 'green')
    axs[0, 0].plot(data['c x'] - data['a x'], data['c y'] - data['a y'], color = 'red')
    
    axs[0, 0].set_xlabel('$x$ [au]', fontsize=18)
    axs[0, 0].set_ylabel('$y$ [au]', fontsize=18)
    axs[0, 0].set_title('$M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_10.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[0, 1].scatter([0], [0], marker='*', color='orange')
    axs[0, 1].plot(data['b x'] - data['a x'], data['b y'] - data['a y'], color = 'green')
    axs[0, 1].plot(data['c x'] - data['a x'], data['c y'] - data['a y'], color = 'red')

    axs[0, 1].set_xlabel('$x$ [au]', fontsize=18)
    axs[0, 1].set_ylabel('$y$ [au]', fontsize=18)
    axs[0, 1].set_title('$10 M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_100.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 0].scatter([0], [0], marker='*', color='orange')
    axs[1, 0].plot(data['b x'] - data['a x'], data['b y'] - data['a y'], color = 'green')
    axs[1, 0].plot(data['c x'] - data['a x'], data['c y'] - data['a y'], color = 'red')

    axs[1, 0].set_xlabel('$x$ [au]', fontsize=18)
    axs[1, 0].set_ylabel('$y$ [au]', fontsize=18)
    axs[1, 0].set_title('$100 M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_1000.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 1].scatter([0], [0], marker='*', color='orange')
    axs[1, 1].plot(data['b x'] - data['a x'], data['b y'] - data['a y'], color = 'green')
    axs[1, 1].plot(data['c x'] - data['a x'], data['c y'] - data['a y'], color = 'red')

    axs[1, 1].set_xlabel('$x$ [au]', fontsize=18)
    axs[1, 1].set_ylabel('$y$ [au]', fontsize=18)
    axs[1, 1].set_title('$1000 M_J$', x=0.2)

    plt.show()

def sun_earth_jupiter_special_relative():
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    fig.set_figwidth(8)
    fig.set_figheight(8)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_special_1.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[0, 0].scatter([0], [0], marker='*', color='orange')
    axs[0, 0].plot(data['b x'] - data['a x'], data['b y'] - data['a y'], color = 'green')
    axs[0, 0].plot(data['c x'] - data['a x'], data['c y'] - data['a y'], color = 'red')
    
    axs[0, 0].set_xlabel('$x$ [au]', fontsize=18)
    axs[0, 0].set_ylabel('$y$ [au]', fontsize=18)
    axs[0, 0].set_title('$M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_special_10.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[0, 1].scatter([0], [0], marker='*', color='orange')
    axs[0, 1].plot(data['b x'] - data['a x'], data['b y'] - data['a y'], color = 'green')
    axs[0, 1].plot(data['c x'] - data['a x'], data['c y'] - data['a y'], color = 'red')

    axs[0, 1].set_xlabel('$x$ [au]', fontsize=18)
    axs[0, 1].set_ylabel('$y$ [au]', fontsize=18)
    axs[0, 1].set_title('$10 M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_special_100.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 0].scatter([0], [0], marker='*', color='orange')
    axs[1, 0].plot(data['b x'] - data['a x'], data['b y'] - data['a y'], color = 'green')
    axs[1, 0].plot(data['c x'] - data['a x'], data['c y'] - data['a y'], color = 'red')

    axs[1, 0].set_xlabel('$x$ [au]', fontsize=18)
    axs[1, 0].set_ylabel('$y$ [au]', fontsize=18)
    axs[1, 0].set_title('$100 M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_special_1000.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 1].scatter([0], [0], marker='*', color='orange')
    axs[1, 1].plot(data['b x'] - data['a x'], data['b y'] - data['a y'], color = 'green')
    axs[1, 1].plot(data['c x'] - data['a x'], data['c y'] - data['a y'], color = 'red')

    axs[1, 1].set_xlabel('$x$ [au]', fontsize=18)
    axs[1, 1].set_ylabel('$y$ [au]', fontsize=18)
    axs[1, 1].set_title('$1000 M_J$', x=0.2)

    plt.show()

def sun_earth_jupiter_diff():
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    fig.set_figwidth(10)
    fig.set_figheight(8)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_1.csv'),
            delimiter=";", header=0, index_col='Time')
    control = data['b x'] - data['a x']
    axs[0, 0].plot(data.index, control - control, color = 'green')
    
    axs[0, 0].set_xlabel('$t$ [yr]', fontsize=18)
    axs[0, 0].set_ylabel('$\Delta_x$ [au]', fontsize=18)
    axs[0, 0].set_title('$M_J$')

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_10.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[0, 1].plot(data.index, data['b x'] - data['a x'] - control, color = 'green')
    
    axs[0, 1].set_xlabel('$t$ [yr]', fontsize=18)
    axs[0, 1].set_ylabel('$\Delta_x$ [au]', fontsize=18)
    axs[0, 1].set_title('$10 M_J$')

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_100.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 0].plot(data.index, data['b x'] - data['a x'] - control, color = 'green')
    
    axs[1, 0].set_xlabel('$t$ [yr]', fontsize=18)
    axs[1, 0].set_ylabel('$\Delta_x$ [au]', fontsize=18)
    axs[1, 0].set_title('$100 M_J$')

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_1000.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 1].plot(data.index, data['b x'] - data['a x'] - control.iloc[0:225000], color = 'green')
    
    axs[1, 1].set_xlabel('$t$ [yr]', fontsize=18)
    axs[1, 1].set_ylabel('$\Delta_x$ [au]', fontsize=18)
    axs[1, 1].set_title('$1000 M_J$')

    plt.show()

def sun_earth_jupiter_special_diff():
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    fig.set_figwidth(10)
    fig.set_figheight(8)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_1.csv'),
            delimiter=";", header=0, index_col='Time')
    control = data['b x'] - data['a x']
    axs[0, 0].plot(data.index, control - control, color = 'green')

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_special_1.csv'),
            delimiter=";", header=0, index_col='Time')
    controlb = data['b x'] - data['a x']
    axs[0, 0].plot(data.index, data['b x'] - data['a x'] - controlb, color = 'red')
    
    axs[0, 0].set_xlabel('$t$ [yr]', fontsize=18)
    axs[0, 0].set_ylabel('$\Delta_x$ [au]', fontsize=18)
    axs[0, 0].set_title('$M_J$')

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_10.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[0, 1].plot(data.index, data['b x'] - data['a x'] - control, color = 'green')
    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_special_10.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[0, 1].plot(data.index, data['b x'] - data['a x'] - controlb, color = 'red')
    
    axs[0, 1].set_xlabel('$t$ [yr]', fontsize=18)
    axs[0, 1].set_ylabel('$\Delta_x$ [au]', fontsize=18)
    axs[0, 1].set_title('$10 M_J$')

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_100.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 0].plot(data.index, data['b x'] - data['a x'] - control, color = 'green')
    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_special_100.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 0].plot(data.index, data['b x'] - data['a x'] - controlb, color = 'red')
    
    axs[1, 0].set_xlabel('$t$ [yr]', fontsize=18)
    axs[1, 0].set_ylabel('$\Delta_x$ [au]', fontsize=18)
    axs[1, 0].set_title('$100 M_J$')

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_1000.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 1].plot(data.index, data['b x'] - data['a x'] - control.iloc[0:225000], color = 'green')
    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_special_1000.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 1].plot(data.index, data['b x'] - data['a x'] - controlb.iloc[0:225000], color = 'red')
    
    axs[1, 1].set_xlabel('$t$ [yr]', fontsize=18)
    axs[1, 1].set_ylabel('$\Delta_x$ [au]', fontsize=18)
    axs[1, 1].set_title('$1000 M_J$')

    plt.show()

def sun_earth_jupiter_attraction():
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    fig.set_figwidth(8)
    fig.set_figheight(8)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_1_attraction.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[0, 0].plot(data.index, data['F_ab'], color = 'orange')
    axs[0, 0].plot(data.index, data['F_bc'], color = 'red')

    axs[0, 0].set_yscale('log')
    axs[0, 0].set_xlabel('$t$ [yr]', fontsize=18)
    axs[0, 0].set_ylabel('$a$ [au/yr$^2$]', fontsize=18)
    axs[0, 0].set_title('$M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_10_attraction.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[0, 1].plot(data.index, data['F_ab'], color = 'orange')
    axs[0, 1].plot(data.index, data['F_bc'], color = 'red')

    axs[0, 1].set_yscale('log')
    axs[0, 1].set_xlabel('$t$ [yr]', fontsize=18)
    axs[0, 1].set_ylabel('$a$ [au/yr$^2$]', fontsize=18)
    axs[0, 1].set_title('$10 M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_100_attraction.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 0].plot(data.index, data['F_ab'], color = 'orange')
    axs[1, 0].plot(data.index, data['F_bc'], color = 'red')

    axs[1, 0].set_yscale('log')
    axs[1, 0].set_xlabel('$t$ [yr]', fontsize=18)
    axs[1, 0].set_ylabel('$a$ [au/yr$^2$]', fontsize=18)
    axs[1, 0].set_title('$100 M_J$', x=0.2)

    data = pd.read_csv(os.path.join('results', 'sun_earth_jupiter_1000_attraction.csv'),
            delimiter=";", header=0, index_col='Time')
    axs[1, 1].plot(data.index, data['F_ab'], color = 'orange')
    axs[1, 1].plot(data.index, data['F_bc'], color = 'red')

    axs[1, 1].set_yscale('log')
    axs[1, 1].set_xlabel('$t$ [yr]', fontsize=18)
    axs[1, 1].set_ylabel('$a$ [au/yr$^2$]', fontsize=18)
    axs[1, 1].set_title('$1000 M_J$', x=0.2)

    plt.show()

def dual_convergence_x():
    fig, ax = plt.subplots(1, 1, sharex=True, sharey=True)
    fig.set_figwidth(8)
    fig.set_figheight(8)

    data = pd.read_csv(os.path.join('results', 'convergence.csv'),
            delimiter=";", header=0)

    ax.plot(data["dt"][2:], data['error x'][2:], color='red')
    ax.set_ylabel("$x_{err}$ [m]")
    ax.set_xlabel("Timestep [$\\tau$]")

    plt.show()

def dual_convergence_r():
    fig, ax = plt.subplots(1, 1, sharex=True, sharey=True)
    fig.set_figwidth(8)
    fig.set_figheight(8)

    data = pd.read_csv(os.path.join('results', 'convergence.csv'),
            delimiter=";", header=0)

    ax.plot(data["dt"][2:], data['error r'][2:], color='red')
    ax.set_ylabel("$|r|^2_{err}$ [m$^2$]")
    ax.set_xlabel("Timestep [$\\tau$]")

    plt.show()

def main():

    parser = argparse.ArgumentParser(description='Plot a result file.')
    parser.add_argument('-m', '--mode',
                    default='',
                    help='file name')
    args = parser.parse_args()

    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica"],
        "font.size": 14})

    if args.mode == 'dual_tests':
        dual_tests()
    elif args.mode == 'dual_diff':
        dual_diff(3)
    elif args.mode == 'dual_diff_p':
        dual_diff(4)
    elif args.mode == 'dual_conv':
        dual_convergence_x()
        dual_convergence_r()
    elif args.mode == 'sej':
        plt.rcParams['axes.titley'] = 0.9
        sun_earth_jupiter()
        sun_earth_jupiter_relative()
        sun_earth_jupiter_diff()
    elif args.mode == 'attraction':
        plt.rcParams['axes.titley'] = 0.9
        sun_earth_jupiter_attraction()
    elif args.mode == 'sej_special':
        plt.rcParams['axes.titley'] = 0.9
        sun_earth_jupiter_special()
        sun_earth_jupiter_special_relative()
        sun_earth_jupiter_special_diff()


if __name__ == '__main__':
    main()