def weight_on_planets(sweight):
    sweight = input ('What do you weigh on earth? ')
    weight = float(sweight)

    print("\nOn Mars you would weigh", (0.38 * int(weight)), "pounds.\nOn Jupiter you would weigh",(2.34 * int(weight)), "pounds.\n")
   
if __name__ == '__main__':
   weight_on_planets()
