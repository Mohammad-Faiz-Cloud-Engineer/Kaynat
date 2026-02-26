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

# Import all stdlib modules
from kaynat.stdlib import math_tools
from kaynat.stdlib import string_tools
from kaynat.stdlib import list_tools
from kaynat.stdlib import file_tools
from kaynat.stdlib import date_tools
from kaynat.stdlib import random_tools
from kaynat.stdlib import network_tools
from kaynat.stdlib import json_tools
from kaynat.stdlib import crypto_tools
from kaynat.stdlib import pattern_tools


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
        # Math constants
        self.global_env.define('pi', KaynatNumber(math.pi), is_constant=True)
        self.global_env.define('e', KaynatNumber(math.e), is_constant=True)
        self.global_env.define('tau', KaynatNumber(math.tau), is_constant=True)
        self.global_env.define('infinity', KaynatNumber(math.inf), is_constant=True)
        
        # Register all stdlib functions as built-in callables
        self._register_stdlib_functions()
    
    def _register_stdlib_functions(self):
        """Register all standard library functions."""
        # Math tools
        stdlib_functions = {
            'sqrt': math_tools.sqrt,
            'abs_value': math_tools.abs_value,
            'round_number': math_tools.round_number,
            'ceiling': math_tools.ceiling,
            'floor': math_tools.floor,
            'pow': math_tools.power,  # 'power' is a keyword, use 'pow'
            'logarithm': math_tools.logarithm,
            'sin': math_tools.sin,
            'cos': math_tools.cos,
            'tan': math_tools.tan,
            'asin': math_tools.asin,
            'acos': math_tools.acos,
            'atan': math_tools.atan,
            'factorial': math_tools.factorial,
            'gcd': math_tools.gcd,
            'lcm': math_tools.lcm,
            'is_prime': math_tools.is_prime,
            'min_value': math_tools.min_value,
            'max_value': math_tools.max_value,
            'clamp': math_tools.clamp,
            
            # String tools
            'to_uppercase': string_tools.to_uppercase,
            'to_lowercase': string_tools.to_lowercase,
            'to_titlecase': string_tools.to_titlecase,
            'trim': string_tools.trim,
            'trim_left': string_tools.trim_left,
            'trim_right': string_tools.trim_right,
            'starts_with': string_tools.starts_with,
            'ends_with': string_tools.ends_with,
            'contains': string_tools.contains,
            'find_position': string_tools.find_position,
            'replace_text': string_tools.replace_text,
            'split_string': string_tools.split_string,
            'join_strings': string_tools.join_strings,
            'substring': string_tools.substring,
            'reverse_string': string_tools.reverse_string,
            'repeat_string': string_tools.repeat_string,
            'string_length': string_tools.string_length,
            'is_empty': string_tools.is_empty,
            'is_numeric': string_tools.is_numeric,
            'is_alphabetic': string_tools.is_alphabetic,
            'is_alphanumeric': string_tools.is_alphanumeric,
            'pad_left': string_tools.pad_left,
            'pad_right': string_tools.pad_right,
            'center_string': string_tools.center_string,
            
            # List tools
            'list_append': list_tools.list_append,
            'list_prepend': list_tools.list_prepend,
            'list_insert': list_tools.list_insert,
            'list_remove': list_tools.list_remove,
            'list_remove_at': list_tools.list_remove_at,
            'list_get': list_tools.list_get,
            'list_slice': list_tools.list_slice,
            'list_length': list_tools.list_length,
            'list_is_empty': list_tools.list_is_empty,
            'list_contains': list_tools.list_contains,
            'list_index_of': list_tools.list_index_of,
            'list_count': list_tools.list_count,
            'list_sort': list_tools.list_sort,
            'list_reverse': list_tools.list_reverse,
            'list_copy': list_tools.list_copy,
            'list_clear': list_tools.list_clear,
            'list_extend': list_tools.list_extend,
            'list_min': list_tools.list_min,
            'list_max': list_tools.list_max,
            'list_sum': list_tools.list_sum,
            'list_average': list_tools.list_average,
            
            # File tools
            'read_file': file_tools.read_file,
            'read_lines': file_tools.read_lines,
            'write_file': file_tools.write_file,
            'append_file': file_tools.append_file,
            'file_exists': file_tools.file_exists,
            'delete_file': file_tools.delete_file,
            'copy_file': file_tools.copy_file,
            'move_file': file_tools.move_file,
            'create_directory': file_tools.create_directory,
            'delete_directory': file_tools.delete_directory,
            'directory_exists': file_tools.directory_exists,
            'list_directory': file_tools.list_directory,
            
            # Date tools
            'current_date': date_tools.current_date,
            'current_time': date_tools.current_time,
            'current_timestamp': date_tools.current_timestamp,
            'format_date': date_tools.format_date,
            'parse_date': date_tools.parse_date,
            
            # Random tools
            'random_integer': random_tools.random_integer,
            'random_float': random_tools.random_float,
            'random_boolean': random_tools.random_boolean,
            'random_choice': random_tools.random_choice,
            'shuffle_list': random_tools.shuffle_list,
            'random_string': random_tools.random_string,
            
            # Network tools
            'fetch_url': network_tools.fetch_url,
            'is_url_reachable': network_tools.is_url_reachable,
            
            # JSON tools
            'parse_json': json_tools.parse_json,
            'generate_json': json_tools.generate_json,
            'format_json': json_tools.format_json,
            
            # Crypto tools
            'hash_sha256': crypto_tools.hash_sha256,
            'hash_md5': crypto_tools.hash_md5,
            'generate_token': crypto_tools.generate_token,
            'encode_base64': crypto_tools.encode_base64,
            'decode_base64': crypto_tools.decode_base64,
            
            # Pattern tools
            'find_matches': pattern_tools.find_matches,
            'matches_pattern': pattern_tools.matches_pattern,
            'replace_pattern': pattern_tools.replace_pattern,
            'split_by_pattern': pattern_tools.split_by_pattern,
            'is_valid_email': pattern_tools.is_valid_email,
            'is_valid_url': pattern_tools.is_valid_url,
        }
        
        # Wrap Python functions as Kaynat built-in functions
        for name, func in stdlib_functions.items():
            # Create a wrapper that can be called from Kaynat
            self.global_env.define(name, KaynatBuiltinFunction(name, func))
    
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
        """Look up a variable, or treat as string literal if undefined."""
        if self.current_env.exists(node.name):
            value = self.current_env.get(node.name)
            return value
        else:
            # Treat undefined identifiers as string literals
            return KaynatString(node.name)
    
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
        """Execute variable assignment or property assignment."""
        value = self.visit(node.value)
        
        # Check if this is a property assignment (my property or object.property)
        if ' ' in node.name:
            parts = node.name.split(' ', 1)
            if parts[0] in ('my', 'this'):
                # Property assignment: set my name to value
                from kaynat.oop.instance import Instance
                obj = self.current_env.get(parts[0])
                if isinstance(obj, Instance):
                    obj.properties[parts[1]] = value
                    return None
        
        # Regular variable assignment
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
        
        # Handle built-in functions
        if isinstance(func, KaynatBuiltinFunction):
            # Evaluate arguments
            args = [self.visit(arg) for arg in node.arguments]
            
            try:
                # Call the Python function
                result = func.call(*args)
                # Ensure result is a Kaynat value
                if not isinstance(result, KaynatValue):
                    if isinstance(result, bool):
                        result = KaynatBoolean(result)
                    elif isinstance(result, (int, float)):
                        result = KaynatNumber(result)
                    elif isinstance(result, str):
                        result = KaynatString(result)
                    elif isinstance(result, list):
                        result = KaynatList(result)
                    elif result is None:
                        result = KaynatNull()
                return result
            except Exception as e:
                raise KaynatRuntimeError(
                    f"Error calling built-in function '{node.name}': {str(e)}",
                    node.line,
                    node.column
                )
        
        # Handle user-defined functions
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

    
    def visit_ClassDefNode(self, node: ClassDefNode) -> None:
        """Define a class/blueprint."""
        from kaynat.oop.blueprint import Blueprint
        
        # Get parent class if exists
        parent_class = None
        if node.parent:
            parent_val = self.current_env.get(node.parent)
            if isinstance(parent_val, Blueprint):
                parent_class = parent_val
            else:
                raise KaynatTypeError(
                    f"'{node.parent}' is not a blueprint",
                    node.line,
                    node.column
                )
        
        # Create blueprint
        blueprint = Blueprint(
            name=node.name,
            properties=node.properties,
            methods={},
            parent=parent_class,
            is_abstract=node.is_abstract
        )
        
        # Add methods to blueprint
        for method in node.methods:
            # Store method as a function definition
            blueprint.methods[method.name] = method
        
        # Register blueprint in environment
        self.current_env.define(node.name, blueprint)
        return None
    
    def visit_CreateInstanceNode(self, node: CreateInstanceNode) -> None:
        """Create an instance of a class."""
        from kaynat.oop.blueprint import Blueprint
        from kaynat.oop.instance import Instance
        
        # Get the blueprint
        blueprint_val = self.current_env.get(node.class_name)
        if not isinstance(blueprint_val, Blueprint):
            raise KaynatTypeError(
                f"'{node.class_name}' is not a blueprint",
                node.line,
                node.column
            )
        
        # Check if blueprint is abstract
        if blueprint_val.is_abstract:
            raise KaynatRuntimeError(
                f"Cannot create instance of abstract blueprint '{node.class_name}'",
                node.line,
                node.column
            )
        
        # Create instance WITHOUT calling __init__ (we'll handle initialize ourselves)
        instance = Instance.__new__(Instance)
        instance.blueprint = blueprint_val
        instance.properties = {}
        
        # Initialize properties
        for prop in blueprint_val.properties:
            instance.properties[prop] = KaynatNull()
        
        # Evaluate constructor arguments
        args = [self.visit(arg) for arg in node.arguments]
        
        # Call initialize method if exists
        if 'initialize' in blueprint_val.methods:
            init_method = blueprint_val.methods['initialize']
            
            # Check argument count
            if len(args) != len(init_method.parameters):
                raise KaynatRuntimeError(
                    f"Constructor expects {len(init_method.parameters)} arguments, got {len(args)}",
                    node.line,
                    node.column
                )
            
            # Create environment for constructor
            init_env = Environment(self.current_env)
            init_env.define('my', instance)  # 'my' refers to current instance
            init_env.define('this', instance)  # 'this' also refers to current instance
            
            for param, arg in zip(init_method.parameters, args):
                init_env.define(param, arg)
            
            # Execute constructor
            prev_env = self.current_env
            self.current_env = init_env
            
            try:
                for stmt in init_method.body:
                    self.visit(stmt)
            except ReturnValue:
                pass  # Constructors don't return values
            finally:
                self.current_env = prev_env
        
        # Store instance in variable
        self.current_env.define(node.variable, instance)
        return None
    
    def visit_MethodCallNode(self, node: MethodCallNode) -> KaynatValue:
        """Call a method on an object."""
        from kaynat.oop.instance import Instance
        
        # Get the object
        obj = self.current_env.get(node.object_name)
        if not isinstance(obj, Instance):
            raise KaynatTypeError(
                f"'{node.object_name}' is not an object instance",
                node.line,
                node.column
            )
        
        # Get the method from blueprint
        if node.method_name not in obj.blueprint.methods:
            raise KaynatRuntimeError(
                f"Object of type '{obj.blueprint.name}' has no method '{node.method_name}'",
                node.line,
                node.column
            )
        
        method = obj.blueprint.methods[node.method_name]
        
        # Evaluate arguments
        args = [self.visit(arg) for arg in node.arguments]
        
        # Check argument count
        if len(args) != len(method.parameters):
            raise KaynatRuntimeError(
                f"Method '{node.method_name}' expects {len(method.parameters)} arguments, got {len(args)}",
                node.line,
                node.column
            )
        
        # Create environment for method
        method_env = Environment(self.current_env)
        method_env.define('my', obj)  # 'my' refers to current instance
        method_env.define('this', obj)  # 'this' also refers to current instance
        
        for param, arg in zip(method.parameters, args):
            method_env.define(param, arg)
        
        # Execute method
        prev_env = self.current_env
        self.current_env = method_env
        
        try:
            for stmt in method.body:
                self.visit(stmt)
            result = KaynatNull()
        except ReturnValue as ret:
            result = ret.value
        finally:
            self.current_env = prev_env
        
        return result
    
    def visit_PropertyAccessNode(self, node: PropertyAccessNode) -> KaynatValue:
        """Access a property on an object."""
        from kaynat.oop.instance import Instance
        
        # Handle 'my' keyword
        if node.object_name == 'my' or node.object_name == 'this':
            obj = self.current_env.get(node.object_name)
        else:
            obj = self.current_env.get(node.object_name)
        
        if not isinstance(obj, Instance):
            raise KaynatTypeError(
                f"'{node.object_name}' is not an object instance",
                node.line,
                node.column
            )
        
        # Get property value
        if node.property_name not in obj.properties:
            raise KaynatRuntimeError(
                f"Object of type '{obj.blueprint.name}' has no property '{node.property_name}'",
                node.line,
                node.column
            )
        
        return obj.properties[node.property_name]
    
    def visit_ContractDefNode(self, node: 'ContractDefNode') -> None:
        """Define a contract/interface."""
        from kaynat.oop.contract import Contract
        
        contract = Contract(
            name=node.name,
            required_methods=node.required_methods
        )
        
        self.current_env.define(node.name, contract)
        return None
