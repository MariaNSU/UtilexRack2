from Holding.BaseHoldingTab import BaseHoldingTab
from Holding.IntHoldingWidget import IntHoldingWidget


class IntHoldingTab(BaseHoldingTab):
    def __init__(self, parent=None):
        super().__init__("INT Holding Регистры", parent)
        self.create_int_registers()

    def create_int_registers(self):
        int_registers = [
            ("Скорость вентилятора", 303),
            ("Управление вентилятором", 304)
        ]

        for name, address in int_registers:
            self.add_register(name, address)

    def add_register(self, name, address):
        register_widget = IntHoldingWidget(name, address)
        self.registers[address] = register_widget
        self.container_layout.addWidget(register_widget)


    def on_update_data(self):
        print(f"Обновление данных для Int Holding!")

    def on_save_data(self):
        print(f"Сохранение данных для Int Holding")
        values = self.get_all_values()
        print("Значения для сохранения:", values)

