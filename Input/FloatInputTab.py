from Input.BaseInputTab import BaseInputTab
from Auxillary.json_parsing import get_config_by_type

class FloatInputTab(BaseInputTab):
    def __init__(self, rack_name, parent=None):
        super().__init__(rack_name, "FLOAT Input Регистры", parent)
        self.create_float_registers()

    def create_float_registers(self):
        float_registers = get_config_by_type('input_float', self.rack_name)

        for register_info in float_registers:
            base_name = register_info['base_name']
            description = register_info['description']
            address = register_info['address']
            self.add_float_register(base_name, description, address, 'float')

    def renew_data(self):
        print("Float Tab Class!")