from sympy import primefactors

def base36_to_base10(number):
    return int(number, 36)

def compute_transformation(x,y,z):
    return round((x/1)+((x+y+1)/2)+((x+y+z+2)/3))

def process_file(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        final_list = []
        for line in infile:
            parts = line.strip().split()
            log_id = int(parts[0])
            encrypted_number = int(parts[1])
            message = parts[2].strip('"')
            
            # Step 1: Prime factorization
            factors = primefactors(encrypted_number)
            sum_factors = sum(factors)

            # Step 2: String transformation
            base10_values = [base36_to_base10(part) for part in message.split('-')]
            transformed_value = compute_transformation(base10_values[0], base10_values[1], base10_values[2])
            
            # Step 3: Computation
            final_result = sum_factors * transformed_value

            final_list.append({"log_id": log_id, "final_result": final_result })

        # Step 4: Sorting and writing
        final_list.sort(key=lambda line: line["final_result"])

        for line in final_list:
            outfile.write(f"{line['log_id']} {line['final_result']}\n")

if __name__ == "__main__":
    input_file = "/data/test_data_input.txt"
    output_file = "/data/test_data_output.txt"

    process_file(input_file, output_file)
    print("Processing complete. Output saved to", output_file)
