"""Main entry point for the Vector Editor CLI application"""

import sys

from cli.commands import CommandProcessor


def main():
    """Main function to run the vector editor."""
    processor = CommandProcessor()

    # If command line arguments are provided, process them and exit
    if len(sys.argv) > 1:
        command = " ".join(sys.argv[1:])
        result = processor.process_command(command)
        print(result)
        return

    # Otherwise, run in interactive mode
    processor.run_interactive()


if __name__ == "__main__":
    main()
