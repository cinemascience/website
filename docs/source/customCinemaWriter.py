#! /usr/bin/env python
# Psuedo code to generate a custom Cinema Database

import sys, os
import pandas as pd

###############################################
# writes the data frame to the CDB data.csv file
################################################
def write_data(fname, df):
    sys.stderr.write ("Writing Cinema database data.csv...\n")

    with open(fname, "w") as output:
                df.to_csv(fname, mode='w', sep=',' , index=False)
################################################

# get database parameters from sys.argv
runParams = [180101, 00]   # Default run params
if len(sys.argv) == 3:
    runParams[0] = int( float(sys.argv[1]) )
    runParams[1] = int( float(sys.argv[2]) )
else:
    sys.stderr.write ( ("Warning, no run information, using defaults: {};{}\n").format(runParams[0],runParams[1]) )

# Setup CDB directory structure and default image for file
sys.stderr.write ( 'Run Params: {}_{}\n'.format(runParams[0],runParams[1]))
sys.stderr.write ( 'Creating Cinema Database directory structure ...\n' )
inputDir = 'input/'
dataDir  = 'data/run_{}_{}.cdb'.format(runParams[0],runParams[1] )
imageDir = dataDir+'/image'
defaultFILEimg = 'cinemaNoFILE.png'

# check for dataDir; copy default File img to image directory
os.makedirs(dataDir, exist_ok=True)
os.system('/bin/cp ' + defaultFILEimg +' '+ imageDir+'/.')

# Read in the already-existing dataset
sys.stderr.write ("Reading in datafile file...\n")
inputFile = inputDir + 'run_{}_{}.csv'.format(runParams[0],runParams[1] )
dfRun = pd.read_csv(inputFile, sep=',')

#  manipulate the dfRun dataframe:
sys.stderr.write ("Analysis and Image File Code Block...\n")
dfRun['newVar'] = dfRun['var1']/dfRun['var2']    # perform some analysis
if 'uselessProperty' in dfRun.columns:           # delete a column
    dfRun = dfRun.drop(['uselessProperty'], axis =1)
# ...etc...
dfRun['FILE'] = defaultFILEimg                   # add the final FILE column for images
for index, row in dfRun.iterrows():              # select an image to show for that row
    thisValue = row['newVar']
    thisImage = inputDir + 'run_{}_{}_{}.png'.format(thisValue, runParams[0],runParams[1])
    if os.path.isfile(thisImage):                # check if it exists and if so
         row['FILE'] = imageDir + thisImage      # set the FILE variable to that image & move it to the image directory
         os.system('/bin/mv ' + inputDir+thisImage +' '+ imageDir+'/.')

# Write out the dataframe to a Cinema database data.csv
datafilename = dataDir+'/data.csv'
write_data( datafilename, dfRun)
