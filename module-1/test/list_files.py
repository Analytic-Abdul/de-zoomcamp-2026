from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__)

print(f"These are the files in {current_dir}")

for file in current_dir.iterdir():
	if file.name == current_file.name:
		continue
	print(f"Current file is {file.name}")
	if file.is_file():
		file_contents = file.read_text(encoding = 'utf-8')
		print(f"Contents:{file_contents}")
