from datetime import datetime

def validate_year(year: int) -> int:
    current_year = datetime.now().year
    if year > current_year:
        raise ValueError(f"Năm không được lớn hơn {current_year}")
    return year
