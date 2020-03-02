from notebook import Note, Notebook

n = Notebook()
n.new_note("hello 1")
n.new_note("hello 2")
print(n.notes)

print(n.notes[0].id)
print(n.notes[1].id)

print(n.search("1"))
print(n.search("not found"))