import numpy as np
import matplotlib.pyplot as plt
import sys

def main():
    argv = sys.argv
    if len(argv) < 2:
        print("usage:", argv[0], "<filename>")
        return
    elem = [[] for i in range(4)]
    clock = 3.8005123 # GHz

    ## extract data from logfile
    with open(argv[1]) as f:
        while True:
            l = f.readline()
            if not l:
                break
            blockno = int(l.split(", ")[0])
            for _ in range(100):
                v = f.readline().split(" ")
                for i in range(3):
                    elem[i].append(int(v[i], 16) / clock)

        ## create figure  
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax1_cdf = ax1.twinx()
    ax2 = fig.add_subplot(2, 2, 2)
    ax2_cdf = ax2.twinx()
    ax3 = fig.add_subplot(2, 2, 3)
    ax3_cdf = ax3.twinx()
        
        ## x  
    x1 = np.array(range(len(elem[0])))
    x2 = np.array(range(len(elem[1])))
    x3 = np.array(range(len(elem[2])))
        
        ## y
    y1 = np.sort(np.array(elem[0]))
    y2 = np.sort(np.array(elem[1]))
    y3 = np.sort(np.array(elem[2]))

        ## labels
    c1, c2, c3, c4 = "blue", "green", "red", "cyan"
    l1, l2, l3, l4 = "tcp_listen_part0_0", "tcp_listen_part0_1", "tcp_listen_part0_2", "tcp_listen_part0_3"

        ## plot
    ax1.hist(y1, bins=100, label=l1, color=c1)
    ax2.hist(y2, bins=100, label=l2, color=c2)
    ax3.hist(y3, bins=100, label=l3, color=c3)

    ax1.set_xlabel("time [ns]")
    ax1.set_ylabel("count")
    ax2.set_xlabel("time [ns]")
    ax2.set_ylabel("count")
    ax3.set_xlabel("time [ns]")
    ax3.set_ylabel("count")
	
        ## legends
    ax1.legend()
    ax2.legend()
    ax3.legend()

        ## show
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
