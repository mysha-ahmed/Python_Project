import matplotlib.pyplot as plt

# Line Chart

months = ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']
temperature = [32, 26, 20, 17, 15, 18, 21, 27, 30, 31, 33, 35]

plt.plot(months, temperature)
plt.xlabel('Months')
plt.ylabel('Temperature (C)')
plt.title('Temperature Over a Year')
plt.show()