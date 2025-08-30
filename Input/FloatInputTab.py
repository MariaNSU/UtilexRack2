from Input.BaseInputTab import BaseInputTab


class FloatInputTab(BaseInputTab):
    def __init__(self, parent=None):
        super().__init__("FLOAT Input Регистры", parent)
        self.create_float_registers()

    def create_float_registers(self):
        float_registers = [
            ("Температура хк", 2, "float"),
            ("Температура гк", 4, "float"),
            ("Хладопроизводительность", 7, "float"),
            ("Уставка температуры", 9, "float"),
            ("Температура вода вход", 11, "float"),
            ("Температура вода выход", 13, "float"),
            ("Наработка вент.исп.", 16, "float"),
            ("Темп хк верх стойка левая", 29, "float"),
            ("Темп хк средн стойка левая", 31, "float"),
            ("Темп хк низ стойка левая", 33, "float"),
            ("Темп гк верх стойка левая", 35, "float"),
            ("Темп гк средн стойка левая", 37, "float"),
            ("Темп гк низ стойка левая", 39, "float"),
            ("Влажность хк стойка левая", 41, "float"),
            ("Влажность гк стойка левая", 43, "float"),
            ("Темп хк верх стойка правая", 53, "float"),
            ("Темп хк средн стойка правая", 55, "float"),
            ("Темп хк низ стойка правая", 57, "float"),
            ("Темп гк верх стойка правая", 59, "float"),
            ("Темп гк средн стойка правая", 61, "float"),
            ("Темп гк низ стойка правая", 63, "float"),
            ("Влажность хк стойка правая", 65, "float"),
            ("Влажность гк стойка правая", 67, "float"),
            ("Аварийный порог температуры", 74, "float"),
            ("Аварийный порог влажности", 76, "float"),
            ("Предупредит порог температуры", 78, "float"),
            ("Предупредит порог влажности", 80, "float"),
            ("Аварийный порог температуры воды", 82, "float"),
            ("Предупредит порог Т воды", 84, "float")
        ]

        for name, address, data_type in float_registers:
            self.add_register(name, address, data_type)

    def renew_data(self):
        print("Float Tab Class!")