from commenUtils import get_input_data
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--log", default="info")

options = parser.parse_args()
levels = {'info': logging.INFO, 'debug': logging.DEBUG}

level = levels.get(options.log.lower())

logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    level=level)

logger = logging.getLogger(__name__)


def loop_through_commands(commands: list[(str, int)]) -> (bool, int):
    visited: set[int] = {0}
    current: int
    acc: int = 0
    next_ind: int
    len_of_commmands: int = len(commands)
    if commands[0][0] == "nop":
        next_ind = 1
    elif commands[0][0] == "acc":
        acc += commands[0][1]
        next_ind = 1
    else:
        next_ind = commands[0][1]
    while next_ind not in visited:
        logger.debug(f"Index: {next_ind}, Command: {commands[next_ind]}")
        visited.add(next_ind)
        if commands[next_ind][0] == "nop":
            next_ind += 1
        elif commands[next_ind][0] == "acc":
            acc += commands[next_ind][1]
            next_ind += 1
        else:
            next_ind += commands[next_ind][1]
        if next_ind >= len_of_commmands:
            return True, acc
    return False, acc


def solution_part_1(file_name: str) -> int:
    commands: list[(str, int)] = get_input_data(file_name)
    return loop_through_commands(commands)[1]


def solution_part_2(file_name: str) -> int:
    commands: list[(str, int)] = get_input_data(file_name)
    for index, command in enumerate(commands):
        if command[0] == "acc":
            continue
        if command[0] == "nop":
            commands_copy: list[(str, int)] = commands.copy()
            commands_copy[index] = ("jmp", command[1])
            loop_result: (bool, int) = loop_through_commands(commands_copy)
            if loop_result[0]:
                return loop_result[1]
            continue
        if command[0] == "jmp":
            commands_copy: list[(str, int)] = commands.copy()
            commands_copy[index] = ("nop", command[1])
            loop_result: (bool, int) = loop_through_commands(commands_copy)
            if loop_result[0]:
                return loop_result[1]
            continue
    return -1


if __name__ == '__main__':
    logger.info(solution_part_1("inputData.txt"))
    logger.info(solution_part_2("inputData.txt"))
