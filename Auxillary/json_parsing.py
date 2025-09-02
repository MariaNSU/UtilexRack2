import json
from pathlib import Path


def get_config_by_type(config_type, rack_name, config_path="Config/utilex.json"):
    """
    Возвращает конфигурацию для указанного типа с подставленным именем стойки в base_name

    Args:
        config_path (str/Path): Путь к JSON файлу с конфигурацией
        config_type (str): Тип конфигурации (coil, input_int16, input_float, etc.)
        rack_name (str): Имя стойки для подстановки

    Returns:
        list: Список словарей с обновленными base_name

    Raises:
        FileNotFoundError: Если файл не найден
        ValueError: Если тип не найден в конфигурации или неверный JSON
    """
    config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Config file is not found: {config_path}")

    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config_data = json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON file parsing error {config_path}: {e}")

    if config_type not in config_data:
        available_types = list(config_data.keys())
        raise ValueError(f"Type '{config_type}' is not found in config. Available types are: {available_types}")

    result = []
    for item in config_data[config_type]:
        item_copy = item.copy()
        item_copy["base_name"] = f"{rack_name}-{item['base_name']}"
        result.append(item_copy)

    return result


def load_config(config_path):
    """Загружает весь конфиг из JSON файла"""
    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file is not found: {config_path}")

    with open(config_path, 'r', encoding='utf-8') as file:
        return json.load(file)


'''
Example usage 

coil_config = get_config_by_type("coil", "Rack1")
print(coil_config)
'''


