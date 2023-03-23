import os
import numpy as np
import sys

def move_testing(foldername, entry, trainfolder, testfolder):
    cur = foldername + "/" + entry
    images = os.listdir(cur)
    np.random.shuffle(images)

    # Move first 15% to testing
    testDest = testFolder + "/" + entry
    trainDest = trainFolder + "/" + entry

    if not os.path.exists(testDest):
            os.makedirs(testDest)

    if not os.path.exists(trainDest):
            os.makedirs(trainDest)


    for i in range(int(len(images) * 0.15)):
        os.rename(cur + "/" + images[i], testDest + "/" + images[i])

    # Rest to training
    for i in range(int(len(images) * 0.15), len(images)):
        os.rename(cur + "/" + images[i], trainDest + "/" + images[i])

        


if __name__ == "__main__":
    foldername = sys.argv[1]

    # Create subfolders
    trainFolder = foldername + "/TrainImages"
    testFolder = foldername + "/TestImages"

    if not os.path.exists(trainFolder):
            os.makedirs(trainFolder)

    if not os.path.exists(testFolder):
        os.makedirs(testFolder)

    # For each pokemon, partition and move
    with os.scandir(foldername) as entries:
        
        for entry in entries:
            if entry.name != 'TestImages' and entry.name != 'TrainImages':
                move_testing(foldername, entry.name, trainFolder, testFolder)
                # Delete old folder after all moved
                os.rmdir(foldername + "/" + entry.name)