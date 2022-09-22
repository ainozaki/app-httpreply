import numpy as np
import matplotlib.pyplot as plt


def main():
    elem = [[] for i in range(4)]

    with open("log.txt") as f:
        while True:
            l = f.readline()
            if not l:
                break
            proto = int(l.split(" ")[0])
            for _ in range(1000):
                v = int(f.readline(), 16)
                elem[proto].append(v)
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)
    x1 = np.array(range(len(elem[0])))
    x2 = np.array(range(len(elem[1])))
    x3 = np.array(range(len(elem[2])))
    x4 = np.array(range(len(elem[3])))
    y1 = np.array(elem[0])
    y2 = np.array(elem[1])
    y3 = np.array(elem[2])
    y4 = np.array(elem[3])
    c1, c2, c3, c4 = "blue", "green", "red", "yellow"
    l1, l2, l3, l4 = "input_ether", "input_ip", "input_udp", "input_tcp"
    ax1.plot(x1, y1, color=c1, label=l1,
             linestyle="None", marker="o", markersize=3)
    ax2.plot(x2, y2, color=c2, label=l2,
             linestyle="None", marker="o", markersize=3)
    ax3.plot(x3, y3, color=c3, label=l3,
             linestyle="None", marker="o", markersize=3)
    ax4.plot(x4, y4, color=c4, label=l4,
             linestyle="None", marker="o", markersize=3)
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
