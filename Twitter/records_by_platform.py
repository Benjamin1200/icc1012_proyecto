import time
import sys

if __name__ == '__main__':
    time_start = time.clock()
    # Clean File.
    open("records_by_platform_summary.txt", 'w').close()
    files = ["project_tweets01.data", "project_tweets02.data", "project_tweets03.data", "project_tweets04.data", "project_tweets.data"]
    for _file in files:
        # Write to file in append mode.
        _fo = open("records_by_platform_summary.txt", 'a')
        sys.stdout = _fo
        print _file
        _data = open(_file, 'r')
        lines = _data.readlines()
        records = len(lines)
        print records, '\n'

    time_end = time.clock()

    print "Time taken to completion of the metric: {0} in processor time".format(time_end - time_start)
