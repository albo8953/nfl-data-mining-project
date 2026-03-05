#!/usr/bin/python

import csv


input_file='2021-2025_games.csv'
output_file='2021-2025_games_clean.csv'

with open(input_file, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = list(reader)

# Get header
header = rows[0]
data = rows[1:]

unique_values = {col: set() for col in header}
nulls = {col: [] for col in header}
numeric_values = {col: [] for col in header}

for row_num, row in enumerate(data, start=2):
    for i, value in enumerate(row):
        col = header[i]
        val = value.strip()

        if val == "":
            nulls[col].append(row_num)
        else:
            unique_values[col].add(val)

            try:
                numeric_values[col].append(float(val))
            except ValueError:
                pass

averages = {}

for col in header:
    if numeric_values[col]:
        averages[col] = int(round(sum(numeric_values[col]) / len(numeric_values[col])))
    else:
        averages[col] = None

# Replace missing values with averages
cleaned_data = []
for row in data:
    new_row = row.copy()
    for i, value in enumerate(row):
        col = header[i]

        # Replace missing weather condition with "Unknown"
        if col == "weather_cond" and value.strip() == "":
            new_row[i] = "Unknown"
            continue

        # Replace missing numeric values with average of the column
        if value.strip() == "" and averages[col] is not None:
            new_row[i] = f"{averages[col]}"

    cleaned_data.append(new_row)

# Write cleaned CSV
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(cleaned_data)

# Print summary
for col in header:
    print(f"Column: {col}")
    vals = unique_values[col]
    if len(vals) < 20:
        print("Unique values:")
        for v in sorted(vals):
            print(v)
    if nulls[col]:
        print(f"No data in rows: {nulls[col]}")
        if averages[col] is not None:
            print(f"Average used for nulls: {averages[col]}")
        if col == "weather_cond":
            print("Replaced nulls with Unknown")
    else:
        print("No missing entries")
    print()
