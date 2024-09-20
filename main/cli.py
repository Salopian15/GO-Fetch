import os
import sys
import argparse
from . import main
from . import utils


def parse_args():
    parser = argparse.ArgumentParser(description="Fetch GO terms for a list of protein IDs")
    parser.add_argument("protein_id_list", help="File containing list of protein IDs")
    parser.add_argument("output_name", help="Output file name")
    parser.add_argument("--checkpoint_file", default="checkpoint.json", help="Checkpoint file name")
    return parser.parse_args()

def run():
    args = parse_args()
    protein_id_list = args.protein_id_list
    output_name = args.output_name

    utils.check_args(protein_id_list, output_name)
    utils.check_internet_connection()

    checkpoint_file = args.checkpoint_file
    checkpoint_data = main.load_checkpoint_data(checkpoint_file)
    protein_ids = main.get_protein_ids(protein_id_list, checkpoint_data)
    main.process_proteins(protein_ids, checkpoint_data, checkpoint_file)
    restructured_data = main.restructure_data(checkpoint_data)
    main.save_restructured_data(restructured_data, output_name)
    os.remove(checkpoint_file)
    print(f"GO terms fetched and saved to {output_name}")   
    
if __name__ == "__main__":
    run()