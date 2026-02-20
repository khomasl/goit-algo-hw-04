from pathlib import Path

def get_cats_info(path: str) -> dict:
    parent_dir_path = Path('.')
    
    try:
        with open(parent_dir_path / path, 'r', encoding='utf-8') as fh:
            lines = [el.strip() for el in fh.readlines()]

        cats_info = list()
        
        for line in lines:
            info_list = line.split(',')
            cat_info = {"id": info_list[0], "name": info_list[1], "age": info_list[2]}
            cats_info.append(cat_info)
        
        return cats_info
    except Exception as e:
        print(f'{e} with file')

cats_info  = get_cats_info('2/cats_file.txt')
print(cats_info )