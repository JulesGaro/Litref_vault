import os
import time
import shutil

import function_litref as fct

# Check if a BetterNote.py process is already running
if [file for file in os.listdir("./") if file == "__betterNoteCacheFile__"]:
	with open("../../../last_pending_note/killthatrunningprocessplease","w") as f:
		time.sleep(1)
	# In that case we don't create a cache file since there is already one
else:
	# Create a cache file meaning a process is running
	with open("__betterNoteCacheFile__","w") as f:
		pass

# initizalize the note content
note = ""

# Get the contetn of the last_pending_note folder
folder_path = "../../../last_pending_note/"
pending_note = os.listdir(folder_path)

# Wait for the note to be created or a killing signal to be sent
timer = time.time() + 600
clock = time.time()
while (not pending_note) and (clock < timer):
	clock = time.time()
	pending_note = os.listdir(folder_path)


# nothing if a killing signal as been sent
if ("killthatrunningprocessplease" in pending_note) or (clock > timer):
	pass
# Else, continue
else:
	os.remove("__betterNoteCacheFile__")
	# Get Article note title
	time.sleep(1)
	with open("../../../last_pending_note/LoadingArticleNote.md") as f:
		note = f.read()
	
	note_title = fct.get_note_title_frontmatter(
		"../../../last_pending_note/LoadingArticleNote.md"
	)
	# Set new note path
	new_note_path = f"../../../Article_note/{note_title}.md"

	# Check if a previous version of the note exists
	if os.path.exists(new_note_path):
		source = new_note_path
		destination = f"../../../Old_Article_notes/{note_title}.md"
		# Chech if a previous verison of the old note exist
		if os.path.exists(destination):
			# If it exists, delete it
			os.remove(destination)
		shutil.move(source, destination)

	# Get article refernces
	try:
		references = fct.get_reference_titles(note_title)
		references = fct.format_ref(references)
		note += references

		# Write down the note and the references
		with open(new_note_path, "w") as f:
			f.write(note)

		os.remove("../../../last_pending_note/LoadingArticleNote.md")

	except KeyError as e:
		os.remove("../../../last_pending_note/LoadingArticleNote.md")
		raise(e)

	