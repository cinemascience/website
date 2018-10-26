import vtk
import numpy as np
import sys
import argparse
import os

################################
# Function to read in data
################################
def read_vtm_data(in_file):
    reader = vtk.vtkXMLMultiBlockDataReader()
    reader.SetFileName(in_file)
    reader.Update()
    return reader.GetOutput().GetBlock(0)

################################
# Function to analyze, manipulate data
# and write out blocks of data
################################
def sample_random(mpData, outfile, x):

    numPieces = mpData.GetNumberOfPieces()
    print("pieces:", numPieces)

    multiblock = vtk.vtkMultiBlockDataSet()
    multiblock.SetNumberOfBlocks(numPieces)
# ...do the random sampling
    w = vtk.vtkXMLMultiBlockDataWriter()
    w.SetInputData(multiblock)
    filename = outfile
    w.SetFileName(filename)
    w.Write()

################################

parser = argparse.ArgumentParser()

if len(sys.argv) != 4:
    parser.error("incorrect number of arguments")

parser.add_argument('--input', action="store", required="true")
parser.add_argument('--output', action="store", required="true")
parser.add_argument('--percentage', action="store", required="true")

args = parser.parse_args()

inputstring = getattr(args, 'input')
outPath = getattr(args, 'output')
sample_fraction = float(getattr(args, 'percentage'))

# change the delimeter here; currently assumes spaces
in_file_name = inputstring.split(' ')

for i in range(len(in_file_name)):
    if(outPath[len(outPath)-1]=='/'):
        out_file_name = outPath + os.path.basename(in_file_name[i])
    else:
        out_file_name = outPath + '/' + os.path.basename(in_file_name[i])

    ## read in the data file
    mpData = read_vtm_data(in_file_name[i])

    ## call the sample data function here
    sample_random(mpData,out_file_name,sample_fraction)
