import time
import sys
import sentiment_analyzer as sa

if __name__ == '__main__':
    time_start = time.clock()
    sid = sa.init_classifier()
    # Clean File.
    open("sentiment_and_language_analysis_by_platform_summary.txt", 'w').close()
    files = ["project_tweets01_language.data", "project_tweets02_language.data", "project_tweets03_language.data", "project_tweets04_language.data"]
    for _file in files:
        _output_filename = sa.classify_file(_file, sid)
        # parameters for mrjob.
        # To run your job in multiple subprocesses with a few Hadoop features simulated, use -r local.
        option1 = "" #""-r"
        option2 = "" #""local"
        sys.argv = ['sentiment_and_language_amount.py', option1, option2, _output_filename]
        # Write to file in append mode.
        _fo = open("sentiment_and_language_analysis_by_platform_summary.txt", 'a')
        sys.stdout = _fo
        print _file
        execfile('sentiment_and_language_amount.py')
        print "\n"
        _fo.close()

    time_end = time.clock()