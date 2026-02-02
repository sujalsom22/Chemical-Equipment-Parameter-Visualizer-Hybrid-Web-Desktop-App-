import csv
import random

types = [
    "Pump",
    "Valve",
    "Reactor",
    "Heat Exchanger",
    "Compressor",
    "Storage Tank"
]

with open("large_equipment_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Equipment Name", "Type", "Flowrate", "Pressure", "Temperature"])

    for i in range(1, 1001):  # change 1001 → 5000 if you want
        eq_type = random.choice(types)
        writer.writerow([
            f"{eq_type}-{i:04d}",
            eq_type,
            round(random.uniform(50, 250), 2),   # Flowrate
            round(random.uniform(2, 12), 2),     # Pressure
            round(random.uniform(20, 350), 2)    # Temperature
        ])

print("large_equipment_data.csv generated")
