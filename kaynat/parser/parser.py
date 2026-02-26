"""
Kaynat Parser - Builds AST from token stream.

Converts tokens into an Abstract Syntax Tree for execution.
"""

from typing import List, Optional
from kaynat.lexer.token_types import Token, TokenType
from kaynat.parser.nodes import *
from kaynat.errors.error_types import ParserError


class Parser:
    """
    Parses tokens into an Abstract Syntax Tree.
    
    Uses recursive descent parsing to build a tree structure
    that represents the program's logic.
    """
    
    def __init__(self, tokens: List[Token]):
        """
        Initialize parser with token stream.
        
        Args:
            tokens: List of tokens from lexer
        """
        self.tokens = tokens
        self.position = 0
    
    def current_token(self) -> Token:
        """Get current token without advancing."""
        if self.position >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[self.position]
    
    def peek_token(self, offset: int = 1) -> Token:
        """Look ahead at a token."""
        pos = self.position + offset
        if pos >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[pos]
    
    def advance(self) -> Token:
        """Move to next token and return current."""
        token = self.current_token()
        if self.position < len(self.tokens) - 1:
            self.position += 1
        return token
    
    def expect(self, token_type: TokenType) -> Token:
        """Expect a specific token type and advance."""
        token = self.current_token()
        if token.type != token_type:
            raise ParserError(
                f"Expected {token_type.name}, got {token.type.name}",
                token.line,
                token.column
            )
        return self.advance()
    
    def match(self, *token_types: TokenType) -> bool:
        """Check if current token matches any of the given types."""
        return self.current_token().type in token_types
    
    def parse(self) -> ProgramNode:
        """
        Parse the entire program.
        
        Returns:
            Root AST node containing all statements
        """
        statements = []
        
        # Check for begin program
        if self.match(TokenType.BEGIN):
            self.advance()
            self.expect(TokenType.PROGRAM)
            self.expect(TokenType.PERIOD)
        
        while not self.match(TokenType.EOF):
            if self.match(TokenType.END):
                self.advance()
                if self.match(TokenType.PROGRAM):
                    self.advance()
                    self.expect(TokenType.PERIOD)
                break
            
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        
        return ProgramNode(statements=statements)
    
    def parse_statement(self) -> Optional[ASTNode]:
        """Parse a single statement."""
        token = self.current_token()
        
        # Variable declaration: set x to 5.
        if self.match(TokenType.SET, TokenType.LET):
            return self.parse_variable_declaration()
        
        # Define can be variable, function, or blueprint
        if self.match(TokenType.DEFINE):
            # Look ahead to see what kind of definition this is
            next_token = self.peek_token()
            if next_token.type == TokenType.A:
                # Could be "define a function" or "define a blueprint"
                next_next = self.peek_token(2)
                if next_next.type == TokenType.BLUEPRINT:
                    return self.parse_class_def()
                elif next_next.type == TokenType.FUNCTION:
                    return self.parse_function_def()
                elif next_next.type == TokenType.CONTRACT:
                    return self.parse_contract_def()
            elif next_token.type == TokenType.FUNCTION:
                return self.parse_function_def()
            # Otherwise it's a variable declaration
            return self.parse_variable_declaration()
        
        # Constant: always set x as 5.
        if self.match(TokenType.ALWAYS):
            return self.parse_constant_declaration()
        
        # Reassignment: change x to 10.
        if self.match(TokenType.CHANGE):
            return self.parse_assignment()
        
        # Print: say hello.
        if self.match(TokenType.SAY, TokenType.PRINT, TokenType.SHOW):
            return self.parse_print()
        
        # Input: ask the user for name.
        if self.match(TokenType.ASK):
            return self.parse_input()
        
        # Conditional: if x is greater than 5 then.
        if self.match(TokenType.IF):
            return self.parse_if()
        
        # While loop: while x is less than 10.
        if self.match(TokenType.WHILE):
            return self.parse_while()
        
        # Repeat loop: repeat 10 times.
        if self.match(TokenType.REPEAT):
            return self.parse_repeat()
        
        # For each: for each item in list.
        if self.match(TokenType.FOR):
            return self.parse_for_each()
        
        # Loop: loop from 1 to 10.
        if self.match(TokenType.LOOP):
            return self.parse_loop()
        
        # Function definition: define a function called name.
        if self.match(TokenType.DEFINE):
            # Look ahead to see if this is a function definition
            if self.peek_token().type in (TokenType.A, TokenType.FUNCTION):
                return self.parse_function_def()
            # Otherwise it's a variable declaration
            return self.parse_variable_declaration()
        
        # Return: give back value.
        if self.match(TokenType.GIVE):
            return self.parse_return()
        
        # Function call: call function with args.
        if self.match(TokenType.CALL):
            # Look ahead to see if this is a method call
            # Pattern: call method on object with args.
            if self.peek_token(2).type == TokenType.ON:
                return self.parse_method_call_statement()
            return self.parse_function_call_statement()
        
        # Break: stop.
        if self.match(TokenType.STOP):
            self.advance()
            self.expect(TokenType.PERIOD)
            return BreakNode(line=token.line, column=token.column)
        
        # Continue: skip.
        if self.match(TokenType.SKIP):
            self.advance()
            self.expect(TokenType.PERIOD)
            return ContinueNode(line=token.line, column=token.column)
        
        # Arithmetic operations: add 5 to x.
        if self.match(TokenType.ADD, TokenType.SUBTRACT, TokenType.MULTIPLY, TokenType.DIVIDE):
            return self.parse_arithmetic_statement()
        
        # Comment: note. this is a comment.
        if self.match(TokenType.NOTE):
            return self.parse_comment()
        
        # Create list: create a list called items.
        if self.match(TokenType.CREATE):
            return self.parse_create()
        
        # List operations: add item to list.
        if self.match(TokenType.ADD) and self.is_list_operation():
            return self.parse_list_operation()
        
        # Unknown statement
        if not self.match(TokenType.EOF):
            raise ParserError(
                f"Unexpected token: {token.type.name}",
                token.line,
                token.column
            )
        
        return None
    
    def parse_variable_declaration(self) -> VariableDeclarationNode:
        """Parse: set x to 5 OR set my name to value."""
        token = self.advance()
        
        # Check for "my" keyword (property assignment in OOP)
        if self.match(TokenType.MY):
            self.advance()
            prop_name = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.TO)
            value = self.parse_expression()
            self.expect(TokenType.PERIOD)
            # Return as assignment with special name format
            return AssignmentNode(
                name=f"my {prop_name}",
                value=value,
                line=token.line,
                column=token.column
            )
        
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.TO)
        value = self.parse_expression()
        self.expect(TokenType.PERIOD)
        return VariableDeclarationNode(
            name=name,
            value=value,
            is_constant=False,
            line=token.line,
            column=token.column
        )
    
    def parse_constant_declaration(self) -> VariableDeclarationNode:
        """Parse: always set x as 5."""
        token = self.advance()
        self.expect(TokenType.SET)
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.AS)
        value = self.parse_expression()
        self.expect(TokenType.PERIOD)
        return VariableDeclarationNode(
            name=name,
            value=value,
            is_constant=True,
            line=token.line,
            column=token.column
        )
    
    def parse_assignment(self) -> AssignmentNode:
        """Parse: change x to 10 OR change my name to value."""
        token = self.advance()
        
        # Check for "my" keyword (property assignment in OOP)
        if self.match(TokenType.MY):
            self.advance()
            prop_name = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.TO)
            value = self.parse_expression()
            self.expect(TokenType.PERIOD)
            return AssignmentNode(
                name=f"my {prop_name}",
                value=value,
                line=token.line,
                column=token.column
            )
        
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.TO)
        value = self.parse_expression()
        self.expect(TokenType.PERIOD)
        return AssignmentNode(
            name=name,
            value=value,
            line=token.line,
            column=token.column
        )
    
    def parse_print(self) -> PrintNode:
        """Parse: say hello, world."""
        token = self.advance()
        values = []
        
        while not self.match(TokenType.PERIOD):
            # Check for property access: my property
            if self.match(TokenType.MY):
                my_token = self.advance()
                if self.match(TokenType.IDENTIFIER):
                    prop_name = self.advance().value
                    values.append(PropertyAccessNode(
                        object_name='my',
                        property_name=prop_name,
                        line=my_token.line,
                        column=my_token.column
                    ))
                else:
                    # Just "my" without property
                    values.append(StringNode(value='my', line=my_token.line, column=my_token.column))
            # Try to parse as expression first for numbers, booleans
            elif self.match(TokenType.NUMBER, TokenType.BOOLEAN, TokenType.NOTHING):
                values.append(self.parse_expression())
            # Identifiers could be variables or string literals
            elif self.match(TokenType.IDENTIFIER):
                id_token = self.advance()
                # Treat as identifier node - interpreter will handle lookup
                values.append(IdentifierNode(name=id_token.value, line=id_token.line, column=id_token.column))
            # Keywords and other words become string literals
            else:
                word_token = self.advance()
                values.append(StringNode(value=str(word_token.value), line=word_token.line, column=word_token.column))
            
            if self.match(TokenType.COMMA):
                self.advance()
        
        self.expect(TokenType.PERIOD)
        return PrintNode(values=values, line=token.line, column=token.column)
    
    def parse_input(self) -> InputNode:
        """Parse: ask the user for name."""
        token = self.advance()
        self.expect(TokenType.THE)
        self.expect(TokenType.USER)
        self.expect(TokenType.FOR)
        variable = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.PERIOD)
        return InputNode(
            prompt=None,
            variable=variable,
            line=token.line,
            column=token.column
        )
    
    def parse_if(self) -> IfNode:
        """Parse: if condition then ... end."""
        token = self.advance()
        condition = self.parse_condition()
        self.expect(TokenType.THEN)
        self.expect(TokenType.PERIOD)
        
        then_block = []
        while not self.match(TokenType.OTHERWISE, TokenType.END, TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                then_block.append(stmt)
        
        elif_blocks = []
        else_block = None
        
        while self.match(TokenType.OTHERWISE):
            self.advance()
            if self.match(TokenType.IF):
                self.advance()
                elif_condition = self.parse_condition()
                self.expect(TokenType.THEN)
                self.expect(TokenType.PERIOD)
                elif_body = []
                while not self.match(TokenType.OTHERWISE, TokenType.END, TokenType.EOF):
                    stmt = self.parse_statement()
                    if stmt:
                        elif_body.append(stmt)
                elif_blocks.append((elif_condition, elif_body))
            else:
                self.expect(TokenType.PERIOD)
                else_block = []
                while not self.match(TokenType.END, TokenType.EOF):
                    stmt = self.parse_statement()
                    if stmt:
                        else_block.append(stmt)
                break
        
        self.expect(TokenType.END)
        self.expect(TokenType.PERIOD)
        
        return IfNode(
            condition=condition,
            then_block=then_block,
            elif_blocks=elif_blocks if elif_blocks else None,
            else_block=else_block,
            line=token.line,
            column=token.column
        )
    
    def parse_while(self) -> WhileNode:
        """Parse: while condition ... end."""
        token = self.advance()
        condition = self.parse_condition()
        
        # Optional "then"
        if self.match(TokenType.THEN):
            self.advance()
        
        self.expect(TokenType.PERIOD)
        
        body = []
        while not self.match(TokenType.END, TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
        
        self.expect(TokenType.END)
        self.expect(TokenType.PERIOD)
        
        return WhileNode(
            condition=condition,
            body=body,
            line=token.line,
            column=token.column
        )
    
    def parse_repeat(self) -> RepeatNode:
        """Parse: repeat 10 times ... end."""
        token = self.advance()
        count = self.parse_expression()
        self.expect(TokenType.TIMES)
        self.expect(TokenType.PERIOD)
        
        body = []
        while not self.match(TokenType.END, TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
        
        self.expect(TokenType.END)
        self.expect(TokenType.PERIOD)
        
        return RepeatNode(
            count=count,
            body=body,
            line=token.line,
            column=token.column
        )
    
    def parse_for_each(self) -> ForEachNode:
        """Parse: for each item in list ... end."""
        token = self.advance()
        self.expect(TokenType.EACH)
        variable = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.IN)
        
        # The iterable should be an identifier (variable name)
        iterable_token = self.expect(TokenType.IDENTIFIER)
        iterable = IdentifierNode(name=iterable_token.value, line=iterable_token.line, column=iterable_token.column)
        
        self.expect(TokenType.PERIOD)
        
        body = []
        while not self.match(TokenType.END, TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
        
        self.expect(TokenType.END)
        self.expect(TokenType.PERIOD)
        
        return ForEachNode(
            variable=variable,
            iterable=iterable,
            body=body,
            line=token.line,
            column=token.column
        )
    
    def parse_loop(self) -> LoopNode:
        """Parse: loop from 1 to 10 stepping by 2 ... end."""
        token = self.advance()
        self.expect(TokenType.FROM)
        start = self.parse_expression()
        self.expect(TokenType.TO)
        end = self.parse_expression()
        
        step = None
        if self.match(TokenType.STEPPING):
            self.advance()
            self.expect(TokenType.BY)
            step = self.parse_expression()
        
        self.expect(TokenType.PERIOD)
        
        body = []
        while not self.match(TokenType.END, TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
        
        self.expect(TokenType.END)
        self.expect(TokenType.PERIOD)
        
        return LoopNode(
            variable='current',
            start=start,
            end=end,
            step=step,
            body=body,
            line=token.line,
            column=token.column
        )
    
    def parse_function_def(self) -> FunctionDefNode:
        """Parse: define a function called name that takes x, y ... end."""
        token = self.advance()
        
        # Skip "a" if present
        if self.match(TokenType.A):
            self.advance()
        
        self.expect(TokenType.FUNCTION)
        self.expect(TokenType.CALLED)
        name = self.expect(TokenType.IDENTIFIER).value
        
        parameters = []
        if self.match(TokenType.THAT):
            self.advance()
            self.expect(TokenType.TAKES)
            
            # Parameters can be identifiers or single letters
            param_token = self.current_token()
            if self.match(TokenType.IDENTIFIER):
                parameters.append(self.advance().value)
            elif self.match(TokenType.A):
                parameters.append('a')
                self.advance()
            else:
                raise ParserError(f"Expected parameter name", param_token.line, param_token.column)
            
            while self.match(TokenType.COMMA):
                self.advance()
                param_token = self.current_token()
                if self.match(TokenType.IDENTIFIER):
                    parameters.append(self.advance().value)
                elif self.match(TokenType.A):
                    parameters.append('a')
                    self.advance()
                else:
                    raise ParserError(f"Expected parameter name", param_token.line, param_token.column)
        
        self.expect(TokenType.PERIOD)
        
        body = []
        while not self.match(TokenType.END, TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
        
        self.expect(TokenType.END)
        self.expect(TokenType.PERIOD)
        
        return FunctionDefNode(
            name=name,
            parameters=parameters,
            body=body,
            line=token.line,
            column=token.column
        )
    
    def parse_return(self) -> ReturnNode:
        """Parse: give back value."""
        token = self.advance()
        self.expect(TokenType.BACK)
        value = self.parse_expression()
        self.expect(TokenType.PERIOD)
        return ReturnNode(value=value, line=token.line, column=token.column)
    
    def parse_function_call_statement(self) -> ASTNode:
        """Parse: call function with arg1, arg2 [and store as result]."""
        token = self.advance()
        name = self.expect(TokenType.IDENTIFIER).value
        
        arguments = []
        if self.match(TokenType.WITH):
            self.advance()
            # Parse arguments, but stop at "and store"
            arguments.append(self.parse_function_argument())
            while self.match(TokenType.COMMA):
                self.advance()
                arguments.append(self.parse_function_argument())
        
        # Check for "and store as variable"
        if self.match(TokenType.AND):
            self.advance()
            self.expect(TokenType.STORE)
            self.expect(TokenType.AS)
            result_var = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.PERIOD)
            
            # Return a variable declaration node that calls the function
            return VariableDeclarationNode(
                name=result_var,
                value=FunctionCallNode(
                    name=name,
                    arguments=arguments,
                    line=token.line,
                    column=token.column
                ),
                is_constant=False,
                line=token.line,
                column=token.column
            )
        
        self.expect(TokenType.PERIOD)
        return FunctionCallNode(
            name=name,
            arguments=arguments,
            line=token.line,
            column=token.column
        )
    
    def parse_function_argument(self) -> ASTNode:
        """Parse a function argument, stopping at 'and store'."""
        # In function arguments, identifiers are always variable references
        token = self.current_token()
        
        # Number
        if self.match(TokenType.NUMBER):
            self.advance()
            return NumberNode(value=token.value, line=token.line, column=token.column)
        
        # Boolean
        if self.match(TokenType.BOOLEAN):
            self.advance()
            return BooleanNode(value=token.value, line=token.line, column=token.column)
        
        # Null
        if self.match(TokenType.NOTHING):
            self.advance()
            return NullNode(line=token.line, column=token.column)
        
        # Identifier - always treat as variable reference in function arguments
        if self.match(TokenType.IDENTIFIER):
            self.advance()
            return IdentifierNode(name=token.value, line=token.line, column=token.column)
        
        # List literal
        if self.match(TokenType.A) and self.peek_token().type == TokenType.LIST:
            self.advance()
            self.advance()
            self.expect(TokenType.CONTAINING)
            elements = []
            elements.append(self.parse_function_argument())
            while self.match(TokenType.COMMA):
                self.advance()
                elements.append(self.parse_function_argument())
            return ListNode(elements=elements, line=token.line, column=token.column)
        
        # For other expressions, use comparison parsing
        return self.parse_comparison()
        return FunctionCallNode(
            name=name,
            arguments=arguments,
            line=token.line,
            column=token.column
        )
    
    def parse_arithmetic_statement(self) -> BinaryOpNode:
        """Parse: add 5 to x."""
        token = self.current_token()
        op = self.advance().value
        value = self.parse_expression()
        self.expect(TokenType.TO if op == 'add' else TokenType.FROM)
        target = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.PERIOD)
        
        # Convert to assignment: x = x + 5
        return AssignmentNode(
            name=target,
            value=BinaryOpNode(
                operator=op,
                left=IdentifierNode(name=target),
                right=value
            ),
            line=token.line,
            column=token.column
        )
    
    def parse_comment(self) -> CommentNode:
        """Parse: note. this is a comment."""
        token = self.advance()
        self.expect(TokenType.PERIOD)
        # Comments are just markers - content is ignored
        return CommentNode(text="", line=token.line, column=token.column)
    
    def parse_create(self) -> ASTNode:
        """Parse: create a list called items OR create a new Animal called dog."""
        token = self.advance()
        self.expect(TokenType.A)
        
        # Check for "new" keyword (OOP instance creation)
        if self.match(TokenType.NEW):
            self.advance()
            class_name = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.CALLED)
            variable = self.expect(TokenType.IDENTIFIER).value
            
            # Check for constructor arguments
            arguments = []
            if self.match(TokenType.WITH):
                self.advance()
                arguments.append(self.parse_function_argument())
                # Handle both comma and "and" as separators
                while self.match(TokenType.COMMA, TokenType.AND):
                    self.advance()
                    arguments.append(self.parse_function_argument())
            
            self.expect(TokenType.PERIOD)
            return CreateInstanceNode(
                class_name=class_name,
                arguments=arguments,
                variable=variable,
                line=token.line,
                column=token.column
            )
        
        # List creation
        if self.match(TokenType.LIST):
            self.advance()
            self.expect(TokenType.CALLED)
            name = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.PERIOD)
            return VariableDeclarationNode(
                name=name,
                value=ListNode(elements=[]),
                line=token.line,
                column=token.column
            )
        
        # Map creation
        elif self.match(TokenType.MAP):
            self.advance()
            self.expect(TokenType.CALLED)
            name = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.PERIOD)
            return VariableDeclarationNode(
                name=name,
                value=MapNode(pairs=[]),
                line=token.line,
                column=token.column
            )
        
        raise ParserError(
            f"Unknown create statement",
            token.line,
            token.column
        )
    
    def is_list_operation(self) -> bool:
        """Check if this is a list operation."""
        # Look ahead to see if pattern matches list operation
        return True
    
    def parse_list_operation(self) -> ListOperationNode:
        """Parse list operations like: add item to list."""
        token = self.current_token()
        # Simplified - would need full implementation
        raise ParserError("List operations not yet implemented", token.line, token.column)
    
    def parse_condition(self) -> ASTNode:
        """Parse a condition expression."""
        left = self.parse_expression()
        
        if self.match(TokenType.IS):
            self.advance()
            
            # is greater than
            if self.match(TokenType.GREATER):
                self.advance()
                self.expect(TokenType.THAN)
                right = self.parse_expression()
                return ComparisonNode(operator='>', left=left, right=right)
            
            # is less than
            elif self.match(TokenType.LESS):
                self.advance()
                self.expect(TokenType.THAN)
                right = self.parse_expression()
                return ComparisonNode(operator='<', left=left, right=right)
            
            # is equal to
            elif self.match(TokenType.EQUAL):
                self.advance()
                self.expect(TokenType.TO)
                right = self.parse_expression()
                return ComparisonNode(operator='==', left=left, right=right)
            
            # is not equal to
            elif self.match(TokenType.NOT):
                self.advance()
                self.expect(TokenType.EQUAL)
                self.expect(TokenType.TO)
                right = self.parse_expression()
                return ComparisonNode(operator='!=', left=left, right=right)
        
        return left
    
    def parse_expression(self) -> ASTNode:
        """Parse an expression."""
        return self.parse_logical_or()
    
    def parse_logical_or(self) -> ASTNode:
        """Parse logical OR."""
        left = self.parse_logical_and()
        
        while self.match(TokenType.OR):
            self.advance()
            right = self.parse_logical_and()
            left = LogicalOpNode(operator='or', left=left, right=right)
        
        return left
    
    def parse_logical_and(self) -> ASTNode:
        """Parse logical AND."""
        left = self.parse_comparison()
        
        while self.match(TokenType.AND):
            self.advance()
            right = self.parse_comparison()
            left = LogicalOpNode(operator='and', left=left, right=right)
        
        return left
    
    def parse_comparison(self) -> ASTNode:
        """Parse comparison."""
        left = self.parse_additive()
        
        if self.match(TokenType.IS):
            self.advance()
            if self.match(TokenType.GREATER):
                self.advance()
                self.expect(TokenType.THAN)
                right = self.parse_additive()
                return ComparisonNode(operator='>', left=left, right=right)
            elif self.match(TokenType.LESS):
                self.advance()
                self.expect(TokenType.THAN)
                right = self.parse_additive()
                return ComparisonNode(operator='<', left=left, right=right)
            elif self.match(TokenType.EQUAL):
                self.advance()
                self.expect(TokenType.TO)
                right = self.parse_additive()
                return ComparisonNode(operator='==', left=left, right=right)
        
        return left
    
    def parse_additive(self) -> ASTNode:
        """Parse addition and subtraction."""
        left = self.parse_multiplicative()
        
        while self.match(TokenType.PLUS, TokenType.MINUS):
            op = '+' if self.current_token().type == TokenType.PLUS else '-'
            self.advance()
            right = self.parse_multiplicative()
            left = BinaryOpNode(operator=op, left=left, right=right)
        
        return left
    
    def parse_multiplicative(self) -> ASTNode:
        """Parse multiplication and division."""
        left = self.parse_unary()
        
        while self.match(TokenType.MULTIPLIED):
            self.advance()
            self.expect(TokenType.BY)
            right = self.parse_unary()
            left = BinaryOpNode(operator='*', left=left, right=right)
        
        return left
    
    def parse_unary(self) -> ASTNode:
        """Parse unary operations."""
        if self.match(TokenType.NEGATIVE):
            token = self.advance()
            operand = self.parse_unary()
            return UnaryOpNode(
                operator='-',
                operand=operand,
                line=token.line,
                column=token.column
            )
        
        if self.match(TokenType.NOT):
            token = self.advance()
            operand = self.parse_unary()
            return UnaryOpNode(
                operator='not',
                operand=operand,
                line=token.line,
                column=token.column
            )
        
        return self.parse_primary()
    
    def parse_primary(self) -> ASTNode:
        """Parse primary expressions."""
        token = self.current_token()
        
        # Number
        if self.match(TokenType.NUMBER):
            self.advance()
            return NumberNode(value=token.value, line=token.line, column=token.column)
        
        # Boolean
        if self.match(TokenType.BOOLEAN):
            self.advance()
            return BooleanNode(value=token.value, line=token.line, column=token.column)
        
        # Null
        if self.match(TokenType.NOTHING):
            self.advance()
            return NullNode(line=token.line, column=token.column)
        
        # Property access: my property
        if self.match(TokenType.MY):
            self.advance()
            prop_name = self.expect(TokenType.IDENTIFIER).value
            return PropertyAccessNode(
                object_name='my',
                property_name=prop_name,
                line=token.line,
                column=token.column
            )
        
        # Identifier - always treat as identifier, interpreter will handle lookup
        if self.match(TokenType.IDENTIFIER):
            self.advance()
            return IdentifierNode(name=token.value, line=token.line, column=token.column)
        
        # List literal: a list containing 1, 2, 3
        if self.match(TokenType.A) and self.peek_token().type == TokenType.LIST:
            self.advance()
            self.advance()
            self.expect(TokenType.CONTAINING)
            elements = []
            elements.append(self.parse_expression())
            while self.match(TokenType.COMMA):
                self.advance()
                elements.append(self.parse_expression())
            return ListNode(elements=elements, line=token.line, column=token.column)
        
        raise ParserError(
            f"Unexpected token in expression: {token.type.name}",
            token.line,
            token.column
        )

    
    def parse_class_def(self) -> ClassDefNode:
        """Parse: define a blueprint called Animal."""
        token = self.advance()  # DEFINE
        self.expect(TokenType.A)
        
        # Check for abstract
        is_abstract = False
        if self.match(TokenType.ABSTRACT):
            self.advance()
            is_abstract = True
        
        self.expect(TokenType.BLUEPRINT)
        self.expect(TokenType.CALLED)
        name = self.expect(TokenType.IDENTIFIER).value
        
        # Check for inheritance
        parent = None
        if self.match(TokenType.EXTENDS):
            self.advance()
            parent = self.expect(TokenType.IDENTIFIER).value
        
        self.expect(TokenType.PERIOD)
        
        # Parse properties and methods
        properties = []
        methods = []
        
        while not self.match(TokenType.END, TokenType.EOF):
            # Property: it has name.
            if self.match(TokenType.IT):
                self.advance()
                self.expect(TokenType.HAS)
                prop_name = self.expect(TokenType.IDENTIFIER).value
                self.expect(TokenType.PERIOD)
                properties.append(prop_name)
            
            # Method: to methodname, do. ... end.
            elif self.match(TokenType.TO):
                method = self.parse_method()
                methods.append(method)
            
            else:
                break
        
        self.expect(TokenType.END)
        self.expect(TokenType.PERIOD)
        
        return ClassDefNode(
            name=name,
            parent=parent,
            properties=properties,
            methods=methods,
            is_abstract=is_abstract,
            line=token.line,
            column=token.column
        )
    
    def parse_method(self) -> FunctionDefNode:
        """Parse: to methodname, do. ... end."""
        token = self.advance()  # TO
        
        # Method name can be an identifier or special keywords like "initialize"
        if self.match(TokenType.IDENTIFIER):
            name = self.advance().value
        elif self.match(TokenType.INITIALIZE):
            name = 'initialize'
            self.advance()
        else:
            raise ParserError(
                f"Expected method name, got {self.current_token().type.name}",
                self.current_token().line,
                self.current_token().column
            )
        
        parameters = []
        # Check for parameters: to methodname, take x, y OR to methodname, take x and y.
        if self.match(TokenType.COMMA):
            self.advance()
            if self.match(TokenType.TAKE):
                self.advance()
                param_token = self.current_token()
                if self.match(TokenType.IDENTIFIER):
                    parameters.append(self.advance().value)
                
                # Handle both comma and "and" as separators
                while self.match(TokenType.COMMA, TokenType.AND):
                    self.advance()
                    param_token = self.current_token()
                    if self.match(TokenType.IDENTIFIER):
                        parameters.append(self.advance().value)
        
        # Expect "do" or just period
        if self.match(TokenType.COMMA):
            self.advance()
        if self.match(TokenType.DO):
            self.advance()
        self.expect(TokenType.PERIOD)
        
        # Parse method body
        body = []
        while not self.match(TokenType.END, TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                body.append(stmt)
        
        self.expect(TokenType.END)
        self.expect(TokenType.PERIOD)
        
        return FunctionDefNode(
            name=name,
            parameters=parameters,
            body=body,
            line=token.line,
            column=token.column
        )
    
    def parse_contract_def(self) -> 'ContractDefNode':
        """Parse: define a contract called Speakable."""
        token = self.advance()  # DEFINE
        self.expect(TokenType.A)
        self.expect(TokenType.CONTRACT)
        self.expect(TokenType.CALLED)
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.PERIOD)
        
        # Parse required methods
        methods = []
        while not self.match(TokenType.END, TokenType.EOF):
            if self.match(TokenType.IT):
                self.advance()
                self.expect(TokenType.REQUIRES)
                method_name = self.expect(TokenType.IDENTIFIER).value
                self.expect(TokenType.PERIOD)
                methods.append(method_name)
            else:
                break
        
        self.expect(TokenType.END)
        self.expect(TokenType.PERIOD)
        
        # Create a simple node for contracts
        from kaynat.parser.nodes import ContractDefNode
        return ContractDefNode(
            name=name,
            required_methods=methods,
            line=token.line,
            column=token.column
        )

    
    def parse_method_call_statement(self) -> ASTNode:
        """Parse: call method on object with arg1, arg2 [and store as result]."""
        token = self.advance()  # CALL
        method_name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.ON)
        object_name = self.expect(TokenType.IDENTIFIER).value
        
        arguments = []
        if self.match(TokenType.WITH):
            self.advance()
            arguments.append(self.parse_function_argument())
            while self.match(TokenType.COMMA):
                self.advance()
                arguments.append(self.parse_function_argument())
        
        # Check for "and store as variable"
        if self.match(TokenType.AND):
            self.advance()
            self.expect(TokenType.STORE)
            self.expect(TokenType.AS)
            result_var = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.PERIOD)
            
            # Return a variable declaration node that calls the method
            return VariableDeclarationNode(
                name=result_var,
                value=MethodCallNode(
                    object_name=object_name,
                    method_name=method_name,
                    arguments=arguments,
                    line=token.line,
                    column=token.column
                ),
                is_constant=False,
                line=token.line,
                column=token.column
            )
        
        self.expect(TokenType.PERIOD)
        return MethodCallNode(
            object_name=object_name,
            method_name=method_name,
            arguments=arguments,
            line=token.line,
            column=token.column
        )
