"""
Kaynat REPL - Interactive shell for Kaynat.

Read-Eval-Print Loop for testing and learning Kaynat.
"""

import sys
from kaynat.interpreter.interpreter import Interpreter
from kaynat.errors.error_types import KaynatError


def print_welcome():
    """Print welcome message."""
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║                                                           ║")
    print("║              Kaynat Programming Language                  ║")
    print("║                                                           ║")
    print("║         Code that reads like poetry                       ║")
    print("║                                                           ║")
    print("║  Named after Kaynat (Saista)                             ║")
    print("║  Built by Mohammad Faiz                                   ║")
    print("║                                                           ║")
    print("║  Type 'exit.' to quit                                     ║")
    print("║  Type 'help.' for help                                    ║")
    print("║                                                           ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print()


def print_help():
    """Print help message."""
    print("\nKaynat Quick Reference:")
    print("  Variables:    set x to 5.")
    print("  Print:        say hello, world.")
    print("  Input:        ask the user for name.")
    print("  If:           if x is greater than 5 then. ... end.")
    print("  While:        while x is less than 10. ... end.")
    print("  Repeat:       repeat 5 times. ... end.")
    print("  For each:     for each item in list. ... end.")
    print("  Function:     define a function called greet that takes name. ... end.")
    print("  Call:         call greet with John.")
    print("  Lists:        set items to a list containing 1, 2, 3.")
    print("  Arithmetic:   add 5 to x.")
    print("  Comments:     note. this is a comment.")
    print()


def start_repl() -> int:
    """
    Start the interactive REPL.
    
    Returns:
        Exit code
    """
    print_welcome()
    
    interpreter = Interpreter()
    statement_buffer = []
    in_block = False
    
    while True:
        try:
            # Prompt
            if in_block:
                prompt = "...  "
            else:
                prompt = ">>>  "
            
            # Read line
            try:
                line = input(prompt)
            except EOFError:
                print("\nGoodbye!")
                return 0
            
            # Skip empty lines
            if not line.strip():
                continue
            
            # Check for exit
            if line.strip().lower() in ('exit.', 'quit.', 'bye.'):
                print("Goodbye!")
                return 0
            
            # Check for help
            if line.strip().lower() == 'help.':
                print_help()
                continue
            
            # Add to buffer
            statement_buffer.append(line)
            
            # Check if we're in a block
            line_lower = line.strip().lower()
            if any(keyword in line_lower for keyword in ['then.', 'do.', 'times.']):
                in_block = True
                continue
            
            if line_lower == 'end.':
                in_block = False
            
            # If not in block and line ends with period, execute
            if not in_block and line.strip().endswith('.'):
                source = '\n'.join(statement_buffer)
                statement_buffer = []
                
                try:
                    result = interpreter.execute(source)
                    # Don't print None results
                    if result is not None and hasattr(result, 'to_string'):
                        print(f"  → {result.to_string()}")
                except KaynatError as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"Unexpected error: {e}")
        
        except KeyboardInterrupt:
            print("\nInterrupted. Type 'exit.' to quit.")
            statement_buffer = []
            in_block = False
            continue


if __name__ == '__main__':
    sys.exit(start_repl())
