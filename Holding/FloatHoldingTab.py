from Holding.BaseHoldingTab import BaseHoldingTab
from Holding.FloatHoldingWidget import FloatHoldingWidget
from Auxillary.json_parsing import get_config_by_type

class FloatHoldingTab(BaseHoldingTab):

    def __init__(self, rack_name, parent=None):
        super().__init__(rack_name, "FLOAT Holding Регистры", parent)
        self.create_float_registers()

    def create_float_registers(self):
        float_holding_registers = get_config_by_type('holding_float', self.rack_name)

        for register_info in float_holding_registers:
            base_name = register_info['base_name']
            description = register_info['description']
            address = register_info['address']
            self.add_register(base_name, description, address, 'float')

    def add_register(self, base_name, description, address, data_type):
        register_widget = FloatHoldingWidget(base_name, description, address, data_type)
        self.registers[address] = register_widget
        self.container_layout.addWidget(register_widget)


    def on_update_data(self):
        print(f"Обновление данных для Float Holding!")

    def on_save_data(self):
        print(f"Сохранение данных для Float Holding")
        values = self.get_all_values()
        print("Значения для сохранения:", values)