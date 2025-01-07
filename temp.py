def evenly_divisible(n, p):
    items_per_core = n // p
    my_first_i = []
    my_last_i = []
    
    for core_number in range(p):
        first_i = core_number * items_per_core
        last_i = first_i + items_per_core - 1
        my_first_i.append(first_i)
        my_last_i.append(last_i)
    
    # Output
    print("Evenly divisible case (n divisible by p):")
    for core_number in range(p):
        print(f"Core {core_number}: my_first_i = {my_first_i[core_number]}, my_last_i = {my_last_i[core_number]}")

# Example Usage
n = 100
p = 5
evenly_divisible(n, p)
