from read_data import calories

calories_per_elf: list[int] = []
total: int = 0

for calorie in calories:
    if calorie == "":
        calories_per_elf.append(total)
        total = 0
    if calorie != "":
        total += int(calorie)

calories_per_elf.sort(reverse=True)
print(sum(calories_per_elf[:3]))
