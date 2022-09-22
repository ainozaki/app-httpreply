import numpy as np
import matplotlib.pyplot as plt


def main():
    elem = [[] for i in range(4)]
    clock = 3.8005123 # GHz

    ## extract data from logfile
    with open("log.txt") as f:
        while True:
            l = f.readline()
            if not l:
                break
            proto = int(l.split(" ")[0])
            for _ in range(1000):
                v = int(f.readline(), 16) / clock
                elem[proto].append(v)

        ## create figure  
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax1_cdf = ax1.twinx()
    ax2 = fig.add_subplot(2, 2, 2)
    ax2_cdf = ax2.twinx()
    ax3 = fig.add_subplot(2, 2, 3)
    ax3_cdf = ax3.twinx()
    ax4 = fig.add_subplot(2, 2, 4)
    ax4_cdf = ax4.twinx()
        
        ## x  
    x1 = np.array(range(len(elem[0])))
    x2 = np.array(range(len(elem[1])))
    x3 = np.array(range(len(elem[2])))
    x4 = np.array(range(len(elem[3])))
        
        ## y and y-CDF
    y1 = np.sort(np.array(elem[0]))
    y1_cdf = np.cumsum(y1) / np.sum(y1)
    y2 = np.sort(np.array(elem[1]))
    y2_cdf = np.cumsum(y2) / np.sum(y2)
    y3 = np.sort(np.array(elem[2]))
    y3_cdf = np.cumsum(y3) / np.sum(y3)
    y4 = np.sort(np.array(elem[3]))
    y4_cdf = np.cumsum(y4) / np.sum(y4)

        ## labels
    c1, c2, c3, c4, c5 = "blue", "green", "red", "cyan", "black"
    l1, l2, l3, l4, l5 = "input_ether", "input_ip", "input_udp", "input_tcp", "CDF"

        ## plot
    ax1.hist(y1, bins=100, label=l1, color=c1)
    ax1_cdf.plot(y1, y1_cdf, label=l5, color=c5, marker="o", markersize=1)
    ax2.hist(y2, bins=100, label=l2, color=c2)
    ax2_cdf.plot(y2, y2_cdf, label=l5, color=c5, marker="o", markersize=1)
    ax3.hist(y3, bins=100, label=l3, color=c3)
    ax3_cdf.plot(y3, y3_cdf, label=l5, color=c5, marker="o", markersize=1)
    ax4.hist(y4, bins=100, label=l4, color=c4)
    ax4_cdf.plot(y4, y4_cdf, label=l5, color=c5, marker="o", markersize=1)

        ## axes
    ax1.set_xlim(0, 6000)
    ax2.set_xlim(0, 6000)
    ax3.set_xlim(0, 6000)
    ax4.set_xlim(0, 6000)

    ax1.set_xlabel("time [ns]")
    ax1.set_ylabel("count")
    ax1_cdf.set_ylabel("CDF")
    ax2.set_xlabel("time [ns]")
    ax2.set_ylabel("count")
    ax2_cdf.set_ylabel("CDF")
    ax3.set_xlabel("time [ns]")
    ax3.set_ylabel("count")
    ax3_cdf.set_ylabel("CDF")
    ax4.set_xlabel("time [ns]")
    ax4.set_ylabel("count")
    ax4_cdf.set_ylabel("CDF")
	
        ## legends
    h1, l1 = ax1.get_legend_handles_labels()
    h1_cdf, l1_cdf = ax1_cdf.get_legend_handles_labels()
    ax1.legend(h1 + h1_cdf, l1 + l1_cdf)

    h2, l2 = ax2.get_legend_handles_labels()
    h2_cdf, l2_cdf = ax2_cdf.get_legend_handles_labels()
    ax2.legend(h2 + h2_cdf, l2 + l2_cdf)

    h3, l3 = ax3.get_legend_handles_labels()
    h3_cdf, l3_cdf = ax3_cdf.get_legend_handles_labels()
    ax3.legend(h3 + h3_cdf, l3 + l3_cdf)

    h4, l4 = ax4.get_legend_handles_labels()
    h4_cdf, l4_cdf = ax4_cdf.get_legend_handles_labels()
    ax4.legend(h4 + h4_cdf, l4 + l4_cdf)

        ## show
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
