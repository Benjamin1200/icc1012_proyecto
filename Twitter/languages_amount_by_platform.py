import time
import sys
import language_detect as ld

# The summary is for each hour per week. (i.e. 20 spanish tweets on week 1, 31 english tweets on week 2, ...)

# Important Note: This is just an estimation of the language based on the stopwords, so if no stopwords are found the language
#                   that will produce is garbage, but is not the fault of the model. Also if there are some stopwords of both
#                   languages it will say is the one with most stopwords.

if __name__ == '__main__':
    time_start = time.clock()
    # Clean File.
    open("languages_amount_by_platform_summary.txt", 'w').close()
    files = ["project_tweets03.data", "project_tweets04.data"]
    for _file in files:
        _output_filename = ld.set_language_for_each_tweet(_file)
        # parameters for mrjob.
        # To run your job in multiple subprocesses with a few Hadoop features simulated, use -r local.
        option1 = "" #""-r"
        option2 = "" #""local"
        sys.argv = ['count_language.py', option1, option2, _output_filename]
        # Write to file in append mode.
        _fo = open("languages_amount_by_platform_summary.txt", 'a')
        sys.stdout = _fo
        print _file
        execfile('count_language.py')
        print "\n"

    time_end = time.clock()
    print "Time taken to completion of the metric: {0} in processor time".format(time_end - time_start)
