import time
import praw
import random
import re

r = praw.Reddit('Title')
r.login("USERNAME","Password")
prawWords = ['Thank', 'e', 'i', 'o', 'u']
prawTerms = ['+/u/reddtipbot']
tip_amount_pattern = re.compile("R?(\d+) ?(?:D|Rdd)?", re.IGNORECASE)
amount_min = 666
amount_max = 666
average_tip = float(amount_min + amount_max) / 2

def rand_amount(minimum, maximum):
    return random.randint(minimum, maximum)

def pick_random_comment():
    global amount_min
    global amount_max

    file = open('idlist2.txt', 'r')
    already_done = file.read()
    file.close()
    tipblacklist = ['Name', 'Name', 'Name', 'Name']
    subreddit = r.get_subreddit('reddcoin')
    subreddit_comments = subreddit.get_comments(limit=50)
    comments_list = list(subreddit_comments)
    randomcomment = random.choice(comments_list)
    author = randomcomment.author
    op_text = randomcomment.body
    has_praw = any(string in op_text for string in prawWords)
    if randomcomment.id not in already_done and author.name not in tipblacklist and has_praw:
            rddtip = str(rand_amount(amount_min, amount_max))
            randomcomment.reply('This is a Zombie Tip [¬º-°]¬ [̲̅$̲̅(̲̅)̲̅$̲̅] +/u/reddtipbot ' + rddtip + ' RDD Happy Halloween!')
            already_done = already_done+' '+randomcomment.id
            file = open('idlist2.txt', 'w')
            file.write(already_done)
            file.close()
            print(randomcomment.id + '  ' + author.name + '  ' + rddtip +' Rdd')
    else:
            print(randomcomment.id + ' ##Failed to meet criteria, Picking again## ')
            pick_random_comment()

def pick_random_comment2():
    global amount_min
    global amount_max

    file = open('idlist2.txt', 'r')
    already_done = file.read()
    file.close()
    tipblacklist = ['Name', 'Name', 'Name', 'Name']
    subreddit = r.get_subreddit('reddcoin')
    subreddit_comments = subreddit.get_comments(limit=50)
    comments_list = list(subreddit_comments)
    randomcomment = random.choice(comments_list)
    author = randomcomment.author
    op_text = randomcomment.body
    has_praw = any(string in op_text for string in prawWords)
    if randomcomment.id not in already_done and author.name not in tipblacklist and has_praw:
            rddtip = str(rand_amount(amount_min, amount_max))
            randomcomment.reply('This is a Zombie Tip [¬º-°]¬ [̲̅$̲̅(̲̅)̲̅$̲̅] +/u/reddtipbot ' + rddtip + ' RDD Happy Halloween!\n\n Unfortunately your brain was not large enough to satisfy, looking for another victim!')
            already_done = already_done+' '+randomcomment.id
            file = open('idlist2.txt', 'w')
            file.write(already_done)
            file.close()
            print(randomcomment.id + '  ' + author.name + '  ' + rddtip +' Rdd')
            pick_random_comment()
    else:
            print(randomcomment.id + ' ##Failed to meet criteria, Picking again## ')
            pick_random_comment2()

def pick_random_comment3():
    global amount_min
    global amount_max

    file = open('idlist2.txt', 'r')
    already_done = file.read()
    file.close()
    tipblacklist = ['Name', 'Name', 'Name', 'Name']
    subreddit = r.get_subreddit('reddcoin')
    subreddit_comments = subreddit.get_comments(limit=50)
    comments_list = list(subreddit_comments)
    randomcomment = random.choice(comments_list)
    author = randomcomment.author
    op_text = randomcomment.body
    has_praw = any(string in op_text for string in prawWords)
    if randomcomment.id not in already_done and author.name not in tipblacklist and has_praw:
            rddtip = str(rand_amount(amount_min, amount_max))
            randomcomment.reply('This is a Spider Tip /╲/\╭( ͡° ͡° ͜ʖ ͡° ͡°)╮/\╱\ [̲̅$̲̅(̲̅)̲̅$̲̅] +/u/reddtipbot ' + rddtip + ' RDD Happy Halloween!')
            already_done = already_done+' '+randomcomment.id
            file = open('idlist2.txt', 'w')
            file.write(already_done)
            file.close()
            print(randomcomment.id + '  ' + author.name + '  ' + rddtip +' Rdd')           
    else:
            print(randomcomment.id + ' ##Failed to meet criteria, Picking again## ')
            pick_random_comment3() 

def pick_random_comment4():
    global amount_min
    global amount_max

    file = open('idlist2.txt', 'r')
    already_done = file.read()
    file.close()
    tipblacklist = ['Name', 'Name', 'Name', 'Name']
    subreddit = r.get_subreddit('reddcoin')
    subreddit_comments = subreddit.get_comments(limit=50)
    comments_list = list(subreddit_comments)
    randomcomment = random.choice(comments_list)
    author = randomcomment.author
    op_text = randomcomment.body
    has_praw = any(string in op_text for string in prawWords)
    if randomcomment.id not in already_done and author.name not in tipblacklist and has_praw:
            rddtip = str(rand_amount(amount_min, amount_max))
            randomcomment.reply('This is a Ghost Tip (~°□°）~ [̲̅$̲̅(̲̅)̲̅$̲̅] +/u/reddtipbot ' + rddtip + ' RDD Happy Halloween!')
            already_done = already_done+' '+randomcomment.id
            file = open('idlist2.txt', 'w')
            file.write(already_done)
            file.close()
            print(randomcomment.id + '  ' + author.name + '  ' + rddtip +' Rdd')
    else:
            print(randomcomment.id + ' ##Failed to meet criteria, Picking again## ')
            pick_random_comment4()

def pick_random_comment5():
    global amount_min
    global amount_max

    file = open('idlist2.txt', 'r')
    already_done = file.read()
    file.close()
    tipblacklist = ['Name', 'Name', 'Name', 'Name']
    subreddit = r.get_subreddit('reddcoin')
    subreddit_comments = subreddit.get_comments(limit=50)
    comments_list = list(subreddit_comments)
    randomcomment = random.choice(comments_list)
    author = randomcomment.author
    op_text = randomcomment.body
    has_praw = any(string in op_text for string in prawWords)
    if randomcomment.id not in already_done and author.name not in tipblacklist and has_praw:
            rddtip = str(rand_amount(amount_min, amount_max))
            randomcomment.reply('This is a Zombie Invasion [¬º-°]¬ [¬º-°]¬ [¬º-°]¬ [¬º-°]¬ [¬º-°]¬ all carrying Reddcoin +/u/reddtipbot 3330 RDD Happy Halloween!')
            already_done = already_done+' '+randomcomment.id
            file = open('idlist2.txt', 'w')
            file.write(already_done)
            file.close()
            print(randomcomment.id + '  ' + author.name + '  3330 Rdd')
    else:
            print(randomcomment.id + ' ##Failed to meet criteria, Picking again## ')
            pick_random_comment5()

#Look for incoming tip
def check_inbox():
    file = open('idlist2.txt', 'r')
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
                message.reply('Thank you! [¬º-°]¬ This will help to keep me eating brains!')
                print('$$ Someone Donated $$   ' )
            else:
                message.reply('Thank you! [¬º-°]¬ This will help to keep me eating brains!')
            already_done = already_done+' '+message.id
            file = open('idlist2.txt', 'w')
            file.write(already_done)
            file.close()
            print('$ Someone Donated $' )
            break

def randomize_func():
    global randomfun
    funchoices = ('pick_random_comment', 'pick_random_comment2', 'pick_random_comment3', 'pick_random_comment4', 'pick_random_comment5')
    randomfun = random.choice(funchoices)
    print(randomfun)

while True:
    print('Bot Started/loop completed' )
    randomize_func()
    locals()[randomfun]()  
    check_inbox()
    time.sleep(600)
