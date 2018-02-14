import ap
import subprocess

# P: cmd, args 
# -> R 

def exec(command, args):
	print('command=',command,'args=', args)
	return subprocess.check_output(command+" "+args, shell=True)
	
#print('DEBUG exec', ap.tvm_get(ap.args["cmd"]), ap.args["R"] ) #

ap.tvm_set(ap.args["R"], exec(ap.args["cmd"], ap.args['args']))
