"""
Created on Fri Nov 27 16:00:47 2020

@author: hien
"""
import argparse
from interactive import interactive

def get_args():
    parser = argparse.ArgumentParser(
        """Implementation of Deep Q Network to play Procon""")
    parser.add_argument("--file_name", default = "input.txt")
    parser.add_argument("--type", default = "1")
    args, unknown = parser.parse_known_args()
    return args

if __name__ == "__main__":
    interactive(get_args())
    
