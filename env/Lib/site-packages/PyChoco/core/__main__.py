from configparser import ConfigParser
from importlib import resources
import sys

from core import model

def main():
    # Read URL of the Real Python feed from config file
    cfg = ConfigParser()
    cfg.read_string(resources.read_text("core", "config.txt"))
    url = cfg.get("feed", "url")

    # test
    print("ressources red.")


if __name__ == "__main__":
    main()
