import ast
from robot.api import get_model


class TestCaseNamePrinter(ast.NodeVisitor):

    def visit_File(self, node):
        print('File ' + node.source + ' has following tests:')
        self.generic_visit(node)

    def visit_TestCaseName(self, node):
        print(f"- {node.name} on line {node.lineno}")


model = get_model('example.robot')
printer = TestCaseNamePrinter()
printer.visit(model)










