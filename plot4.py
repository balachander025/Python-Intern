import matplotlib.pyplot as plt


labels = ['Tech', 'Retail', 'Finance', 'Other']
sizes = [40, 25, 20, 15]


plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Company Revenue Distribution')
plt.show()
