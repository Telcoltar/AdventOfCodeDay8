import logging

logger = logging.getLogger(__name__)


def get_input_data(input_file_name: str) -> list[(str, int)]:
    f = open(input_file_name, "r")
    commands: list[(str, int)] = []
    command: str
    number_str: int
    number: int
    for line in f:
        command, number_str = line.strip().split(" ")
        number = int(number_str)
        commands.append((command, number))
    f.close()
    return commands
