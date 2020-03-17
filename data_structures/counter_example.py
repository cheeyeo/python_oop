from collections import Counter

responses = [
  "vanilla",
  "chocolate",
  "vanilla",
  "vanilla",
  "strawberry"
]

print(Counter(responses).most_common(1))