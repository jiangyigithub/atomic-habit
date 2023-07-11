import re

input_file = "Longman_Communication_3000_new.md"
output_file = "Longman_Communication_3000_new2.md"

# Read the input file
with open(input_file, "r") as file:
    content = file.read()

# Define the regular expression pattern
pattern = r"\*\*(.*?)\*\*"

# Find matching words in the content
matching_words = re.findall(pattern, content, re.MULTILINE)

# Create the output content
output_content = "\n".join(matching_words)

# Write the output to a file
with open(output_file, "w") as file:
    file.write(output_content)
