class Connection1:
	""" 新方案——对每个状态定义一个类，Connection1类为主类"""

	def __init__(self):
		# 初始状态为closed状态，为ClosedConnectionState的实例
		self.new_state(ClosedConnectionState)


	def new_state(self, newstate):
		self._state = newstate  # Delegate to the state class

	def read(self):
		# 调用的是所属实例的方法（Close/Open）
		return self._state.read(self)

	def write(self, data):
		return self._state.write(self, data)

	def open(self):
		return self._state.open(self)

	def close(self):
		return self._state.close(self)


# Connection state base class
class ConnectionState:
	@staticmethod
	def read(conn):
		# 子类必须实现父类的方法，否则报下列错误
		raise NotImplementedError()

	@staticmethod
	def write(conn, data):
		raise NotImplementedError()

	@staticmethod
	def open(conn):
		raise NotImplementedError()

	@staticmethod
	def close(conn):
		raise NotImplementedError()


# Implementation of different states
class ClosedConnectionState(ConnectionState):
	@staticmethod
	def read(conn):
		raise RuntimeError('Not open')

	@staticmethod
	def write(conn, data):
		raise RuntimeError('Not open')

	@staticmethod
	def open(conn):
		conn.new_state(OpenConnectionState)

	@staticmethod
	def close(conn):
		raise RuntimeError('Already closed')


class OpenConnectionState(ConnectionState):
	@staticmethod
	def read(conn):
		print('reading')

	@staticmethod
	def write(conn, data):
		print('writing')

	@staticmethod
	def open(conn):
		raise RuntimeError('Already open')

	@staticmethod
	def close(conn):
		# 转换为Close实例，调用父类的new_state方法
		conn.new_state(ClosedConnectionState)


if __name__ == '__main__':
	c = Connection1()
	print(c._state)
	c.open()
	print(c._state)
	c.read()
	c.write("write")
	c.close()
	print(c._state)
