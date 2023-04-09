#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Name: Cynthia NWaka Ogochukwu
# Course: Software Development Coursework 1
# Question: A prestigious football club has hired our Software Development 
# company,estimate each player's salary by rating their skills.
# Answer:
# Create a Boolean Variable name “Valid Input” and initialize it to false.
valid_input = False
while not valid_input:
    speed = int(input('Enter player speed skill: '))
    shooting = int(input('Enter player shooting skill: '))
    passing = int(input('Enter player passing skill: '))
    defending = int(input('Enter player defending skill: '))
    dribbling = int(input('Enter player dribbling skill: '))
    physicality = int(input('Enter player physicality skill: '))
    if not all(0 <= val <= 5 for val in [speed, shooting, passing, defending, dribbling, physicality]):
        print("Invalid input. Please enter a value between 0 and 5.")
    else:
        valid_input = True
# Using the list function to list the players skills
skills = [speed, shooting, passing, defending, dribbling, physicality]
# Here Add all the skills together and Multiply the summation of skills
# by hundred and divide the sum by thirty to get the overall rating
add_all_skills = 0
for skill in skills:
    add_all_skills += skill
overall_rate = add_all_skills * 100/30
if overall_rate >= 80:
    print(1000)
elif 60 < overall_rate < 80:
    print(1000, 700)
elif overall_rate == 60:
    print(700)
elif 45 < overall_rate < 60:
    print(700, 500)
elif overall_rate == 45:
    print(500)
elif 30 < overall_rate < 45:
    print(500, 400)
# Else for the last condition because all other possible conditions
# are less than or equal to 30
else:
    print(400)

