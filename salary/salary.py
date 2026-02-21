from pathlib import Path

def total_salary(path: str) -> tuple:
    parent_dir_path = Path('.')
    
    try:
        with open(parent_dir_path / path, 'r', encoding='utf-8') as fh:
            lines = [el.strip() for el in fh.readlines()]

        total = 0
        for line in lines:
            total += float(line.split(',')[1])
        
        average = total / len(lines)

        return total, average
    except Exception as e:
        print(f'{e} with file')

total, average = total_salary('1/salary_file.txt')
print(f'Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}')
