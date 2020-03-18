song_library = [
  ("Phantom Of The Opera", "Sarah Brightman"),
  ("Knocking On Heaven's Door", "Guns N' Roses"),
  ("Captain Nemo", "Sarah Brightman"),
  ("Patterns In The Ivy", "Opeth"),
  ("November Rain", "Guns N' Roses"),
  ("Beautiful", "Sarah Brightman"),
  ("Mal's Song", "Vixy and Tony")]

artists = set()

for _, artist in song_library:
	artists.add(artist)

print(artists)

print("Opeth" in artists)

# sort alphabetically
l = list(artists)
print(l)
l.sort(key=str.lower)
print(l)