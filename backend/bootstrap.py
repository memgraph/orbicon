"""
Bootstraps python project

Script used to bootstrap python projects. Make sure to set the
<project name> in a Pythonic fashion where <project name> should
consist only of lowercase english letters and underscores.
Root directory will be named the same way as <project name> except that
every underscore will be replaced with a hyphen, e.g. my_new_project
becomes a directory my-new-project.

Example:
    python bootstrap.py my_new_project
    python bootstrap.py my_new_project ../my-new-project

If directory is omitted, then default directory will be
"../<project name>". If you set a custom destination directory and the
last path is not equal to <project name>, bootstrap will create an
additional folder in the destination directory that matches
<project name>.

Usage:
    bootstrap.py NAME [DIRECTORY]
    bootstrap.py -h | --help

Arguments:
    -h --help   Shows this screen.
    NAME        Project name
    DIRECTORY   Destination directory
"""

import logging
import os
import re
from collections.abc import Iterable
from pathlib import Path
from typing import Any, Optional

import pathspec

logging.basicConfig(format="%(asctime)-15s [%(levelname)s]: %(message)s")
logger = logging.getLogger("bootstrap")
logger.setLevel(logging.INFO)

TEMPLATE_NAME = "orbit_graph"

IGNORE_FILE_RULES = ".gitignore"
IGNORE_FILE_PREFIX = {".git/", "bootstrap.py"}


def list_files(path: Optional[str] = None) -> Iterable[str]:
    filenames = os.listdir(path)
    for filename in filenames:
        filepath = os.path.join(path or "", filename)
        if os.path.isdir(filepath):
            yield from list_files(filepath)
            continue
        if os.path.isfile(filepath):
            yield filepath


def filter_files(stream: Iterable[str], rules_filename: str) -> Iterable[str]:
    with open(rules_filename) as f:
        spec = pathspec.PathSpec.from_lines("gitwildmatch", f)

        for filename in stream:
            if any(filename.startswith(p) for p in IGNORE_FILE_PREFIX):
                continue
            if not spec.match_file(filename):
                yield filename


def create_bootstrap_file(source_filepath: str, name: str, destination: str):
    with open(source_filepath) as f:
        source_content = f.read()

        dest_filename = source_filepath.replace(TEMPLATE_NAME, name)
        dest_filepath = os.path.join(destination, dest_filename)

        if os.path.dirname(dest_filename):
            dest_folders = os.path.dirname(dest_filepath)
            logger.info(f'Creating folders "{dest_folders}"')
            os.makedirs(dest_folders, exist_ok=True)

        dest_content = source_content.replace(TEMPLATE_NAME, name)
        logger.info(f'Creating file "{dest_filepath}" from "{source_filepath}"')
        with open(dest_filepath, "w") as w:
            w.write(dest_content)


def validate_name(name: str) -> str:
    if not re.match(r"^[a-z]+(_[a-z]+)*$", name):
        raise ValueError('Project name can include only letters [a-z] and "_"')
    return name


def main(args: Dict[str, Any]):
    name = validate_name(args["NAME"])
    directory_name = name.replace("_", "-")
    directory = args.get("DIRECTORY") or Path(__file__).parent.joinpath("..").resolve()
    if os.path.basename(directory) != directory_name:
        directory = os.path.join(directory, directory_name)

    logger.info(f'Project name: "{name}"')
    logger.info(f'Project directory: "{directory}"')

    for filename in filter_files(list_files(), IGNORE_FILE_RULES):
        logger.info(f'Creating directory "{directory}"')
        os.makedirs(directory, exist_ok=True)
        create_bootstrap_file(filename, name, directory)


if __name__ == "__main__":
    from docopt import docopt

    main(docopt(__doc__))
