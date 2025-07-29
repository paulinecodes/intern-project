directions = {}

with open('AIR00096.AIR', 'r') as file:
    count = 1
    for line in file:
        if line.startswith('A-'):
            values = line[2:].strip()
            #EMIRATES;EK 1761 
            # Split into name and the rest
            name, rest = values.split(';', 1)
            rest_parts = rest.strip().split(' ', 1)

            if len(rest_parts) == 2:
                code, id_  = rest_parts
                directions[f'Discription_{count}'] = {
                    'name': name.strip(),
                    'code': code.strip(),
                    'numeric_code': id_.strip()
                }
                count += 1

if directions:
    for key, value in directions.items():
        print(f"{key}: {value}")
else:
    print("No matching lines found starting with 'A-' in AIR00096.AIR.")
