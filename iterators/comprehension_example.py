# example of creating a set() and dict()

from collections import namedtuple

Book = namedtuple("Book", "author title genre")

books = [
  Book("Pratchett", "Nightwatch", "fantasy"),
  Book("Pratchett", "Thief of time", "fantasy"),
  Book("Le Guin", "The dispossessed", "scifi"),
  Book("Turner", "The Thief", "fantasy"),
  Book("Phillips", "Preston Diamond", "western"),
  Book("Phillips", "Twice upon a time", "scifi")
]

# create a set using comprehension
fantasy_authors = {b.author for b in books if b.genre == "fantasy"}
print(type(fantasy_authors))
print(fantasy_authors)

# creating dict
fantasy_titles = {b.author: b.title for b in books if b.genre == "fantasy"}
print(type(fantasy_titles))
print(fantasy_titles)