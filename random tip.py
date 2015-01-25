import time
import praw
import random
import re

r = praw.Reddit('Title')
r.login("USERNAME","PASSWORD")
prawWords = ['Thank', 'e', 'i', 'o', 'u']
prawTerms = ['+/u/reddtipbot']
tip_amount_pattern = re.compile("R?(\d+) ?(?:D|Rdd)?", re.IGNORECASE)
amount_min = 200
amount_max = 750
average_tip = float(amount_min + amount_max) / 2

def rand_amount(minimum, maximum):
    return random.randint(minimum, maximum)

def pick_random_comment():
    global amount_min
    global amount_max

    file = open('idlist.txt', 'r')
    already_done = file.read()
    file.close()
    tipblacklist = ['NAME', 'NAME', 'NAME']
    subreddit = r.get_subreddit('reddcoin')
    subreddit_comments = subreddit.get_comments(limit=50)
    comments_list = list(subreddit_comments)
    randomcomment = random.choice(comments_list)
    author = randomcomment.author
    op_text = randomcomment.body
    has_praw = any(string in op_text for string in prawWords)
    if randomcomment.id not in already_done and author.name not in tipblacklist and has_praw:
            rddtip = str(rand_amount(amount_min, amount_max))
            randomcomment.reply('^This ^is ^a ^random ^Tip ^+/u/reddtipbot ' + rddtip + ' RDD ^Please ^consider ^tipping ^this ^bot ^to ^keep ^it ^Tipping! [^Bot ^Owner](http://www.reddit.com/user/BrownSlaughter/) ^- [^Rdd ^Companion ^for ^Chrome](https://chrome.google.com/webstore/detail/rdd-companion/kloifefdfjjlmbadgkbaphjecijiokja)')
            already_done = already_done+' '+randomcomment.id
            file = open('idlist.txt', 'w')
            file.write(already_done)
            file.close()
            print(randomcomment.id + '  ' + author.name + '  ' + rddtip +' Rdd')
    else:
            print(randomcomment.id + ' ##Failed to meet criteria, Picking again## ')
            pick_random_comment()

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
    print('Bot Started/loop completed' )
    check_inbox()
    pick_random_comment()
    time.sleep(600)
        
