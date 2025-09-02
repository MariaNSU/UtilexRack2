from Holding.BaseHoldingTab import BaseHoldingTab
from Holding.IntHoldingWidget import IntHoldingWidget
from Auxillary.json_parsing import get_config_by_type


class IntHoldingTab(BaseHoldingTab):
    def __init__(self, rack_name, parent=None):
        super().__init__(rack_name, "INT Holding Регистры", parent)
        self.create_int_registers()

    def create_int_registers(self):
        int_holding_registers = get_config_by_type('holding_int16', self.rack_name)

        for register_info in int_holding_registers:
            base_name = register_info['base_name']
            description = register_info['description']
            address = register_info['address']
            self.add_register(base_name, description, address, 'int')

    def add_register(self, base_name, description, address, data_type):
        register_widget = IntHoldingWidget(base_name, description, address, data_type)
        self.registers[address] = register_widget
        self.container_layout.addWidget(register_widget)


    def on_update_data(self):
        print(f"Обновление данных для Int Holding!")

    def on_save_data(self):
        print(f"Сохранение данных для Int Holding")
        values = self.get_all_values()
        print("Значения для сохранения:", values)

