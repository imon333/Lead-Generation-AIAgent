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
    filename = f"leads_{now.strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # Convert list of dictionaries to a pandas DataFrame
    try:
        df = pd.DataFrame(leads)

        # Save the DataFrame to an Excel file
        df.to_excel(filepath, index=False)

        return f"Successfully saved {len(leads)} leads to {filepath}"
    except Exception as e:
        return f"Error saving file: {e}"