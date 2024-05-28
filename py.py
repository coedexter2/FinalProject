
def remove_whitespace_sections(text):


  # Split the string into lines, stripping any whitespace
  lines = [line.strip() for line in text.splitlines()]

  # Identify non-empty lines
  non_empty_lines = [line for line in lines if line]  # List comprehension for concise filtering

  # Join the non-empty lines with newlines
  new_string = "\n".join(non_empty_lines)

  return new_string

# Example usage
my_string = """

line
line

Line
Line
Line
Line

Line
Line

"""

new_string = remove_whitespace_sections(my_string)
print(new_string)