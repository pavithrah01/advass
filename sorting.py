def sort_strings(strings):
    return sorted(strings, key=lambda x: x.lower())

# Example usage:
strings = ['apple', 'Orange', 'banana', 'Mango']
sorted_strings = sort_strings(strings)
print(sorted_strings)
