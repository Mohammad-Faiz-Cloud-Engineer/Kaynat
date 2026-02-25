"""
Kaynat Interpreter - Executes the Abstract Syntax Tree.

Tree-walking interpreter that evaluates each node.
"""

from typing import Any
from kaynat.lexer.lexer import Lexer
from kaynat.parser.parser import Parser
from kaynat.parser.nodes import *
from kaynat.interpreter.environment import Environment
from kaynat.interpreter.runtime_types import *
from kaynat.errors.error_types import RuntimeError as KaynatRuntimeError, TypeError as KaynatTypeError
import math


class Interpreter:
    """
    Executes Kaynat programs by walking the AST.
    
    Each node type has a corresponding visit method that
    evaluates the node and returns a runtime value.
    """
    
    def __init__(self):
        """Initialize the interpreter with a global environment."""
        self.global_env = Environment()
        self.current_env = self.global_env
        self._setup_builtins()
    
    def _setup_builtins(self):
        """Setup built-in constants and functions."""
        self.global_env.define('pi', KaynatNumber(math.pi), is_constant=True)
        self.global_env.define('e', KaynatNumber(math.e), is_constant=True)
    
    def execute(self, source: str) -> Any:
        """
        Execute Kaynat source code.
        
        Args:
            source: Kaynat source code
            
        Returns:
            Result of execution
        """
        # Lexical analysis
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Execution
        return self.visit(ast)
    
    def visit(self, node: ASTNode) -> Any:
        """
        Visit a node and execute it.
        
        Args:
            node: AST node to visit
            
        Returns:
            Result of node execution
        """
        method_name = f'visit_{node.__class__.__name__}'
        method = getattr(self, method_name, self.generic_visit)
        return method(node)
    
    def generic_visit(self, node: ASTNode):
        """Fallback for unimplemented node types."""
        raise KaynatRuntimeError(
            f"No visit method for {node.__class__.__name__}",
            node.line,
            node.column
        )
    
    def visit_ProgramNode(self, node: ProgramNode) -> Any:
        """Execute a program."""
        result = None
        for statement in node.statements:
            result = self.visit(statement)
        return result
    
    def visit_NumberNode(self, node: NumberNode) -> KaynatNumber:
        """Evaluate a number literal."""
        return KaynatNumber(node.value)
    
    def visit_StringNode(self, node: StringNode) -> KaynatString:
        """Evaluate a string literal."""
        return KaynatString(node.value)
    
    def visit_BooleanNode(self, node: BooleanNode) -> KaynatBoolean:
        """Evaluate a boolean literal."""
        return KaynatBoolean(node.value)
    
    def visit_NullNode(self, node: NullNode) -> KaynatNull:
        """Evaluate null."""
        return KaynatNull()
    
    def visit_IdentifierNode(self, node: IdentifierNode) -> KaynatValue:
        """Look up a variable."""
        return self.current_env.get(node.name)
    
    def visit_ListNode(self, node: ListNode) -> KaynatList:
        """Evaluate a list literal."""
        elements = [self.visit(elem) for elem in node.elements]
        return KaynatList(elements)
    
    def visit_MapNode(self, node: MapNode) -> KaynatMap:
        """Evaluate a map literal."""
        pairs = {}
        for key, value in node.pairs:
            key_val = self.visit(key)
            value_val = self.visit(value)
            pairs[key_val.to_string()] = value_val
        return KaynatMap(pairs)
    
    def visit_VariableDeclarationNode(self, node: VariableDeclarationNode) -> None:
        """Execute variable declaration."""
        value = self.visit(node.value)
        self.current_env.define(node.name, value, node.is_constant)
        return None
    
    def visit_AssignmentNode(self, node: AssignmentNode) -> None:
        """Execute variable assignment."""
        value = self.visit(node.value)
        self.current_env.set(node.name, value)
        return None
    
    def visit_BinaryOpNode(self, node: BinaryOpNode) -> KaynatValue:
        """Execute binary operation."""
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        # Arithmetic operations
        if node.operator in ('+', 'add', 'plus'):
            if isinstance(left, KaynatNumber) and isinstance(right, KaynatNumber):
                return KaynatNumber(left.value + right.value)
            elif isinstance(left, KaynatString) or isinstance(right, KaynatString):
                return KaynatString(left.to_string() + right.to_string())
            else:
                raise KaynatTypeError(
                    f"Cannot add {type(left).__name__} and {type(right).__name__}",
                    node.line,
                    node.column
                )
        
        elif node.operator in ('-', 'subtract', 'minus'):
            if isinstance(left, KaynatNumber) and isinstance(right, KaynatNumber):
                return KaynatNumber(left.value - right.value)
            else:
                raise KaynatTypeError(
                    f"Cannot subtract {type(right).__name__} from {type(left).__name__}",
                    node.line,
                    node.column
                )
        
        elif node.operator in ('*', 'multiply', 'multiplied'):
            if isinstance(left, KaynatNumber) and isinstance(right, KaynatNumber):
                return KaynatNumber(left.value * right.value)
            else:
                raise KaynatTypeError(
                    f"Cannot multiply {type(left).__name__} and {type(right).__name__}",
                    node.line,
                    node.column
                )
        
        elif node.operator in ('/', 'divide', 'divided'):
            if isinstance(left, KaynatNumber) and isinstance(right, KaynatNumber):
                if right.value == 0:
                    raise KaynatRuntimeError(
                        "Cannot divide by zero",
                        node.line,
                        node.column
                    )
                return KaynatNumber(left.value / right.value)
            else:
                raise KaynatTypeError(
                    f"Cannot divide {type(left).__name__} by {type(right).__name__}",
                    node.line,
                    node.column
                )
        
        raise KaynatRuntimeError(
            f"Unknown binary operator: {node.operator}",
            node.line,
            node.column
        )
    
    def visit_UnaryOpNode(self, node: UnaryOpNode) -> KaynatValue:
        """Execute unary operation."""
        operand = self.visit(node.operand)
        
        if node.operator == '-':
            if isinstance(operand, KaynatNumber):
                return KaynatNumber(-operand.value)
            else:
                raise KaynatTypeError(
                    f"Cannot negate {type(operand).__name__}",
                    node.line,
                    node.column
                )
        
        elif node.operator == 'not':
            return KaynatBoolean(not operand.is_truthy())
        
        raise KaynatRuntimeError(
            f"Unknown unary operator: {node.operator}",
            node.line,
            node.column
        )
    
    def visit_ComparisonNode(self, node: ComparisonNode) -> KaynatBoolean:
        """Execute comparison."""
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if node.operator == '>':
            if isinstance(left, KaynatNumber) and isinstance(right, KaynatNumber):
                return KaynatBoolean(left.value > right.value)
        
        elif node.operator == '<':
            if isinstance(left, KaynatNumber) and isinstance(right, KaynatNumber):
                return KaynatBoolean(left.value < right.value)
        
        elif node.operator == '>=':
            if isinstance(left, KaynatNumber) and isinstance(right, KaynatNumber):
                return KaynatBoolean(left.value >= right.value)
        
        elif node.operator == '<=':
            if isinstance(left, KaynatNumber) and isinstance(right, KaynatNumber):
                return KaynatBoolean(left.value <= right.value)
        
        elif node.operator == '==':
            return KaynatBoolean(left.value == right.value)
        
        elif node.operator == '!=':
            return KaynatBoolean(left.value != right.value)
        
        raise KaynatTypeError(
            f"Cannot compare {type(left).__name__} and {type(right).__name__}",
            node.line,
            node.column
        )
    
    def visit_LogicalOpNode(self, node: LogicalOpNode) -> KaynatBoolean:
        """Execute logical operation."""
        left = self.visit(node.left)
        
        if node.operator == 'and':
            if not left.is_truthy():
                return KaynatBoolean(False)
            right = self.visit(node.right)
            return KaynatBoolean(right.is_truthy())
        
        elif node.operator == 'or':
            if left.is_truthy():
                return KaynatBoolean(True)
            right = self.visit(node.right)
            return KaynatBoolean(right.is_truthy())
        
        raise KaynatRuntimeError(
            f"Unknown logical operator: {node.operator}",
            node.line,
            node.column
        )
    
    def visit_IfNode(self, node: IfNode) -> Any:
        """Execute if statement."""
        condition = self.visit(node.condition)
        
        if condition.is_truthy():
            for stmt in node.then_block:
                self.visit(stmt)
            return None
        
        if node.elif_blocks:
            for elif_condition, elif_body in node.elif_blocks:
                condition = self.visit(elif_condition)
                if condition.is_truthy():
                    for stmt in elif_body:
                        self.visit(stmt)
                    return None
        
        if node.else_block:
            for stmt in node.else_block:
                self.visit(stmt)
        
        return None
    
    def visit_WhileNode(self, node: WhileNode) -> None:
        """Execute while loop."""
        try:
            while True:
                condition = self.visit(node.condition)
                if not condition.is_truthy():
                    break
                
                try:
                    for stmt in node.body:
                        self.visit(stmt)
                except ContinueException:
                    continue
        except BreakException:
            pass
        
        return None
    
    def visit_RepeatNode(self, node: RepeatNode) -> None:
        """Execute repeat loop."""
        count_val = self.visit(node.count)
        
        if not isinstance(count_val, KaynatNumber):
            raise KaynatTypeError(
                f"Repeat count must be a number, got {type(count_val).__name__}",
                node.line,
                node.column
            )
        
        count = int(count_val.value)
        
        try:
            for _ in range(count):
                try:
                    for stmt in node.body:
                        self.visit(stmt)
                except ContinueException:
                    continue
        except BreakException:
            pass
        
        return None
    
    def visit_ForEachNode(self, node: ForEachNode) -> None:
        """Execute for each loop."""
        iterable = self.visit(node.iterable)
        
        if not isinstance(iterable, KaynatList):
            raise KaynatTypeError(
                f"Can only iterate over lists, got {type(iterable).__name__}",
                node.line,
                node.column
            )
        
        # Create new scope for loop variable
        loop_env = Environment(self.current_env)
        prev_env = self.current_env
        self.current_env = loop_env
        
        try:
            for element in iterable.value:
                loop_env.define(node.variable, element)
                try:
                    for stmt in node.body:
                        self.visit(stmt)
                except ContinueException:
                    continue
        except BreakException:
            pass
        finally:
            self.current_env = prev_env
        
        return None
    
    def visit_LoopNode(self, node: LoopNode) -> None:
        """Execute loop from X to Y."""
        start_val = self.visit(node.start)
        end_val = self.visit(node.end)
        
        if not isinstance(start_val, KaynatNumber) or not isinstance(end_val, KaynatNumber):
            raise KaynatTypeError(
                "Loop bounds must be numbers",
                node.line,
                node.column
            )
        
        start = int(start_val.value)
        end = int(end_val.value)
        step = 1
        
        if node.step:
            step_val = self.visit(node.step)
            if not isinstance(step_val, KaynatNumber):
                raise KaynatTypeError(
                    "Loop step must be a number",
                    node.line,
                    node.column
                )
            step = int(step_val.value)
        
        # Create new scope for loop variable
        loop_env = Environment(self.current_env)
        prev_env = self.current_env
        self.current_env = loop_env
        
        try:
            current = start
            while (step > 0 and current <= end) or (step < 0 and current >= end):
                loop_env.define(node.variable, KaynatNumber(current))
                try:
                    for stmt in node.body:
                        self.visit(stmt)
                except ContinueException:
                    pass
                current += step
        except BreakException:
            pass
        finally:
            self.current_env = prev_env
        
        return None
    
    def visit_FunctionDefNode(self, node: FunctionDefNode) -> None:
        """Define a function."""
        func = KaynatFunction(node.name, node.parameters, node.body, self.current_env)
        self.current_env.define(node.name, func)
        return None
    
    def visit_FunctionCallNode(self, node: FunctionCallNode) -> KaynatValue:
        """Call a function."""
        func = self.current_env.get(node.name)
        
        if not isinstance(func, KaynatFunction):
            raise KaynatTypeError(
                f"'{node.name}' is not a function",
                node.line,
                node.column
            )
        
        # Evaluate arguments
        args = [self.visit(arg) for arg in node.arguments]
        
        # Check argument count
        if len(args) != len(func.parameters):
            raise KaynatRuntimeError(
                f"Function '{node.name}' expects {len(func.parameters)} arguments, got {len(args)}",
                node.line,
                node.column
            )
        
        # Create new environment for function
        func_env = Environment(func.env)
        for param, arg in zip(func.parameters, args):
            func_env.define(param, arg)
        
        # Execute function body
        prev_env = self.current_env
        self.current_env = func_env
        
        try:
            for stmt in func.body:
                self.visit(stmt)
            result = KaynatNull()
        except ReturnValue as ret:
            result = ret.value
        finally:
            self.current_env = prev_env
        
        return result
    
    def visit_ReturnNode(self, node: ReturnNode) -> None:
        """Execute return statement."""
        value = self.visit(node.value) if node.value else KaynatNull()
        raise ReturnValue(value)
    
    def visit_BreakNode(self, node: BreakNode) -> None:
        """Execute break statement."""
        raise BreakException()
    
    def visit_ContinueNode(self, node: ContinueNode) -> None:
        """Execute continue statement."""
        raise ContinueException()
    
    def visit_PrintNode(self, node: PrintNode) -> None:
        """Execute print statement."""
        values = []
        for val_node in node.values:
            # Special handling for identifiers - if undefined, treat as string
            if isinstance(val_node, IdentifierNode):
                if self.current_env.exists(val_node.name):
                    values.append(self.visit(val_node))
                else:
                    # Treat as string literal
                    values.append(KaynatString(val_node.name))
            else:
                values.append(self.visit(val_node))
        
        output = ' '.join(val.to_string() for val in values)
        print(output)
        return None
    
    def visit_InputNode(self, node: InputNode) -> None:
        """Execute input statement."""
        prompt = f"Enter {node.variable}: "
        user_input = input(prompt)
        self.current_env.define(node.variable, KaynatString(user_input))
        return None
    
    def visit_CommentNode(self, node: CommentNode) -> None:
        """Comments do nothing at runtime."""
        return None
