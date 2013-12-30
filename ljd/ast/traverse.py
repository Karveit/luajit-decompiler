class Visitor():
	def __init__(self):
		pass

	# ##

	def visit_function_definition(self, node):
		pass

	# ##

	def visit_table_constructor(self, node):
		pass

	def visit_table_record(self, node):
		pass

	# ##

	def visit_assignment(self, node):
		pass

	# ##

	def visit_binary_operator(self, node):
		pass

	def visit_unary_operator(self, node):
		pass

	# ##

	def visit_statements_list(self, node):
		pass

	def visit_identifiers_list(self, node):
		pass

	def visit_records_list(self, node):
		pass

	def visit_variables_list(self, node):
		pass

	def visit_expressions_list(self, node):
		pass

	# ##

	def visit_identifier(self, node):
		pass

	def visit_multres(self, node):
		pass

	def visit_table_element(self, node):
		pass

	def visit_vararg(self, node):
		pass

	def visit_function_call(self, node):
		pass

	# ##

	def visit_if(self, node):
		pass

	def visit_elseif(self, node):
		pass

	# ##

	def visit_return(self, node):
		pass

	def visit_break(self, node):
		pass

	# ##

	def visit_while(self, node):
		pass

	def visit_repeat_until(self, node):
		pass

	def visit_numeric_for(self, node):
		pass

	def visit_iterator_for(self, node):
		pass

	# ##

	def visit_constant(self, node):
		pass

	def visit_primitive(self, node):
		pass

	def _visit_node(self, handler, node):
		handler(node)

	def _visit(self, node):
		assert node is not None

		node._accept(self)

	def _visit_list(self, nodes_list):
		assert isinstance(nodes_list, list)

		for node in nodes_list:
			self._visit(node)


def traverse(visitor, ast):
	visitor._visit(ast)
