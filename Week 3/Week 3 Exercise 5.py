# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 16:46:58 2021

@author: aland
"""

infile = open("C:\\Users\\aland\\Documents\\Uni\Programming Statistics\Week 3\music_review.txt", "r")
music_string = infile.read()
music_string_f = music_string.split(" ")
music_dict = {}
banned_list = ["a","A","i","I","an","An","The","the","and","to","of","that"]

for word in music_string_f:
    if word not in banned_list:
        if word not in music_dict:
            music_dict[word] = 1
        else:
            music_dict[word] += 1
        

a = sorted(music_dict.items(), key=lambda x: x[1])    
print(a)