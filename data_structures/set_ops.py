# Operations on sets

# alternate way of declaring a set
first_artists = {
	"Sarah Brightman",
	"Guns N' Roses",
	"Opeth",
	"Vixy and Tony",
}

second_artists = {"Nickelback", "Guns N' Roses", "Savage Garden"}

print("All: ", first_artists.union(second_artists))
print("Common between two sets: ", first_artists.intersection(second_artists))
print("In either set but not both: ", first_artists.symmetric_difference(second_artists))