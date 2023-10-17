# # This code reads cfg file and deletes the configurations which has energy greater than zero. Deleting of these configurations ensures only good configurations are used while training. 

# Define the input and output file names
input_file = "Cr70Mn30.cfg"
output_file = "Filtered_" + str(input_file)

# Initialize an empty list to store configurations
configurations = []
current_config = []

# Open the input file for reading
with open(input_file, 'r') as file:
    inside_config = False  # A flag to track whether we are inside a configuration block
    read_energy = False  # A flag to track if we should read the next line as energy
    energy_value = None  # To store the energy value
    for line in file:
        if line.strip() == "BEGIN_CFG":
            inside_config = True
            current_config = []  # Start a new configuration
            current_config.append("BEGIN_CFG")
            read_energy = False
            energy_value = None
        elif line.strip() == "END_CFG":
            inside_config = False
            current_config.append("END_CFG")  # Add "END_CFG" to the current configuration
            if energy_value is None or energy_value <= 0:
                configurations.append(current_config)  # Add the configuration to the list
        elif inside_config:
            current_config.append(line)  # Preserve the line as it is
            if read_energy:
                try:
                    energy_value = float(line)
                    read_energy = False
                except ValueError:
                    pass
            if "Energy" in line:
                read_energy = True

# Now, 'configurations' contains a list of arrays, each array representing a configuration

# Save the remaining configurations to the output file, preserving formatting
with open(output_file, 'w') as output:
    for config in configurations:
        for line in config:
            output.write(line)
        output.write('\n')  # Write a one-line gap between configurations

print(f"Filtered configurations saved to {output_file}")
