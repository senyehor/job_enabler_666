# L0010 Part 2: ask for a name and a distance, then print it converted (see task.md)

name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
distance_m = int(input("Enter the distance in metres: "))

metres_per_mile = 1609.344

print(f"Hello, {name} {last_name}!")
print(f"Metres: {distance_m}")
print(f"Kilometres: {distance_m / 1000}")
print(f"Miles: {distance_m / metres_per_mile:.2f}")
print(f"Split: {distance_m // 1000} km {distance_m % 1000} m")
print("Badge:", end=" ")
print(name[0] + last_name[0], name[:3], sep="-")
print(f'{name[0] + last_name[0]}, {name[:3]},  sep="-")