from pathlib import Path
for p in Path('../APT_Digital_Weapon').glob('./**/*'):
	if p.is_file():
		if "README.md" in str(p):
			print(p)




