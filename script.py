from moviepy.editor import *

clip = VideoFileClip("wows.mp4") # create a video clip object from moviepy based on the given file

subs = open("wows.srt", "r") # create a file object in reading mode

word_times = {} # dict to store word to time mapping

for line in subs:
	line = line.strip("\n") 
	if "-->" in line: # --> means that it denotes a time in the form start --> end
		line1 = next(subs).strip("\n") # get the actual text of the subtitle
		line2 = next(subs).strip("\n") # this may or may not have text
		if line2 == '':
			text = line1 
		else:
			text = line1 + " " + line2
		words = text.split() # split text up into words
		for word in words: # add each word into the dict
			if word in word_times:
				word_times[word].append(line)
			else:
				word_times[word] = [line]

word = 'fuck' # the word we are searching for

clips = [] # list containing all times the word occurs 
for time in word_times[word]:
	split = time.index("--> ") # split time into start and ending
	start = time[0: split]
	end = time[split + len(split): ]
	clips.append(clip.subclip(start, end)) # create a subclip using moviepy based on the start and end times, add it to the list

final_clip = concatenate_videoclips(clips) # create a new video file by concatenating all subclips in the list
final_clip.write_videofile("out.mp4") # write the actual video file to the hard disk