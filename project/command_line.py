import os
import random
import string
import sys
from dataclasses import dataclass, field

import utils


@dataclass
class CLArgs:
    PASSWORD_LEN = 12
    using_dict: bool = field(default=False)
    dict_path: str = field(default="")


def __parse_args() -> CLArgs:
    out = CLArgs()

    for index, value in enumerate(sys.argv):
        if value == "-use_dict":
            out.using_dict = True
            if len(sys.argv) > index + 1:
                out.dict_path = sys.argv[index + 1]

    return out


def __validate_args(args: CLArgs) -> CLArgs:
    if args.dict_path == "":
        return args

    if not os.path.exists(args.dict_path):
        raise OSError(f"Path {args.dict_path} does not exist")
    if not os.path.isfile(args.dict_path):
        raise OSError(f"Path {args.dict_path} is not a file")
    if not os.access(args.dict_path, os.R_OK):
        raise OSError(f"Cannot read from file {args.dict_path}")

    return args


def __execute_args(args: CLArgs) -> str:
    if not args.using_dict:
        return "".join(
            random.choices(
                string.ascii_letters + string.digits + string.punctuation,
                k=CLArgs.PASSWORD_LEN,
            )
        )

    if args.dict_path != "":
        words = utils.get_words_from_file(args.dict_path)
        return utils.generate_password_from_words(words)

    if args.using_dict:
        words = utils.get_words_online()
        return utils.generate_password_from_words(words)

    return "Unexpected error"


def run() -> None:
    try:
        args = __parse_args()
        args = __validate_args(args)
        print(__execute_args(args))
    except OSError | ConnectionError as ex:
        print(str(ex))
    except Exception as ex:
        print("Unexpected exception", ex)
