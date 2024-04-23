sales_2023 = [50582, 55912, 52736, 67890]
growth_rates_2024 = [0.052,0.04,0.03,0.02]


def predictsales(sales_2023,growth_rates_2024):
    projectedsales = []
    for i in range(len(sales_2023)):
        projected= sales_2023[i]* (1+growth_rates_2024[i])
        projectedsales.append(projected)
    return projectedsales


def highestsales(sales_2023):
   return sales_2023.index(max(sales_2023)) + 1

projected2024 = predictsales(sales_2023,growth_rates_2024)
highestquarter = highestsales(sales_2023)

print("The quarter with the highest sales is Q",highestquarter)

for i in range(4):
    print("Q", str(i+1), str(projected2024[i]))