import numpy as np
import matplotlib.pyplot as plt
import sys


def main():
    argv = sys.argv
    if len(argv) < 2:
        print("usage:", argv[0], "<filename>")
        return
    elem = [[] for i in range(6)]
    scatter = [[] for i in range(4)]
    clock = 3.8005123  # GHz

    # extract data from logfile
    with open(argv[1]) as f:
        while True:
            l = f.readline()
            if not l:
                break
            title = l.split(" ")
            if len(title) == 1:
                for _ in range(100):
                    plots = f.readline().replace("\n", "").split(" ")
                    scatter[0].append(int(plots[0], 16) / clock)
                    scatter[1].append(int(plots[1], 16))
                    scatter[2].append(int(plots[2], 16))
                    scatter[3].append(int(plots[3], 16))
            else:
                print(title)
                proto = int(title[0])
                for _ in range(100):
                    v = int(f.readline(), 16) / clock
                    elem[proto].append(v)

        # create figure
    fig1 = plt.figure()
    fig2 = plt.figure()
    ax1 = fig1.add_subplot(2, 2, 1)
    ax1_cdf = ax1.twinx()
    ax2 = fig1.add_subplot(2, 2, 2)
    ax2_cdf = ax2.twinx()
#ax3 = fig1.add_subplot(2, 3, 3)
#   ax3_cdf = ax3.twinx()
    ax41 = fig1.add_subplot(2, 2, 3)
    ax42 = fig1.add_subplot(2, 2, 4)
#ax43 = fig1.add_subplot(2, 3, 6)
    ax51 = fig2.add_subplot(2, 2, 1)
    ax52 = fig2.add_subplot(2, 2, 2)
    ax53 = fig2.add_subplot(2, 2, 3)

    # x
    x1 = np.array(range(len(elem[0])))
    x2 = np.array(range(len(elem[1])))
#x3 = np.array(range(len(elem[2])))
    x41 = np.array(range(len(elem[3])))
    x42 = np.array(range(len(elem[4])))
#x43 = np.array(range(len(elem[5])))
    x5 = scatter[0]

    # y and y-CDF
    y1 = np.sort(np.array(elem[0]))
    y1_cdf = np.cumsum(y1) / np.sum(y1)
    y2 = np.sort(np.array(elem[1]))
    y2_cdf = np.cumsum(y2) / np.sum(y2)
#y3 = np.sort(np.array(elem[2]))
#y3_cdf = np.cumsum(y3) / np.sum(y3)
    y41 = np.sort(np.array(elem[3]))
    y42 = np.sort(np.array(elem[4]))
#y43 = np.sort(np.array(elem[5]))
    y51 = scatter[1]
    y52 = scatter[2]
    y53 = scatter[3]

    # labels
    c1, c2, c3, c4, c5 = "blue", "green", "red", "cyan", "black"
    l1, l2, l3, l4, l5 = "input_ether", "input_ip", "input_udp", "input_tcp", "CDF"
    l41, l42, l43 = "tcp-established", "tcp-listen-syn", "tcp-listen-ack"
    l51, l52, l53 = "tcphdr->wnd", "rcv_wnd", "snd_wnd"

    # plot
    ax1.hist(y1, bins=100, label=l1, color=c1)
    ax1_cdf.plot(y1, y1_cdf, label=l5, color=c5, marker="o", markersize=1)
    ax2.hist(y2, bins=100, label=l2, color=c2)
    ax2_cdf.plot(y2, y2_cdf, label=l5, color=c5, marker="o", markersize=1)
#ax3.hist(y3, bins=100, label=l3, color=c3)
#ax3_cdf.plot(y3, y3_cdf, label=l5, color=c5, marker="o", markersize=1)
    ax41.hist(y41, bins=100, label=l41, color=c3)
    ax42.hist(y42, bins=100, label=l42, color=c3)
#ax43.hist(y43, bins=100, label=l4, color=c3)
    ax51.scatter(x5, y51, label=l4, color=c1)
    ax52.scatter(x5, y52, label=l4, color=c2)
    ax53.scatter(x5, y53, label=l4, color=c3)

    # axes
# ax1.set_xlim(0, 6000)
# ax2.set_xlim(0, 6000)
# ax3.set_xlim(0, 6000)
# ax4.set_xlim(0, 6000)

    ax1.set_xlabel("time [ns]")
    ax1.set_ylabel("count")
    ax1_cdf.set_ylabel("CDF")
    ax2.set_xlabel("time [ns]")
    ax2.set_ylabel("count")
    ax2_cdf.set_ylabel("CDF")
#ax3.set_xlabel("time [ns]")
#ax3.set_ylabel("count")
#ax3_cdf.set_ylabel("CDF")
    ax41.set_xlabel("time [ns]")
    ax41.set_ylabel("count")
    ax42.set_xlabel("time [ns]")
    ax42.set_ylabel("count")
#ax43.set_xlabel("time [ns]")
#ax43.set_ylabel("count")
    ax51.set_xlabel("time [ns]")
    ax51.set_ylabel("tcphdr->wnd")
    ax52.set_xlabel("time [ns]")
    ax52.set_ylabel("rcv_wnd")
    ax53.set_xlabel("time [ns]")
    ax53.set_ylabel("snd_wnd")

    # legends
    h1, l1 = ax1.get_legend_handles_labels()
    h1_cdf, l1_cdf = ax1_cdf.get_legend_handles_labels()
    ax1.legend(h1 + h1_cdf, l1 + l1_cdf)

    h2, l2 = ax2.get_legend_handles_labels()
    h2_cdf, l2_cdf = ax2_cdf.get_legend_handles_labels()
    ax2.legend(h2 + h2_cdf, l2 + l2_cdf)

#h3, l3 = ax3.get_legend_handles_labels()
#h3_cdf, l3_cdf = ax3_cdf.get_legend_handles_labels()
#ax3.legend(h3 + h3_cdf, l3 + l3_cdf)

    ax41.legend()
    ax42.legend()
#ax43.legend()

    # show
    fig1.tight_layout()
    fig2.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
