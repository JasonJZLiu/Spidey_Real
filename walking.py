from spidey_interface import Spidey
import time, pickle


def set_init_pose(spidey_interface):
    infile = open("joint_cmds/init_joint_cmd",'rb')
    cmds = pickle.load(infile)
    infile.close()
    
    for i in range(len(cmds)):
        spidey_interface.apply_command(cmds[i])
        #time.sleep(0.2)


def forward(spidey_interface):
    infile = open("joint_cmds/walking_joint_cmd",'rb')
    cmds = pickle.load(infile)
    infile.close()

    for i in range(len(cmds)):
        spidey_interface.apply_command(cmds[i])
        #time.sleep(0.2)



if __name__ == "__main__":
    spidey_interface = Spidey()
    set_init_pose(spidey_interface)
    input("wait")
    forward(spidey_interface)





