from Input.BaseInputTab import BaseInputTab
from Auxillary.json_parsing import get_config_by_type


class IntInputTab(BaseInputTab):

    def __init__(self, rack_name, parent=None):
        super().__init__(rack_name, "INT Input Регистры", parent)
        self.create_int_registers()

    def create_int_registers(self):
        int_registers = get_config_by_type('input_int16', self.rack_name)

        for register_info in int_registers:
            base_name = register_info['base_name']
            description = register_info['description']
            address = register_info['address']
            self.add_int_register(base_name, description, address, 'int16')

    def renew_data(self):
        print("Int Input Tab Class!")