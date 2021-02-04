class System:
	def __init(self):
		pass

	def login(self, username, password):
		pass

	def logout(self):
		pass

	def edit_heating_prog(self, index, **program):
		return False

	def set_heating_prog(self, index):
		pass

	def get_heating_program(self, index):
		pass
		# return Program

	def get_status(self):
		pass

	def start_heating(self):
		pass

	def stop_heating(self):
		pass

	def set_power(self, percent):
		pass

	def set_temp(self, temperature):
		pass

	def get_power(self):
		return 0.0

	def get_temp(self):
		return 0.0

	def get_heat_cycles(year, month):
		return tuple()

	def get_heat_cycle_details(self, date):
		return dict{}

