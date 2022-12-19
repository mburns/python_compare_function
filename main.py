#!/bin/env python3

import sys
import json


def usage():
    print("Provide 2 quoted JSON strings as arguments:")
    print("    python3 main.py '{...}' '{...}'")
    exit(1)


def compare(a, b, shallow=False):
    """Compare a and b to find any differences.
    What was added or removed or if the hash is the same.

    `a`       is a dict with string keys
    `b`       is a dict with string keys
    `shallow` is a flag, False implies a deep compare
    """

    # print(f" => {a} versus {b}")

    if type(a) is dict and type(b) is dict:
        # find any keys that are not in both A and B.
        unique_keys = set(a.keys()).symmetric_difference(b.keys())

        if unique_keys:
            removed = set(a.keys()).difference(b.keys()) or None
            for n in removed or []:
                print(f"removed {{ {n}: {a[n]} }}")

            added = set(b.keys()).difference(a.keys()) or None
            for n in added or []:
                print(f"added {{ {n}: {b[n]} }}")

            return False
        else:
            # top-level Keys match 1:1
            if shallow:
                # print("Dicts shallowly match")
                return True

            for key in a:
                return compare(a[key], b[key], False)

            # return True
    else:
        # compare value literals
        if a != b:
            print(f"Values changed: '{a}' -> '{b}'")
        return a == b


if __name__ == "__main__":
    try:
        a = json.loads(sys.argv[1])
        b = json.loads(sys.argv[2])
    except IndexError:
        print("Missing arguments")
        usage()
    except json.decoder.JSONDecodeError:
        print("Failed to decode arguments.")
        usage()

    try:
        shallow = bool(sys.argv[3])
        if shallow:
            print("Performing a shallow search")
    except IndexError:
        shallow = False

    print(compare(a, b, shallow))
