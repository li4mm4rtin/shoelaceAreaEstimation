import vtk
import numpy as np
from vtk.util.numpy_support import vtk_to_numpy
import pandas as pd
import os
import natsort


def shoelaceFormula(vertices):
    """
    Implementation of the shoelace formulation to calculate the area of an irregular polygon. More information can be
    found here: https://en.wikipedia.org/wiki/Shoelace_formula
    :param array vertices: 2D array of points, which are used to calculate the area
    :return: float: area
    """
    # Initialize the area
    area = 0

    # Apply the shoelace formula
    for i in range(len(vertices)-1):
        area += (vertices[i][0] * vertices[i + 1][1]) - (vertices[i + 1][0] * vertices[i][1])

    # Add the last term to complete the formula
    area += (vertices[len(vertices) - 1][0] * vertices[0][1]) - (vertices[0][0] * vertices[len(vertices) - 1][1])

    # Take the absolute value and divide by 2
    area = abs(area) / 2

    return area


def VTK2Area(vtk_file_path):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(vtk_file_path)
    reader.Update()

    data = vtk_to_numpy(reader.GetOutput().GetPoints().GetData())

    # Calculate area using the shoelace formula
    return shoelaceFormula(data[:, 1:])


inDirectory = './testFiles/'
filenames = natsort.natsorted(os.listdir(inDirectory))
filenames = [filename for filename in filenames if filename.lower().endswith(".vtk")]

areas = np.empty(len(filenames))

for i, filename in enumerate(filenames):
    areas[i] = VTK2Area(os.path.join(inDirectory, filename))

dataFrame = pd.DataFrame({
    "VTK Filename": filenames,
    "Calculated Area:": areas
})

excel_filename = os.path.join(inDirectory, 'traceArea.xlsx')
dataFrame.to_excel(excel_filename, index=False)

