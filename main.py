__author__ = 'cafacan'

import time
import config
from bin.tailor import Tailor


def main():
    log_tailor = Tailor()
    log_tailor.run()

    while True:
        config.defaults["exit"]
        time.sleep(2)


if __name__ == "__main__":
    main()