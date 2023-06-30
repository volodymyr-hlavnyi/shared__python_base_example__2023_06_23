import logging

my_dict = {"name": "Luke"}
my_list = ["a", "b"]

try:
    my_dict["nickname"]
except KeyError as exc:
    print(f"{type(exc)}, {exc}")

    logging.warning("this is my_log")
    logging.exception(exc)

try:
    my_list[10]
except IndexError as exc:
    print(f"{type(exc)}, {exc}")
