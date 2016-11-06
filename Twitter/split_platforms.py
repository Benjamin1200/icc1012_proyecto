import time
import json

if __name__ == '__main__':
    time_start = time.clock()
    nintendo_platform_file = []
    playstation_platform_file = []
    xbox_platform_file = []
    else_platform_file = []
    _file = open("project_tweets.data", 'r')
    for line in _file.readlines():
        data = json.loads(line)
        try:
            raw_text = data['text'].strip().upper()
            raw_username = data['user']['screen_name'].strip().upper()
        except:
            # No idea why would happen.
            print "WTF!"
            raw_text = ""
            raw_username = ""
        #tokens = nltk.word_tokenize(raw)
        nintendo_mentions = raw_text.count("NINTENDO")
        playstation_mentions = raw_text.count("PLAYSTATION")
        xbox_mentions = raw_text.count("XBOX")
        nintendo_mentions += 1 if raw_username.find("NINTENDO") != -1 else 0
        playstation_mentions += 1 if raw_username.find("PLAYSTATION") != -1 else 0
        xbox_mentions += 1 if raw_username.find("XBOX") != -1 else 0
    #    print nintendo_mentions, playstation_mentions, xbox_mentions
        if nintendo_mentions > playstation_mentions and nintendo_mentions > xbox_mentions:
            nintendo_platform_file.append(line)
        elif playstation_mentions > nintendo_mentions and playstation_mentions > xbox_mentions:
            playstation_platform_file.append(line)
        elif xbox_mentions > playstation_mentions and xbox_mentions > nintendo_mentions:
            xbox_platform_file.append(line)
        elif nintendo_mentions == playstation_mentions and nintendo_mentions == xbox_mentions and nintendo_mentions > 0:
            nintendo_platform_file.append(line)
            playstation_platform_file.append(line)
            xbox_platform_file.append(line)
        elif nintendo_mentions == playstation_mentions and nintendo_mentions != xbox_mentions:
            nintendo_platform_file.append(line)
            playstation_platform_file.append(line)
        elif nintendo_mentions == xbox_mentions and nintendo_mentions != playstation_mentions:
            nintendo_platform_file.append(line)
            xbox_platform_file.append(line)
        elif playstation_mentions == xbox_mentions and playstation_mentions != nintendo_mentions:
            playstation_platform_file.append(line)
            xbox_platform_file.append(line)
        else:
            else_platform_file.append(line)
    filenames = ["project_tweets01.data", "project_tweets02.data", "project_tweets03.data", "project_tweets04.data"]
    for filename in filenames:
        # Clean files.
        open(filename, 'w').close()
        # Write files in append mode.
        with open(filename, 'a') as _file:
            if filename == "project_tweets01.data":
                for line in nintendo_platform_file:
                    _file.write(line)
            elif filename == "project_tweets02.data":
                for line in playstation_platform_file:
                    _file.write(line)
            elif filename == "project_tweets03.data":
                for line in xbox_platform_file:
                    _file.write(line)
            else:
                for line in else_platform_file:
                    _file.write(line)
    time_end = time.clock()

    print "Time taken to completion of the metric: {0} in processor time".format(time_end - time_start)
