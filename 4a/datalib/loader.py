def load_csv(filepath):
    import csv

    data = []
    try:
        with open(filepath, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Error: El archivo {filepath} no fue encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo {filepath}: {e}")  