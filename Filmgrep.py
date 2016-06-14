from moviepy.editor import *

clip = VideoFileClip("wows.mp4") # create a video clip object from moviepy based on the given file

subs = open("wows.srt", "r") 

word_times = {}

slang = ["fuck", "fucker", "fucking", "fucked", "fucks", "fuckers", "motherfucker", 
         "motherfuckers", "motherfuck", "motherfucking", "fuckety", "fuckload", 
         "fuckhead", "fuckheads", "fuckloads", "fucktard", "fuckturd"]

delimiters = ["<i>", "</i>", ".", "!", ",", "'", "?"]

fuck_count = 0

for line in subs:
	line = line.strip() 
	if "-->" in line: 
		line1 = next(subs).strip() 
		line2 = next(subs).strip() 
		for delimiter in delimiters :
			line1 = line1.replace(delimiter, "")
		line1 = line1.replace("-", " ") # special delimiter
		if line2 == '':
			text = line1 
		else:
			for delimiter in delimiters :
				line2 = line2.replace(delimiter, "")
			line2 = line2.replace("-", " ") # special delimiter
			text = line1 + " " + line2
		text = text.strip()
		text = " ".join(text.split())
		words = text.split() # split text up into words
		for word in words: # add each word into the dict
			word = word.lower()
			if word in slang:
				fuck_count = fuck_count + 1
			if word in word_times:
				word_times[word].append(line)
			else:
				word_times[word] = [line]

print "Number of times the word fuck is used in The Wolf of Wall Street -> " + str(fuck_count)

## Tested OK uptil here - Parsing issues fixed

clips = []  
for word in slang :
	for time in word_times[word]:
		split = time.index("--> ") 
		start = time[0: split]
		end = time[split + len(split): ]
		clips.append(clip.subclip(start, end)) 
## Yet to test the above section

final_clip = concatenate_videoclips(clips)
final_clip.write_videofile("out.mp4") 
