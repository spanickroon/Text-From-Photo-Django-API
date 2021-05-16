#!/usr/bin/env python

import os


def read_from_file(file_path: str) -> str:
    with open(os.path.abspath(os.getcwd()) + file_path, "r") as rf:
        return rf.read()


def write_to_file(file_path: str, data: str) -> None:
    with open(os.path.abspath(os.getcwd()) + file_path, "w") as wf:
        wf.write(data)


def parse_dev_env(data: str):
    list_env = [
            f"{i[:i.index('=')+1]}'{i[i.index('=')+1:]}'"
            for i in list(filter(None, data.split("\n")))
        ]
    list_env.pop(list_env.index("DJANGO_LOCAL_TESTING_MODE='False'"))
    list_env.append("DJANGO_LOCAL_TESTING_MODE='True'")

    return "\n".join(
        list_env
    )


def main() -> None:
    write_to_file(
        "/variables/console_dev.env",
        parse_dev_env(read_from_file("/variables/dev.env")),
    )


if __name__ == "__main__":
    main()
