from Holding.BaseHoldingTab import BaseHoldingTab
from Holding.FloatHoldingWidget import FloatHoldingWidget


class FloatHoldingTab(BaseHoldingTab):

    def __init__(self, parent=None):
        super().__init__("FLOAT Holding Регистры", parent)
        self.create_float_registers()

    def create_float_registers(self):
        float_registers = [
            ("MY-DEVICE-PREFIX:AO", 301),
            ("Аварийный порог влажности", 305),
            ("Аварийный порог температуры", 307),
            ("Предупредит порог температуры", 309),
            ("Предупредит порог влажности", 311),
            ("P", 314),
            ("I", 316),
            ("D", 318),
            ("Аварийный порог температуры воды", 320),
            ("Предупредит порог Т воды", 322)
        ]

        for name, address in float_registers:
            self.add_register(name, address)

    def add_register(self, name, address):
        register_widget = FloatHoldingWidget(name, address)
        self.registers[address] = register_widget
        self.container_layout.addWidget(register_widget)


    def on_update_data(self):
        print(f"Обновление данных для Float Holding!")

    def on_save_data(self):
        print(f"Сохранение данных для Float Holding")
        values = self.get_all_values()
        print("Значения для сохранения:", values)