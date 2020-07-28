import matplotlib.pyplot as plt

x_values = [x for x in range(1, 5001)]
y_values = [x**3 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=7)

ax.set_title("Deez Cubez!", fontsize=27)
ax.set_xlabel("Deez x Values", fontsize=14)
ax.set_ylabel("Deez y Values", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 5100, 0, 150000000000])

plt.show()
