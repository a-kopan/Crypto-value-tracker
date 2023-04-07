import numpy as np
import matplotlib.pyplot as plt
import APIDataLoading as APIDL
import mplcursors

def drawGraph(time, cryptoOfChoice, convertInto):
    x_points = np.array(range(0,time+1))

    # Invert the x-axis
    plt.gca().invert_xaxis()
    data = APIDL.getApiData(time, cryptoOfChoice, convertInto)
    for currency in cryptoOfChoice.split(","):
        y_points = []
        for element in data.values():
            y_points.append(element[currency])
        y_points = np.array(y_points)
        plt.plot(x_points,y_points,label=currency)
    plt.title("Crypto value tracker")
    plt.legend()
    plt.xlabel("Days ago")
    plt.ylabel(convertInto)
    #adding hlines 
    yticks = plt.yticks()[0]
    for ytick in yticks:
        if(int(ytick>0)):
            plt.hlines(ytick, x_points.min(), x_points.max(), linestyles='dotted', alpha=0.5)
    #hovering on the plots
    def show_annotation(sel):
        index = sel.target.index
        x, y = sel.target
        sel.annotation.set_text(f"Days ago: ={x:.2f}, {convertInto}={y:.2f}")
    annotations = [f"x={xval:.2f}, y={yval:.2f}" for xval, yval in zip(x_points, y_points)]
    lines = plt.gca().get_lines()
    mplcursors.cursor(lines, hover=True).connect("add", show_annotation)
    plt.show()

if __name__ == "__main__":
    drawGraph(183,"ETH,BTC","USD")