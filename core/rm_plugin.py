'''rm:
remove one or more files/directories
usage: 
    shellista-core rm

positional arguments:
  path             Path or paths of files/dirs to delete.

optional arguments:
  -h, --help       show this help message and exit
  -r, --recursive  Recursively delete directories.
  -f, --force      Ignore delete confirmation.
  -v, --verbose    View console output.
'''
#from .. tools.toolbox import bash,pprint
import os
import argparse



alias = ['remove']

def main(self, line):
    """remove one or more files/directories"""
    parser = argparse.ArgumentParser(description='shellista-core rm')
    parser.add_argument('-r', '--recursive', 
                        action="store_true", 
                        default=False,
                        help='Recursively delete directories.')
    parser.add_argument('-f', '--force', 
                        action="store_true", 
                        default=False,
                        help='Ignore delete confirmation.')
    parser.add_argument('-v', '--verbose', 
                        action="store_true", 
                        default=False,
                        help='View console output.')
    parser.add_argument('path', action="store", nargs='*',help='Path or paths of files/dirs to delete.')
    
    args = parser.parse_args(line.split(' '))

    #exit if no path arguments are found
    if not args.path:
        print 'rm: please use help rm'
        return
        
    #setup print function
    def printp(text):
        pass
        
    if args.verbose:
        def printp(text):
            print text
    else:
        def printp(text):
            pass
            
    if not args.force:
        def prompt(file):
            result = raw_input('Delete %s? [Y,n]: '%file)
            if result == 'Y' or result == 'y':
                return True
            else:
                return False
    else:
        def prompt(file):
            return True
        
    for path in args.path:
        path = os.path.expanduser(path)
        if os.path.isfile(path):
            if prompt(path):
                printp('%s has been deleted'%path)
                print 'fake delete'
                os.remove(path)
        elif os.path.isdir(path) and args.recursive:
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    if prompt(os.path.join(root,name)):
                        printp('%s file has been deleted.'% name)
                        print 'fake file delete'
                        os.remove(os.path.join(root, name))
                for name in dirs:
                    if prompt(os.path.join(root,name)):
                        printp('%s directory has been deleted.' % name)
                        print 'fake dir delete'
                        os.rmdir(os.path.join(root, name))
        elif os.path.isdir(path):
            print 'rm: cannot remove directories. View help rm'
        else:
            print '%s does not exist.'% path
            
            
