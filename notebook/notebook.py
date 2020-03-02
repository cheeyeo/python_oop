import datetime

# Store next avail ID for new notes
last_id = 0

class Note:
	"""Represent note in notebook. Match against a string in searches and store tags for each note."""

	def __init__(self, memo, tags=""):
		"""Initialize a note with memo and space-separated tags. Automatically set the note's creation date and unique id"""

		self.memo = memo
		self.tags = tags
		self.creation_date = datetime.date.today()
		global last_id
		last_id += 1
		self.id = last_id

	def match(self, filter):
		"""Determine if this note matches the filter text. Return True if matches, False otherwise.

		Search is case sensitive and matches both text and tags."""

		return filter in self.memo or filter in self.tags

class Notebook:
	"""Collection of notes"""

	def __init__(self):
		"""Initialize an empty list"""
		self.notes = []

	def new_note(self, memo, tags=""):
		"""Create new note and add to list"""
		self.notes.append(Note(memo, tags))

	def _find_note(self, note_id):
		"""Locate note with given id"""
		for note in self.notes:
			if str(note.id) == str(note_id):
				return note
		return None

	def modify_memo(self, note_id, memo):
		"""Find note with given id and change its content"""
		self._find_note(note_id).memo = memo

	def modify_tags(self, note_id, tags):
		"""Find note with given id and update its tags"""
		self._find_note(note_id).tags = tags

	def search(self, filter):
		"""Find all notes that match given filter"""
		return [note for note in self.notes if note.match(filter)]
