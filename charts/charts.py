import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["A", "B", "C"]
    values = [200, 300, 400]

    fig, ax = plt.subplot()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()
