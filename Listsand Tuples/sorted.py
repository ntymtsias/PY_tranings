pangram = "The quick brown fox jumped over lazy dog"
missing_letter = sorted("The quick brown fox jumped over lazy dog")
sorted_pangram = sorted(pangram)

print(missing_letter)
print(sorted_pangram.remove())

dir(sorted_pangram)
