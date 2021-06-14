import pickle
infile = open("joint_cmds/walking_joint_cmd",'rb')
cmds = pickle.load(infile)
infile.close()

print(cmds)