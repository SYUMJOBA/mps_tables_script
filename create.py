from mps import MPS_table
from mps import ceil_int

print("GG-RR")

table = MPS_table(40)
table.set_initial_available(15)

table.fill_row_fo([160, 140, 134, 178, 150, 150, 132, 120, 130, 146])
table.fill_row_co([30, 30, 40, 40, 35, 25, 30, 30, 25, 25])

table.calculate_table()
table.print_table()
print()
print()

print("GG-NN")

table = MPS_table(40)
table.set_initial_available(12)

table.fill_row_fo([160, 140, 134, 178, 150, 150, 132, 120, 130, 146])
table.fill_row_co([35, 30, 25, 35, 35, 35, 30, 30, 20, 25])

table.calculate_table()
table.print_table()
print()
print()


print("MM-RR")

table = MPS_table(55)
table.set_initial_available(22)

table.fill_row_fo([160, 140, 134, 178, 150, 150, 132, 120, 130, 146])
table.fill_row_co([40, 40, 50, 50, 50, 40, 35, 35, 25, 20])

table.calculate_table()
table.print_table()
print()
print()


print("MM-NN")

table = MPS_table(55)
table.set_initial_available(25)

table.fill_row_fo([160, 140, 134, 178, 150, 150, 132, 120, 130, 146])
table.fill_row_co([45, 50, 50, 30, 30, 45, 25, 55, 40, 40])

table.calculate_table()
table.print_table()
print()
print()

