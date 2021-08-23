import matplotlib.pyplot as plt
chocolate_total = 0
vanilla_total = 0
strawberry_total = 0
max_total = 0
cupcake_file = open("CupcakeInvoices.csv")
for line in cupcake_file:
  array = line.split(",")
  amount = float(array[3])
  price = float(array[4])
  print(array[2])
  total = amount *price
  max_total += total
  print(round((total),2))
  if array[2] == 'Chocolate':
    chocolate_total += total
  elif array[2] == 'Strawberry':
    strawberry_total += total
  elif array[2] == 'Vanilla':
    vanilla_total += total
print(round((max_total),2))
cupcake_file.close()
# print(float(array[3] * float(array[4])))
print(chocolate_total,vanilla_total,strawberry_total)
labels = 'chocolate', 'vanilla', 'strawberry'
sizes = [chocolate_total, vanilla_total, strawberry_total]
colors = ['brown', 'yellow', 'lightcoral']


# Plot
# copied this part from a website, idk how it works but i think it asigns the labels and sizes i created above to the pie chart then sets some visual attributes to the chart as well.
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()