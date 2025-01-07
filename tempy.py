def offset_workload_distribution(n, p):
    base_items_per_core = n // p  # Base division of items
    offset = 0  # Tracks the additional workload distribution
    my_first_i = []
    my_last_i = []

    for core_number in range(p):
        # Calculate the starting index for this core
        first_i = core_number * base_items_per_core + offset
        # Calculate the ending index for this core
        last_i = first_i + base_items_per_core - 1

        # If core_number is less than the remaining items, assign an extra item
        if core_number < n % p:
            last_i += 1
            offset += 1  # Increment the offset when assigning extra item

        # Append the results to the lists
        my_first_i.append(first_i)
        my_last_i.append(last_i)

    # Output the results
    print("Offset workload distribution:")
    for core_number in range(p):
        print(f"Core {core_number}: my_first_i = {my_first_i[core_number]}, my_last_i = {my_last_i[core_number]}")

# Example Usage
n = 25  # Total number of items
p = 4    # Number of cores
offset_workload_distribution(n, p)
