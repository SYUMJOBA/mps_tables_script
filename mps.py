from math import ceil

def ceil_int(x, base):
	return int(ceil(x/base) * base)

def stringify_list(list):
	buf = ""
	for v in list:
		buf += "\t" + str(v)
	return buf

class MPS_table:



	def __init__(self, segment_size = 1):
		self.segment_size = segment_size
		self.inital_available = 0
		self.row_fo = []
		self.row_co = []
		self.row_mps = []
		self.row_pa = []
		self.row_atp = []
	

	def set_initial_available(self, initial_available):
		self.inital_available = initial_available

	def fill_row_fo(self, row_fo):
		self.row_fo = []
		for v in row_fo:
			self.row_fo.append(v)
	
	def fill_row_co(self, row_co):
		self.row_co = []
		for v in row_co:
			self.row_co.append(v)
		

	def calc_vals(self, fo, co, pa_prev, segsize):
		mps = ceil_int(max(co, fo) - pa_prev, segsize)
		pa = pa_prev + mps - max(co, fo)
		atp = mps - co
		return (fo, co, mps, pa, atp)

		
	def calculate_table(self):
		table_len = len(self.row_fo)
		if len(self.row_co) != table_len:
			print("row_co and row_fo must be of the same length")
			return

		self.row_mps = [-1 for n in range(table_len)]
		self.row_pa  = [-1 for n in range(table_len)]
		self.row_atp  = [-1 for n in range(table_len)]


		_, _, mps, pa, atp = self.calc_vals(self.row_fo[0], self.row_co[0], self.inital_available, self.segment_size)
		self.row_mps[0] = mps
		self.row_pa[0] = pa
		self.row_atp[0] = self.inital_available + mps - self.row_co[0]

		for i in range(1, table_len):
			_, _, mps, pa, atp = self.calc_vals(self.row_fo[i], self.row_co[i], self.row_pa[i-1], self.segment_size)
			self.row_mps[i] = mps
			self.row_pa[i] = pa
			self.row_atp[i] = atp


	def print_table(self):
		print("")
		print("initial: " + str(self.inital_available) + "\tsegment_size: " + str(self.segment_size))
		print("")
		print("FORECAST ", end=""); print(stringify_list(self.row_fo))
		print("CUST.ORD ", end=""); print(stringify_list(self.row_co))
		print("MPS      ", end=""); print(stringify_list(self.row_mps))
		print("PROJ.AVL ", end=""); print(stringify_list(self.row_pa))
		print("ATP      ", end=""); print(stringify_list(self.row_atp))
		print("")
