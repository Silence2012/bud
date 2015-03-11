import sys
if sys.version_info[0] == 3:
    requirements_file = './requirements3.txt'
else:
    requirements_file = './requirements.txt'

exec(open('agent/version.py').read())

with open(requirements_file) as requirements_txt:
    requirements = [line for line in requirements_txt]
    print requirements
print "="*80
print version
print sys.version_info
