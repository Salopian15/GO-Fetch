import requests
import sys
import time
import json
from tqdm import tqdm


def fetch_go_terms(protein_id):
    try:
        url = f"https://www.ebi.ac.uk/proteins/api/proteins/{protein_id}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            go_terms = [x['id'] for x in data.get('dbReferences', []) if x['type'] == 'GO']
            return go_terms
        else:
            return []
    except requests.ConnectionError:
        print("Error: No internet connection.")
        sys.exit(1)

def load_checkpoint_data(checkpoint_file):
    try:
        with open(checkpoint_file, 'r') as checkpoint:
            checkpoint_data = json.load(checkpoint)
    except FileNotFoundError:
        checkpoint_data = {}
    return checkpoint_data

def get_protein_ids(protein_id_list, checkpoint_data):
    protein_ids = []
    with open(protein_id_list, 'r') as file:
        lines = file.readlines()
        for line in lines:
            protein_id = line.strip()
            if protein_id not in checkpoint_data:
                protein_ids.append(protein_id)
    return protein_ids

def process_proteins(protein_ids, checkpoint_data, checkpoint_file):
    total_proteins = len(protein_ids)
    with tqdm(total=total_proteins, desc="Processing proteins") as pbar:
        for protein_id in protein_ids:
            go_terms = fetch_go_terms(protein_id)
            checkpoint_data[protein_id] = go_terms
            
            # Save checkpoint data after processing each protein
            with open(checkpoint_file, 'w') as checkpoint:
                json.dump(checkpoint_data, checkpoint)
            
            pbar.update(1)

def restructure_data(checkpoint_data):
    restructured_data = []
    for protein_id, go_terms in checkpoint_data.items():
        for term in go_terms:
            restructured_data.append((protein_id, term))
    return restructured_data

def save_restructured_data(restructured_data, output_name):
    with open(output_name, 'w') as file:
        for protein_id, go_term in restructured_data:
            file.write(f"{protein_id}\t{go_term}\n")

