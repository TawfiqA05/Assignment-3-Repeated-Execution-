# Function to count unique state values
def count_unique_states(file_path):
    # Step 1: Open the file
    with open(file_path, 'r') as file:
        # Step 2: Read the file line by line
        lines = file.readlines()

    # Step 3: Initialize an empty set to store unique state values
    unique_states = set()

    # Step 4: Iterate over the lines, starting from the second line to skip the header
    for line in lines[1:]:
        # Step 5: Split the line by commas and extract the state value (second column)
        state = line.split(',')[1]
        # Step 6: Add the state value to the set
        unique_states.add(state)

    # Step 7: Count the number of unique state values
    num_unique_states = len(unique_states)

    # Return the result
    return num_unique_states

# Example of repeated execution
file_path = '/Users/tawfiqabulail/Downloads/Information Infrastructure I /covid_data_set.csv'
for _ in range(3):  # Repeated execution 3 times
    result = count_unique_states(file_path)
    print(f"Number of unique state values: {result}")