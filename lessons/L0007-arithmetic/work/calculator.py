# L0007: calculator.py - predict operator results, then compute workout stats with arithmetic
# predict: 14
print("2 + 3 * 4 =", 2 + 3 * 4)
# predict: 20
print("(2 + 3) * 4 =", (2 + 3) * 4)
# predict: 5
print("20 - 10 - 5 =", 20 - 10 - 5)
# predict: 512
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)
# predict: 3.5
print("7 / 2 =", 7 / 2)
# predict: 3
print("7 // 2 =", 7 // 2)
# predict: 1
print("7 % 2 =", 7 % 2)
# predict: 3.0
print("6 / 2 =", 6 / 2)

total_seconds = 9876
run1 = 7
run2 = 4
run3 = 9
run4 = 6
start_points = 50
weeks = 10

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print("Workout time:", hours, "h", minutes, "min", seconds, "s")

average_distance = (run1 + run2 + run3 + run4) / 4
print("Average distance:", average_distance, "km")
whole_average_distance = (run1 + run2 + run3 + run4) // 4
print("Whole km average:", whole_average_distance, "km")

points = start_points * 2 ** weeks
print("Points after 10 weeks:", points)