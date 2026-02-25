"""
AST Node Definitions for Kaynat.

Every construct in the language has a corresponding node type.
"""

from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class ASTNode:
    """Base class for all AST nodes."""
    pass


@dataclass
class ProgramNode(ASTNode):
    """Root node containing all statements."""
    statements: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class NumberNode(ASTNode):
    """Numeric literal."""
    value: float
    line: int = 0
    column: int = 0


@dataclass
class StringNode(ASTNode):
    """String literal."""
    value: str
    line: int = 0
    column: int = 0


@dataclass
class BooleanNode(ASTNode):
    """Boolean literal."""
    value: bool
    line: int = 0
    column: int = 0


@dataclass
class NullNode(ASTNode):
    """Null/nothing value."""
    line: int = 0
    column: int = 0


@dataclass
class IdentifierNode(ASTNode):
    """Variable or function name."""
    name: str
    line: int = 0
    column: int = 0


@dataclass
class ListNode(ASTNode):
    """List literal."""
    elements: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class MapNode(ASTNode):
    """Dictionary/map literal."""
    pairs: List[tuple]
    line: int = 0
    column: int = 0


@dataclass
class VariableDeclarationNode(ASTNode):
    """Variable declaration: set x to 5."""
    name: str
    value: ASTNode
    is_constant: bool = False
    line: int = 0
    column: int = 0


@dataclass
class AssignmentNode(ASTNode):
    """Variable reassignment: change x to 10."""
    name: str
    value: ASTNode
    line: int = 0
    column: int = 0


@dataclass
class BinaryOpNode(ASTNode):
    """Binary operation: add, subtract, multiply, etc."""
    operator: str
    left: ASTNode
    right: ASTNode
    line: int = 0
    column: int = 0


@dataclass
class UnaryOpNode(ASTNode):
    """Unary operation: negative, not, etc."""
    operator: str
    operand: ASTNode
    line: int = 0
    column: int = 0


@dataclass
class ComparisonNode(ASTNode):
    """Comparison: is greater than, is equal to, etc."""
    operator: str
    left: ASTNode
    right: ASTNode
    line: int = 0
    column: int = 0


@dataclass
class LogicalOpNode(ASTNode):
    """Logical operation: and, or, not."""
    operator: str
    left: ASTNode
    right: Optional[ASTNode] = None
    line: int = 0
    column: int = 0


@dataclass
class IfNode(ASTNode):
    """Conditional statement."""
    condition: ASTNode
    then_block: List[ASTNode]
    elif_blocks: List[tuple] = None
    else_block: List[ASTNode] = None
    line: int = 0
    column: int = 0


@dataclass
class WhileNode(ASTNode):
    """While loop."""
    condition: ASTNode
    body: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class RepeatNode(ASTNode):
    """Repeat N times loop."""
    count: ASTNode
    body: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class ForEachNode(ASTNode):
    """For each loop."""
    variable: str
    iterable: ASTNode
    body: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class LoopNode(ASTNode):
    """Loop from X to Y."""
    variable: str
    start: ASTNode
    end: ASTNode
    step: Optional[ASTNode]
    body: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class BreakNode(ASTNode):
    """Break statement (stop)."""
    line: int = 0
    column: int = 0


@dataclass
class ContinueNode(ASTNode):
    """Continue statement (skip)."""
    line: int = 0
    column: int = 0


@dataclass
class FunctionDefNode(ASTNode):
    """Function definition."""
    name: str
    parameters: List[str]
    body: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class ReturnNode(ASTNode):
    """Return statement (give back)."""
    value: Optional[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class FunctionCallNode(ASTNode):
    """Function call."""
    name: str
    arguments: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class PrintNode(ASTNode):
    """Print/say statement."""
    values: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class InputNode(ASTNode):
    """Input from user."""
    prompt: Optional[ASTNode]
    variable: str
    line: int = 0
    column: int = 0


@dataclass
class ListOperationNode(ASTNode):
    """List operation: add, remove, get, etc."""
    operation: str
    list_name: str
    arguments: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class StringOperationNode(ASTNode):
    """String operation: join, split, uppercase, etc."""
    operation: str
    arguments: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class MathOperationNode(ASTNode):
    """Math operation: sqrt, sin, cos, etc."""
    operation: str
    arguments: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class FileOperationNode(ASTNode):
    """File operation: read, write, append, etc."""
    operation: str
    arguments: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class TryNode(ASTNode):
    """Try-catch block (attempt)."""
    try_block: List[ASTNode]
    catch_variable: Optional[str]
    catch_block: List[ASTNode]
    finally_block: Optional[List[ASTNode]]
    line: int = 0
    column: int = 0


@dataclass
class RaiseNode(ASTNode):
    """Raise error."""
    message: ASTNode
    line: int = 0
    column: int = 0


@dataclass
class ClassDefNode(ASTNode):
    """Class/blueprint definition."""
    name: str
    parent: Optional[str]
    properties: List[str]
    methods: List[FunctionDefNode]
    is_abstract: bool = False
    line: int = 0
    column: int = 0


@dataclass
class MethodCallNode(ASTNode):
    """Method call on object."""
    object_name: str
    method_name: str
    arguments: List[ASTNode]
    line: int = 0
    column: int = 0


@dataclass
class PropertyAccessNode(ASTNode):
    """Property access: my name."""
    object_name: str
    property_name: str
    line: int = 0
    column: int = 0


@dataclass
class CreateInstanceNode(ASTNode):
    """Create new instance of class."""
    class_name: str
    arguments: List[ASTNode]
    variable: str
    line: int = 0
    column: int = 0


@dataclass
class CommentNode(ASTNode):
    """Comment (note)."""
    text: str
    line: int = 0
    column: int = 0
