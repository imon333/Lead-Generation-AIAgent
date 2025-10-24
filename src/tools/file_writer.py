import pandas as pd

from datetime import datetime
import os

OUTPUT_DIR = "outputs"

def save_leads_to_excel(leads: list[dict]):
    """
    Saves a list of lead dictionaries to an excel file.
    the filename will be timestamped.
    """
    
    if not leads:
        return "No leads to save."
    
    # Ensure the output directory exists

    os.makedirs(OUTPUT_DIR, exist_ok = True)
    
    # Get current time for the filename
    now = datetime.now()