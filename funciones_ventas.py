import csv
from collections import defaultdict

def leer_archivo(filename):
    ventas = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ventas.append({
                'id': int(row['id']),
                'fecha': row['fecha'],
                'producto': row['producto'],
                'cantidad': int(row['cantidad']),
                'precio': float(row['precio'])
            })
    return ventas