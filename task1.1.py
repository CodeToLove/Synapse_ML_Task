

jumbled_superheroes = ["DocToR_sTRAngE", "SPidERman", "MoON_KnigHT", "caPTAIN_aMERIca", "hULK"]

# Create empty lists to store indices and decoded names
indices = []
decoded_names = []

# Populate indices and decoded_names lists
for index, name in enumerate(jumbled_superheroes):
    indices.append(index)
    decoded_names.append(name.lower().replace("_", " "))

# Create a lambda function to get the length of a sequence
get_length = lambda seq: len(seq)

# Use map to apply the lambda function on decoded_names
name_lengths = list(map(get_length, decoded_names))

# Sort the indices list based on name_lengths
indices.sort(key=lambda index: name_lengths[index])

# Print the sorted list of superheroes
print("Phase 5 kickoff list :")
for index in indices:
    print(decoded_names[index].title())
