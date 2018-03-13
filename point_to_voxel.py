#######################################################################
# This script converts a wavefront object into a series of JSON       #
# "gradients" (shapes) used by the Live Parts application.            #
# Specifically, this script should be used to import generatively     #
# designed models from Live Parts, and these parts will need to be    #
# first converted from .stl to .obj using Blender.                    #
# Care must be taken with the .obj file, it should only contain       #
# vertex data. (any line that starts with "v")                        #
# This script only produces gradients a.k.a. shapes in JSON, the JSON #
# must then be carefully inserted into the JSON file read by          #
# Live Parts.                                                         #
#######################################################################

#the name of the file to be converted.
terminalIn = ""

#controls weather the output cubes are generated as attractors or repellers. These entities attract or repell seed cells in the Live Parts application.
repellerOrAttractor = ""

#a scaler for each voxel that's created. Changing this value will make each cube have a uniform length, width, and height.
dimensions = ""

#For the user's convenience, the .obj extension is added to input file name.
terminalIn = raw_input("Enter a .obj filename w/o the extension:")
terminalInWithExtension = terminalIn + ".obj"


repellerOrAttractor = raw_input("Enter a cube boundary type (attractor/repeller)[a/r]: ")
dimensions = raw_input("Enter cube width [1/2/3/4/5]:")

#shorthand console input, this saves the user from entering the entire phrase of "attractor" or "repeller"
if(repellerOrAttractor == "a"):
    repellerOrAttractor = "attractor"
else:
    repellerOrAttractor = "repeller"

#reads all lines from the specified file.
lines = [line.rstrip('\n') for line in open(terminalInWithExtension)]

#voxel stack that will hold all the JSON voxel "gradients"
voxels = []

#traverses each line in the file and extracts point data.
#the point data is wrapped into the proper gradient JSON.
for i in range(len(lines)):
    x = 0
    y = 0
    z = 0
    line = []
    line = lines[i].split()
    x = line[1]
    y = line[2]
    z = line[3]
    voxels.append("{\"id\":" + str(i) + ",\"type\":\"" + repellerOrAttractor + "\",\"shape\":\"rightprism\",\"length\":" + dimensions + ",\"width\":" + dimensions + ",\"height\":" + dimensions + ",\"pos\":[" + str(z) + "," + str(x) + "," + str(y) + "]}");

#writes all of the gradient voxels to a JSON file.
fout = open(terminalIn + '.json', 'w')
for i in range(len(voxels)):
    fout.write(voxels[i] + ",\n")
fout.close()