import matplotlib.pyplot as plt
categories=['xy','ab','cd','ef','ed','df']
values=['20','30','40','50','60','70']
values2=['10','20','55','45','12','89']
plt.bar(categories,values)
plt.plot(categories,values)
plt.xlabel('categories')
plt.ylabel('values')
plt.title('Barchart')
plt.show()
plt.pie(values)
plt.show()
