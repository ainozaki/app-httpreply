import numpy as np
import math
import matplotlib.pyplot as plt
import sys

def main():
    argv = sys.argv
    if len(argv) < 2:
        print("usage:", argv[0], "<filename> <title>")
        return
    filename = argv[1]
    title = argv[2]
    elem = [[] for i in range(4)]
    clock = 3.8005123 # GHz
    proto = 0

    ## extract data from logfile
    with open(filename) as f:
        while True:
            l = f.readline().replace('\n', '')
            if not l:
                break
            if l == "ETHER":
                proto = 0
                print("Ether")
            elif l == "IP":
                proto = 1
                print("IP")
            elif l == "TCP":
                proto = 3
                print("TCP")
            else:
                v = int(l, 16) / clock
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
        
        ## data
    y1 = np.sort(np.array(elem[0]))
    y2 = np.sort(np.array(elem[1]))
    y3 = np.sort(np.array(elem[2]))
    y4 = np.sort(np.array(elem[3]))

        ## labels
    c1, c2, c3, c4, c5 = "blue", "green", "red", "cyan", "black"
    l1, l2, l3, l4, l5 = "input_ether", "input_ip", "input_udp", "input_tcp", "CDF"

        ## hist, cdf
    n, bins, _ = ax1.hist(y1, range=(0,1000), bins=100, label=l1, color=c1)
    x1_cdf = np.array([(bins[i] + bins[i+1])/2 for i in range(len(bins) - 1)])
    y1_cdf = np.cumsum(n) / np.sum(n)
    ax1_cdf.plot(x1_cdf, y1_cdf, label=l5, color=c5, marker="o", markersize=1)

    n, bins, _ = ax2.hist(y2, range=(0,1000), bins=100, label=l2, color=c2)
    x2_cdf = np.array([(bins[i] + bins[i+1])/2 for i in range(len(bins) - 1)])
    y2_cdf = np.cumsum(n) / np.sum(n)
    ax2_cdf.plot(x2_cdf, y2_cdf, label=l5, color=c5, marker="o", markersize=1)

    n, bins, _ = ax3.hist(y3, bins=100, label=l3, color=c3)
    x3_cdf = np.array([(bins[i] + bins[i+1])/2 for i in range(len(bins) - 1)])
    y3_cdf = np.cumsum(n) / np.sum(n)
    ax3_cdf.plot(x3_cdf, y3_cdf, label=l5, color=c5, marker="o", markersize=1)

#n, bins, _ = ax4.hist(y4, range=(0, 50000), bins=100, label=l4, color=c4)
    n, bins, _ = ax4.hist(y4, bins=100, label=l4, color=c4)
    x4_cdf = np.array([(bins[i] + bins[i+1])/2 for i in range(len(bins) - 1)])
    y4_cdf = np.cumsum(n) / np.sum(n)
    ax4_cdf.plot(x4_cdf, y4_cdf, label=l5, color=c5, marker="o", markersize=1)

        ## 90%, 99%
    ax1_cdf.axhline(y=0.9, color="red", linestyle='--')
    ax1_cdf.axhline(y=0.99, color="red", linestyle='--')
    ax2_cdf.axhline(y=0.9, color="red", linestyle='--')
    ax2_cdf.axhline(y=0.99, color="red", linestyle='--')
    ax4_cdf.axhline(y=0.9, color="red", linestyle='--')
    ax4_cdf.axhline(y=0.99, color="red", linestyle='--')


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

    ax1_cdf.set_ylim(0, 1)
    ax2_cdf.set_ylim(0, 1)
    ax3_cdf.set_ylim(0, 1)
    ax4_cdf.set_ylim(0, 1)
	
        ## legends
    h1, l1 = ax1.get_legend_handles_labels()
    h1_cdf, l1_cdf = ax1_cdf.get_legend_handles_labels()
    ax1.legend(h1 + h1_cdf, l1 + l1_cdf, loc="lower right")

    h2, l2 = ax2.get_legend_handles_labels()
    h2_cdf, l2_cdf = ax2_cdf.get_legend_handles_labels()
    ax2.legend(h2 + h2_cdf, l2 + l2_cdf, loc="lower right")

    h3, l3 = ax3.get_legend_handles_labels()
    h3_cdf, l3_cdf = ax3_cdf.get_legend_handles_labels()
    ax3.legend(h3 + h3_cdf, l3 + l3_cdf, loc="lower right")

    h4, l4 = ax4.get_legend_handles_labels()
    h4_cdf, l4_cdf = ax4_cdf.get_legend_handles_labels()
    ax4.legend(h4 + h4_cdf, l4 + l4_cdf, loc="lower right")

    print("======================");
    print("Data size:")
    print("ether:", len(y1))
    print("ip   :", len(y2))
    print("tcp  :", len(y4))
    print("======================");
    print("99% latency (", title, "):");
    print("ether: ", round(y1[math.floor(len(y1) * 0.9)], 2), " [ns]");
    print("ip   : ", round(y2[math.floor(len(y2) * 0.9)], 2), " [ns]");
    print("tcp  : ", round(y4[math.floor(len(y4) * 0.9)], 2), " [ns]");
    print("======================");

        ## show
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
