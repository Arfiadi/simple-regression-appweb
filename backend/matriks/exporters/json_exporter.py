# matriks/exporters/json_exporter.py
import json
from ..matrix import Matrix

def export_to_json(matrix, filename):
    """Mengekspor data matriks ke file JSON."""
    with open(filename, 'w') as jsonfile:
        json.dump(matrix.data, jsonfile, indent=4)
    print(f"Matriks berhasil diekspor ke {filename}")