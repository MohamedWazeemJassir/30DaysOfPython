import os
import shutil
from pathlib import Path

# Get source directory as input
SOURCE_DIR = Path(input("Enter the source directory: "))

# Save file extensions in a dictionary
FILE_CATEGORIES = {
	"Images": [".jpg", ".png", ".jpeg", ".gif", ".webp"],
	"Documents": [".pdf", ".txt", ".csv", ".pptx", ".docx"],
	"Videos": [".mp4", ".webm", ".mov", ".mkv", ".avi"],
	"Archives": [".zip", ".tar", ".gz"],
	"Code": [".py", ".js", ".json"]
}

def create_category_folders():
	for category in FILE_CATEGORIES:
		folder = SOURCE_DIR / category
		print("Folder" , folder)
		folder.mkdir(exist_ok=True)
	# Folder for handling missed file categories (extension)
	other_folder = SOURCE_DIR / "Others"
	other_folder.mkdir(exist_ok=True)

def check_path_exists():
	if not SOURCE_DIR.exists():
		return False
	return True

def get_category(extension):
	for category, extensions in FILE_CATEGORIES.items():
		if extension.lower() in extensions:
			return category
	return "Others"

def organize_files():
	print(f"Scanning: {SOURCE_DIR}...")
	for file in SOURCE_DIR.iterdir():
		# Skip the folders
		if file.is_dir():
			continue
		extension = file.suffix
		category = get_category(extension)
		target_folder = SOURCE_DIR / category
		target_path = target_folder / file.name
		
		try:
			print(f"Moving: {file.name} -> {category}/")
			shutil.move(str(file), str(target_path))
		except Exception as ex:
			print(f"Error Moving {file.name}")
		
def migrate():
	if check_path_exists():
		print("Proceed")
		create_category_folders()
		organize_files()
	else:	
		print("Path Doesn't Exists")
		
migrate()

