import math
array = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey", "xray", "yankee", "zulu"]

def base36_to_base10(number):
    return int(number, 36)

def compute_transformation(x,y,z):
    result = x + ((x+y+1)/2) + ((x+y+z+2)/3)
    frac = result - math.floor(result)
    if frac < 0.5: 
        return math.floor(result)
    else:
        return math.ceil(result)

def process_file(output_path):
    with open(output_path, 'w') as outfile:
        for part_a in array:
            for part_b in array:
                for part_c in array:
                    transformed_value = compute_transformation(base36_to_base10(part_a), base36_to_base10(part_b),base36_to_base10(part_c))
                    key = '"'+ part_a+"-"+ part_b+"-"+ part_c+ '"'

                    outfile.write(f"\u007B{key}, {transformed_value}\u007D,\n")

if __name__ == "__main__":
    output_file = "./lookupTable.txt"

    process_file(output_file)
    print("Processing complete. Output saved to", output_file)
