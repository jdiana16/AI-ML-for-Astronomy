#!/usr/bin/env python3

import os
import glob
import argparse
from astropy.io import fits
import pandas as pd
from typing import List, Dict, Optional

def find_fits_files(directory: str) -> List[str]:
    """
    Find all FITS files in the given directory.
    
    Args:
        directory (str): Path to the directory to search
    
    Returns:
        List[str]: List of paths to FITS files
    """
    # Get absolute path and search for .fits files
    search_path = os.path.join(os.path.abspath(directory), "*.fits")
    return glob.glob(search_path)

def extract_header_info(fits_file: str) -> Optional[Dict]:
    """
    Extract metadata from a FITS file.
    
    Args:
        fits_file (str): Path to the FITS file
    
    Returns:
        Optional[Dict]: Dictionary containing metadata or None if extraction fails
    """
    try:
        with fits.open(fits_file) as hdul:
            header = hdul[0].header
            
            # Extract required information with default values if keywords missing
            metadata = {
                'Filename': os.path.basename(fits_file),
                'RA': header.get('RA', 'N/A'),
                'Dec': header.get('DEC', 'N/A'),
                'Exposure_Time': header.get('EXPTIME', 'N/A'),
                'Observation_Date': header.get('DATE-OBS', 'N/A')
            }
            return metadata
    except Exception as e:
        print(f"Error processing {fits_file}: {str(e)}")
        return None

def create_csv(metadata_list: List[Dict], output_file: str = 'fits_metadata_summary.csv'):
    """
    Create a CSV file from the metadata.
    
    Args:
        metadata_list (List[Dict]): List of metadata dictionaries
        output_file (str): Name of the output CSV file
    """
    if not metadata_list:
        print("No valid metadata to write to CSV")
        return
    
    df = pd.DataFrame(metadata_list)
    df.to_csv(output_file, index=False)
    print(f"Metadata saved to {output_file}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Extract metadata from FITS files')
    parser.add_argument('directory', help='Directory containing FITS files')
    parser.add_argument('--output', '-o', default='fits_metadata_summary.csv',
                       help='Output CSV file name (default: fits_metadata_summary.csv)')
    
    args = parser.parse_args()
    
    # Find all FITS files
    fits_files = find_fits_files(args.directory)
    if not fits_files:
        print(f"No FITS files found in {args.directory}")
        return
    
    print(f"Found {len(fits_files)} FITS files")
    
    # Extract metadata from each file
    metadata_list = []
    for fits_file in fits_files:
        metadata = extract_header_info(fits_file)
        if metadata:
            metadata_list.append(metadata)
    
    # Create CSV file
    create_csv(metadata_list, args.output)

if __name__ == '__main__':
    main()
