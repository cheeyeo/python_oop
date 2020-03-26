import pickle

some_Data = ["a list", "containing", "5", "values", "including", ["another", "list"]]

with open("pickled_list.pkl", "wb") as file:
	pickle.dump(some_Data, file)

with open("pickled_list.pkl", "rb") as file:
	loaded_data = pickle.load(file)

print(loaded_data)
assert loaded_data == some_Data	