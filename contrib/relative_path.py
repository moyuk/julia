import sys, os
sys.stdout.write(os.path.relpath(sys.argv[2], sys.argv[1]))

# Always print a trailing slash
if os.path.isdir(sys.argv[2]):
    sys.stdout.write(os.path.sep)