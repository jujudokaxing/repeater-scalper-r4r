import praw
from alive_progress import alive_bar
import datetime

# token
reddit = praw.Reddit(client_id = '',
					client_secret = '', 
					username = '',
					password = '',
					user_agent = '',)


usernumberlimit = None # declare how many posts; None is accepted
subreddit = reddit.subreddit('phr4r') # declare what subreddit; may apply to PhR4Friends and similar subreddits
newsubrr = subreddit.new(limit=usernumberlimit) 

user_list = []
post_list = []
repeater_user = []
dmpcnt = 0

with alive_bar(usernumberlimit) as bar:
	for submission in  newsubrr:
		try:
			if "[F4M]" in str(submission.title.upper()):
				if submission.author in user_list: # checks if user is in the user list already
					if repeater_user.count(submission.author) < 1:	# checks if user has been counted already
						repeater_user.append(submission.author)
				user_list.append(submission.author)
				post_list.append(submission.title)
		except:
			pass
		dumpcnt = dmpcnt + 1
		bar()

print('\n\nDone!\n\n')
main_post_list = []

def get_date(submission):
	time = submission.created
	d = datetime.datetime.fromtimestamp(time)
	d = str(d)
	return d


for st in repeater_user:
	reddituser = reddit.redditor(str(st))
	posts_user = reddituser.submissions.new(limit=None)
	user_posts = []
	subreddit_dump = []
	temp_list_subm = []
	print('Posts by ' + str(reddituser), end='')
	print(': \n')
	for submissions2 in posts_user:
		user_posts.append(submissions2.title)
		print(str(get_date(submissions2)), end='')
		print('\t', end='')
		print(submissions2.subreddit, end='')
		print('\n\t\t\t', end='')
		subreddit_dump.append(submissions2.subreddit)
		print(submissions2.title)
		temp_list_subm.append(submissions2.title)
		print('\n')
	main_post_list.append(user_posts)
	ints_list = subreddit_dump
	ints_list1 = list(set(ints_list))
	print('\tTotal Posts: ' + str(len(temp_list_subm)))
	print('\tActive Subreddits:  ', end='')
	for g in ints_list1:
		print(str(g) + ', ', end='')

	print('\n\n ------------------------- \n\n')
