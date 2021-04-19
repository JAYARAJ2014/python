from pathlib import Path
path = Path()
print(path.absolute())
print(path.home())
print(path.stem)
print(path.exists())
# List files and directories.

print(path.exists())
print(path.iterdir())  # returns generator object

# iterate through the generator.
# for p in path.iterdir():
#     print(p)

# comprehension expression to list only directories

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)
for p in paths:
    print(p)
