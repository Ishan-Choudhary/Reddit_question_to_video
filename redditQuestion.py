import praw
from configparser import ConfigParser

#CREATING THE CONFIG FILE
config = ConfigParser()
config.read('config.ini')

#CREATING REDDIT INSTANCE
reddit = praw.Reddit(
    client_id=config["questionBot"]["client_id"],
    client_secret=config["questionBot"]["client_secret"],
    password=config["questionBot"]["password"],
    user_agent=config["questionBot"]["user_agent"],
    username=config["questionBot"]["username"],
)

def get_latest_question() -> dict:  
    '''
    Function that goes to the subreddit AskReddit, and returns the latest function
    '''
    #QUESTION DETAILS
    question = ""
    questionAuthor = ""

    #GETTING TOP POST AND REQUIRED INFO FROM IT
    for submissions in reddit.subreddit('AskReddit').new(limit=10):
        if(submissions.over_18 == False):
            questionAuthor = str(submissions.author)

            if(bool(str(submissions.title)) == False): question = submissions.selftext
            else: question = submissions.title

            #DIVIDING THE STRING
            part1 = ""
            part2 = ""

            for i, each in enumerate(question.split()):
                if(len(question.split())  > 7):
                    if i <= 7:  part1 += each + ' '
                    else: part2 += each + ' '
                else: part1 += each + ' '

            with open('question.txt', 'w') as f:
                f.write(part1)
                f.write('\n')
                f.write(part2)
                f.write('\n')
                f.write('-u/' + questionAuthor)
                f.write('\n')
                f.write('Comment down below')
            
            break
            
        else: pass
    
    #RETURNING
    return {"question": question, "author": questionAuthor}
#TODO: FIX BUG OF EMPTY VIDEO