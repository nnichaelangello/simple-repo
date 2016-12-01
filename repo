#!/usr/bin/python
import os
import time
import shutil
import stat
import sys
import re
import subprocess
import repo_utils

repo_manifest = [
					['.', 'repo_test1.git'],
					['.', 'repo_test2.git'],
				]

repo_url_dic = {
	'test' : "git@github.com:imagec/"
}

command_dic = {
	"status"     : repo_utils.repo_status,
	"branch"     : repo_utils.repo_branch,
	"init"       : repo_utils.repo_init,
	"push"       : repo_utils.repo_push,
	"sync"       : repo_utils.repo_sync,
	"checkout"   : repo_utils.repo_checkout,
	"forall"     : repo_utils.repo_forall,
	"remote"     : repo_utils.repo_remote
}

try:
	command_handler = command_dic[sys.argv[1]]
except KeyError:
	print repo_utils.inred("wrong command :" + sys.argv[1])
	exit()

if (sys.argv[1] == 'status' or sys.argv[1] == 'branch'):
	command_handler(repo_manifest)
elif (sys.argv[1] == 'push'):
	command_handler(sys.argv[2], repo_manifest)
elif (sys.argv[1] == 'init'):
	command_handler(repo_url_dic[sys.argv[2]], repo_manifest)
elif (sys.argv[1] == 'sync'):
	command_handler(sys.argv[2], repo_manifest)
elif (sys.argv[1] == 'checkout'):
	command_handler(sys.argv[2], repo_manifest)
elif (sys.argv[1] == 'forall'):
	command_handler(sys.argv[2], repo_manifest)
elif (sys.argv[1] == 'remote'):
	command_handler(sys.argv[2], sys.argv[3], repo_manifest)
else:
	print "Command not supported"
