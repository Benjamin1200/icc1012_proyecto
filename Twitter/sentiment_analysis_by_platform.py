import time
import sys
import sentiment_analyzer as sa

# The summary is for each hour per week. (i.e. 20 positives tweets on week 1, 31 negative tweets on week 2, ...)

if __name__ == '__main__':
    time_start = time.clock()
    sid = sa.init_classifier()
    # Clean File.
    open("sentiment_analysis_by_platform_summary.txt", 'w').close()
    files = ["project_tweets01.data", "project_tweets02.data", "project_tweets03.data", "project_tweets04.data"]
    for _file in files:
        _output_filename = sa.classify_file(_file, sid)
        # parameters for mrjob.
        # To run your job in multiple subprocesses with a few Hadoop features simulated, use -r local.
        option1 = "" #""-r"
        option2 = "" #""local"
        sys.argv = ['sentiment_amount.py', option1, option2, _output_filename]
        # Write to file in append mode.
        _fo = open("sentiment_analysis_by_platform_summary.txt", 'a')
        sys.stdout = _fo
        print _file
        execfile('sentiment_amount.py')
        print "\n"

    time_end = time.clock()

    print "Time taken to completion of the metric: {0} in processor time".format(time_end - time_start)
