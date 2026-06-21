import json
from pathlib import Path


def load_student_data(file_path: str) -> dict:
    """
    Učitava eksterne podatke o studentskim obavezama iz JSON fajla.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Fajl nije pronađen: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
