from collections import Counter

magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
note = ['give', 'one', 'grand', 'today']

print(Counter(magazine) - Counter(note))
print(Counter(note) - Counter(magazine))
print(Counter(note) - Counter(magazine) == {})
