import time
import praw
import random
import re
import urllib3

r = praw.Reddit('TITLE')
r.login("USERNAME","TITLE")
prawWords = ['Thank', 'e', 'i', 'o', 'u']
prawTerms = ['+/u/reddtipbot']
tip_amount_pattern = re.compile("R?(\d+) ?(?:D|Rdd)?", re.IGNORECASE)
amount_min = 0
amount_max = 0
average_tip = float(amount_min + amount_max) / 2
def rand_amount(minimum, maximum):
    return random.randint(minimum, maximum)

def pick_random_comment():
    global amount_min
    global amount_max

    file = open('replylist.txt', 'r')
    already_done = file.read()
    file.close()
    tipblacklist = ['NAME']
    subreddit = r.get_subreddit('reddcoin')
    subreddit_thread = subreddit.get_new(limit=3)
    thread_list = list(subreddit_thread)
    randomcomment = random.choice(thread_list)
    author = randomcomment.author


    if randomcomment.id not in already_done and author.name not in already_done:
            rddtip = str(rand_amount(amount_min, amount_max))
            randomcomment.add_comment('Hi ' + author.name + '\n\n  I am a bot here to tell you the main activity and chat has moved to the official forums [ReddcoinTalk.org](https://www.reddcointalk.org/)' '\n\n  You will have higher visibility and recieve quicker replies there.')
            already_done = already_done+' '+randomcomment.id +' '+ author.name
            file = open('replylist.txt', 'w')
            file.write(already_done)
            file.close()
            print('************' + randomcomment.title + '  - Done ************' )

def check_inbox():
    file = open('idlist.txt', 'r')
    already_done = file.read()
    file.close()
    messages = r.get_unread('comments')
    for message in messages:
        op_text = message.body
        author = message.author
        has_praw = any(string in op_text for string in prawTerms)
        if message.id not in already_done and has_praw:
            amount_matches = tip_amount_pattern.findall(op_text)
            if amount_matches: # found a specified amount in the comment
                tip_allows_hours = float(amount_matches[0]) / average_tip
                tip_allows_hours2 = round(tip_allows_hours, 2)
                message.reply('Thank you! This will help to keep me running for {num_hours} hours!\n\n[Bot Owner](http://www.reddit.com/user/BrownSlaughter/) - [Rdd Companion for Chrome](https://chrome.google.com/webstore/detail/rdd-companion/kloifefdfjjlmbadgkbaphjecijiokja)'.format(num_hours = tip_allows_hours2))
                print('$$ Someone Donated $$   ' )
            else:
                message.reply('Thank you! This will help to keep me running!\n\n[Bot Owner](http://www.reddit.com/user/BrownSlaughter/) - [Rdd Companion for Chrome](https://chrome.google.com/webstore/detail/rdd-companion/kloifefdfjjlmbadgkbaphjecijiokja)')
            already_done = already_done+' '+message.id
            file = open('idlist.txt', 'w')
            file.write(already_done)
            file.close()
            print('$ Someone Donated $' )
            break

while True:
    try:
        print('Redirect Bot checking' )
        pick_random_comment()
        time.sleep(15)
        
    except urllib3.exceptions.HTTPError as e:
        if e.code in [429, 500, 502, 503, 504, 520]:
            print ("**********Reddit is down, sleeping...**********")
            time.sleep(60)
            pass
        else:
            raise
    except Exception as e:
        print ("**********couldn't Reddit**********")
        time.sleep(60)
        pick_random_comment()
        print ("*********RETRYING**********")
        raise

        
