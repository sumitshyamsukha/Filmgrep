from moviepy.editor import *

clip = VideoFileClip("wows.mp4")

subs = open("wows.srt", "r") 

key_word = "fuck"
key_word_count = 0
movie = "The Wolf of Wall Street"

word_times = {}
word_times[key_word] = []

word_list = ["fuck", "fucker", "fucking", "fucked", "fucks", "fuckers", "motherfucker", 
             "motherfuckers", "motherfuck", "motherfucking", "fuckety", "fuckload", 
             "fuckhead", "fuckheads", "fuckloads", "fucktard", "fuckturd"]

delimiters = ["<i>", "</i>", ".", "!", ",", "'", "?"]

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
		text = " ".join(text.split()) # remove multiple spaces between words
		words = text.split()
		seen = false
		for word in words: 
			word = word.lower()
			if word in word_list: # for each word in word_list
				key_word_count = key_word_count + 1 #increment count
				if seen == false : 
					word_times[key_word].append(line)
					seen = true # Don't add the same time interval more than once!

print key_word + " appears in " + movie + " " + str(key_word_count) + " times "

clips = []  
for time in word_times[key_word]:
	split = time.index("--> ") 
	start = time[0: split]
	end = time[split + len(split): ]
	clips.append(clip.subclip(start, end)) 

final_clip = concatenate_videoclips(clips)
final_clip.write_videofile("out.mp4") 
