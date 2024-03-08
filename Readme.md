# VTK Mid-sagittal area estimation 
This script reads in .vtk files drawn on the YZ plane and then calculates their area using the shoelace formula. Further
reading on the shoelace formula can be found at https://en.wikipedia.org/wiki/Shoelace_formula. This code assumes that 
the vtk files are a polyline object only on one plane. It should be easy to change this plane by changing which values
are passed into the area calculation function.

## Prerequisites
- Python (>=3.6)
- VTK library
- NumPy
- Pandas
- natsort

### Install the required libraries using:

```bash
pip install -r requirements.txt
```

## Usage
1. Point inDirectory to the folder containing the .vtk files of which you want the area calculated
2. Run the script: 
```bash
python shoelaceArea.py 
```
3. The calculated areas will be saved to an Excel file named 'traceArea.xlsx' in the same directory as the VTK files.

## Output
The calculated areas are stored in a Pandas DataFrame with two columns: "VTK Filename" and "Calculated Area." The 
DataFrame is then saved to an Excel file for further analysis or reporting.

Feel free to adapt and integrate this script into your workflow for VTK file processing and area calculations.
