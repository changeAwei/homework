from pathlib import Path
def change(pathdir):
    for x in pathdir.iterdir():
        if x.is_file() and x.suffix == '.htm':
            new_x = x.with_suffix('.html')
            x.replace(new_x)
        elif x.is_dir():
            change(x)
            print(x)
        else:
            continue

p = Path( '\\tmp' )

change(p)