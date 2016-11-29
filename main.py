import sys
import argparse
from pprint import pprint
from workflow import loadConfig
from os import path

UNDERLINE = ('\n' + '-'*100)

def main(config):
    """
    This is the main runner
    :return:
    """
    # pprint(config)
    for step in config['Steps']:
        print "\n\n"
        print "Doing '{1}' step: {0}".format(step['attr']['name'], step['attr']['type']) + UNDERLINE
        if 'Cmd' in step:
            print "  Executing: {0} with arguments:".format(step['Cmd']['Value'])
        if 'Cwd' in step:
            print "    in folder: {0}".format(step['Cwd']['Value'])
        if 'Module' in step:
            print "    in python Module: {0}".format(step['Module']['Value'])
        if 'items' in step['Args']:
            print "    with arguments:"
            for arg in step['Args']['items']:
                print '      {0} --> {1}'.format(arg['attr']['id'], arg['attr']['type'])






"""
This function handles the argument parsing and calls our main function
"""
if __name__ == '__main__':
    #parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument('input_xml',
                        help='Path to the input GCD (xml) file.',
                        type=argparse.FileType('r'))
    parser.add_argument('--workflow', type=argparse.FileType('r'), default=path.join('xml', 'SAMPLEWorkflow.xml'),
                        help='Path to the workflow GCD file (optional)')
    args = parser.parse_args()
    print args
    try:
        # Load the XML into a simple dictionary
        config = loadConfig(args.workflow)
        # Now kick things off
        main(config)
    except:
        print 'Unxexpected error: {0}'.format(sys.exc_info()[0])
        raise
        sys.exit(0)
