import csv
import matplotlib.pyplot as plt

last = None

fname = "1490415085.csv"
vars_to_plt = ["sin_time", "cos_time"]

data = {}
with open(fname, 'rU') as infile:
    # read the file as a dictionary for each row ({header : value})
    reader = csv.DictReader(infile)
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]

plot0 = None
plt.figure("Robot Log Plotter")
for i, var in enumerate(vars_to_plt):
    if i == 0:
        plot0 = plt.subplot(211+i)
    else:
        plt.subplot(211+i, sharex=plot0)
    plt.ylabel(var)
    times = data["time"]
    plt.plot(times, data[var], 'bo')
plt.show()
