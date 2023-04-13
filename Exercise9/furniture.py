import re

pattern = r">>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"
all_furniture_information = ""
total = 0

while True:
    information = input()
    if information == "Purchase":
        break
    all_furniture_information += information

valid_information = re.finditer(pattern, all_furniture_information)

print(f"Bought furniture:")
for valid_info in valid_information:
    print(valid_info["furniture"])
    total += float(valid_info["price"]) * int(valid_info["quantity"])

print(f"Total money spend: {total:.2f}")
