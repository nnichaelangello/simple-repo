import sys
import os
import subprocess

def inred(s):
	return"%s[31;2m%s%s[0m"%(chr(27), s, chr(27))

def ingreen(s):
	return"%s[32;2m%s%s[0m"%(chr(27), s, chr(27))

def system_excu(cmd):
	ret = os.system(cmd)
	if ret != 0:
		print inred(cmd + " " + "failed")
		print os.getcwd()
		#exit()

# iter loop
def next_repo(it):
	try:
		item = it.next()
	except StopIteration:
		return None
	# root dir(zygote)
	if item[0] == '..':
		return '.'
	else:
		return os.path.join(item[0], item[1][:-4])


# repo mngr commands
def repo_status(repo_manifest):
	it = iter(repo_manifest)
	repo_path = next_repo(it)
	while repo_path :
		old_path = os.getcwd();
		os.chdir(repo_path)
		ret_buf = subprocess.check_output("git status -s", shell=True)
		if ret_buf != "":
			print ingreen(repo_path)
			print inred(ret_buf),
		os.chdir(old_path)

		repo_path = next_repo(it)

all_branches = {}

class BranchInfo(object):
	def __init__(self, branch_name):
		self.branch_name = branch_name
		self.repo_list = []

def update_branch_info(branch_name, repo_name):
	if branch_name not in all_branches:
		all_branches[branch_name] = BranchInfo(branch_name)
	all_branches[branch_name].repo_list.append(repo_name)

def pretty_branchinfo_output():
	for item in all_branches:
		print ingreen("branch : %s" % item)
		for repo_item in all_branches[item].repo_list:
			print "            %s" % repo_item
		print

def repo_branch(repo_manifest):
	it = iter(repo_manifest)
	repo_path = next_repo(it)
	while repo_path :
		if os.path.exists(repo_path):
			old_path = os.getcwd();
			os.chdir(repo_path)
			# print ingreen(repo_path)
			#os.system("git branch")
			ret_buf = subprocess.check_output("git branch | grep '*'", shell=True)
			update_branch_info(ret_buf.split(' ')[-1], repo_path.split('/')[-1])
			os.chdir(old_path)

		repo_path = next_repo(it)

	pretty_branchinfo_output()

def repo_init(repo_url, repo_manifest):
	for item in repo_manifest:
		if not os.path.exists(item[0]):
			os.mkdir(item[0])
		if item[0] == '..':
			# skip root dir(zygote)
			continue

		old_path = os.getcwd()
		os.chdir(item[0])
		if not os.path.exists(item[1][:-4]):
			print repo_url + item[1]
			system_excu("git clone " + repo_url + item[1])
		else:
			print inred(item[1] + " already exists, PLS make sure you need re-down it...")
		os.chdir(old_path)

def repo_sync(remote, repo_manifest):
	it = iter(repo_manifest)
	repo_path = next_repo(it)
	while repo_path :
		if os.path.exists(repo_path):
			old_path = os.getcwd()
			os.chdir(repo_path)
			print ingreen(repo_path)
			system_excu("git checkout master");
			system_excu("git fetch " + remote);
			system_excu("git merge " + remote + "/master")
			os.chdir(old_path)

		repo_path = next_repo(it)

def repo_checkout(branch, repo_manifest):
	it = iter(repo_manifest)
	repo_path = next_repo(it)
	while repo_path :
		if os.path.exists(repo_path):
			old_path = os.getcwd()
			os.chdir(repo_path)
			print ingreen(old_path + "/" + repo_path)
			system_excu("git checkout " + branch);
			os.chdir(old_path)

		repo_path = next_repo(it)

def repo_forall(command, repo_manifest):
	it = iter(repo_manifest)
	repo_path = next_repo(it)
	while repo_path :
		if os.path.exists(repo_path):
			old_path = os.getcwd()
			os.chdir(repo_path)
			print ingreen(repo_path)
			system_excu(command);
			os.chdir(old_path)
		else:
			print repo_path + " not exist"

		repo_path = next_repo(it)

def repo_remote(remote_name, remote_addr, repo_manifest):
	it = iter(repo_manifest)
	repo_path = next_repo(it)
	while repo_path :
		if os.path.exists(repo_path):
			old_path = os.getcwd()
			os.chdir(repo_path)
			print ingreen(repo_path)
			remote_path = os.path.join(remote_addr, item[1])
			command = "git remote add " + remote_name + " " + remote_path
			print command;
			system_excu(command);
			os.chdir(old_path)

		repo_path = next_repo(it)

def repo_push(remote, repo_manifest):
	it = iter(repo_manifest)
	repo_path = next_repo(it)
	while repo_path :
		if os.path.exists(repo_path):
			old_path = os.getcwd();
			os.chdir(repo_path)
			print ingreen(repo_path)
			system_excu("git push " + remote + " master:master")
			os.chdir(old_path)

		repo_path = next_repo(it)
