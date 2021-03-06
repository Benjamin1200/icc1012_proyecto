import time
import sys

if __name__ == '__main__':
    time_start = time.clock()
    # Clean File.
    open("top_users_by_platform_summary.txt", 'w').close()
    files = ["project_tweets01.data", "project_tweets02.data", "project_tweets03.data", "project_tweets04.data"]
    for _file in files:
        # parameters for mrjob.
        # To run your job in multiple subprocesses with a few Hadoop features simulated, use -r local.
        option1 = "" #""-r"
        option2 = "" #""local"
        sys.argv = ['top_users.py', option1, option2, _file]
        # Write to file in append mode.
        _fo = open("top_users_by_platform_summary.txt", 'a')
        sys.stdout = _fo
        print _file
        execfile('top_users.py')
        print "\n"

    time_end = time.clock()

    print "Time taken to completion of the metric: {0} in processor time".format(time_end - time_start)
