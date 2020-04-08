import sys, os
if len(sys.argv) != 3:
    sys.stderr.write("\nrelative_path.py - incomplete arguments: %s\n"%(sys.argv))
    sys.exit(1)

sys.stdout.write(os.path.relpath(sys.argv[2], sys.argv[1]))

# Always print a trailing slash
if os.path.isdir(sys.argv[2]):
    sys.stdout.write(os.path.sep)