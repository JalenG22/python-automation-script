#Log Parser#

error_count = 0

with open("sample.log", "r") as file:
  for line in file:
    if "Error" in line:
      error_count += 1

Print(f"Total errors found: {error_count}")

      
