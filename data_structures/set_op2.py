first_artists = {
	"Sarah Brightman", 
	"Guns N' Roses",
	"Opeth", 
	"Vixy and Tony"
}

bands = {"Guns N' Roses", "Opeth"}

# difference method returns elements in calling set but not in set passed as argument
print("DIFFERENCE: ", first_artists.difference(bands))

# issuperset returns True if all items in arguments also in calling set
print("issuperset: ", first_artists.issuperset(bands))

# issubset returns True if all elements in calling set also in set passed as params
print("issubset: ", first_artists.issubset(bands))

print('*' * 20)
print("DIFFERENCE: ", bands.difference(first_artists))
print("issuperset: ", bands.issuperset(first_artists))
print("issubset: ", bands.issubset(first_artists))