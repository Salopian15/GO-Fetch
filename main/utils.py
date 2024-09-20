import os
import sys
import time
import json
import requests
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Fetch GO terms for a list of protein IDs")
    parser.add_argument("protein_id_list", help="File containing list of protein IDs")
    parser.add_argument("output_name", help="Output file name")
    return parser.parse_args()


def check_args(inf, outf):
    if len(sys.argv) != 3:
        print("Usage: python main.py <protein_id_list> <output_name>")
        sys.exit(1)
    if not os.path.isfile(inf):
        print("Error: Protein ID list file not found.")
        sys.exit(1)
    if os.path.isfile(outf):
        print("Error: Output file already exists.")
        sys.exit(1)
    if os.stat(inf).st_size == 0:
        print("Error: Protein ID list file is empty.")
        sys.exit(1)

def check_internet_connection():
    try:
        requests.get("https://www.ebi.ac.uk/proteins/api/proteins/")
    except requests.ConnectionError:
        print("Error: No internet connection.")
        sys.exit(1)
    
    