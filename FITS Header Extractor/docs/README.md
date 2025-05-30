# FITS Metadata Extractor

A Python script that extracts metadata from FITS (Flexible Image Transport System) files and compiles it into a CSV file for easy analysis.

## Features

- Recursively finds all FITS files in a specified directory
- Extracts key metadata:
  - Right Ascension (RA)
  - Declination (Dec)
  - Exposure Time
  - Observation Date
- Compiles metadata into a well-structured CSV file
- Handles errors gracefully (invalid files, missing headers, permission issues)
- Command-line interface for easy usage

## Requirements

- Python 3.6+
- Required Python packages:
  - astropy (for FITS file handling)
  - pandas (for CSV creation)

## Installation

1. Clone or download this repository
2. Install the required packages:
```bash
pip install astropy pandas
```

## Usage

### Basic Usage

```bash
python fits_metadata_extractor.py /path/to/fits/files
```

This will:
1. Search for all `.fits` files in the specified directory
2. Extract metadata from each file
3. Create a file named `fits_metadata_summary.csv` in the current directory

### Specifying Output File

```bash
python fits_metadata_extractor.py /path/to/fits/files -o custom_output.csv
```

### Command-line Arguments

- `directory` (required): Path to the directory containing FITS files
- `--output`, `-o` (optional): Name of the output CSV file (default: fits_metadata_summary.csv)

## Output Format

The script generates a CSV file with the following columns:

| Column | Description |
|--------|-------------|
| Filename | Name of the FITS file |
| RA | Right Ascension |
| Dec | Declination |
| Exposure_Time | Exposure time of the observation |
| Observation_Date | Date when the observation was taken |

## Error Handling

The script handles various error conditions:
- Invalid FITS files are skipped with an error message
- Missing header keywords are replaced with 'N/A'
- File access permission issues are reported

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
