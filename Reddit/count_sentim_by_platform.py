import time
import sys

if __name__ == '__main__':
    time_start = time.clock()
    # Clean File.
    open("count_sentim_by_platform_summary.txt", 'w').close()
    files = ["out2.json"]
    for _file in files:
        # parameters for mrjob.
        # To run your job in multiple subprocesses with a few Hadoop features simulated, use -r local.
        option1 = "" #""-r"
        option2 = "" #""local"
        sys.argv = ['count_sentim.py', option1, option2, _file]
        # Write to file in append mode.
        _fo = open("count_sentim_by_platform_summary.txt", 'a')
        sys.stdout = _fo
        print _file
        execfile('count_sentim.py')
        print "\n"

    time_end = time.clock()

    print "Time taken to completion of the metric: {0} in processor time".format(time_end - time_start)
