# Task 1: Keyword Highlighter

# Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

key_words = ["good", "excellent", "bad", "Poor", "average"]   # creating list of keywords to find 
new_reviews = [] 
for review in reviews:  # for each review in reviews list 
    for word in key_words:   # for each word in 'key_words'
        if word in review: # if the word in 'review' and 'key_words' are equal 
            new_reviews.append(review.replace(word, word.upper()))    # add new review with word.upper() to 'new_reviews' 
                
print("First, uppercase the keywords in the given reivews list: ")    

for i in new_reviews: 
    print(i) 

# So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

# Task 2: Sentiment Tally
'''
Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
'''
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] # positive words to search for 
negative_words = ["bad", "Poor", "terrible", "horrible", "awful", "disappointing", "subpar"] # negative words to search for 

count_positive = 0  # set count to 0 for positive words
count_negative = 0  # set count to 0 for negative words 
for review in reviews: 
    for word in positive_words: 
        if word in review:    # if word in review and postive words
            count_positive += 1 # add one tally to count_positive          
    for word in negative_words: 
        if word in review: # if word in review and negative words
            count_negative += 1  # add on tally to count_negative
print("Next, tally the total positive and negative words in each review: ") 
print(f'There are {count_positive} positive words in the reviews and {count_negative} negative words in the reivews.') 

# Task 3: Review Summary

# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.
# Example: "This product is really good. I'm...",

def short_summary(string, length , ending = str):   # define a funciton that takes a string 'review', length of 30 (for num of characters), and string to add ('...')
    if len(string) <= length:   # if the length of the string is less than or equal to our defined length
        return string  # return string (length defined) 
    else: 
        return ' '.join(string[:length+1].split(' ')[0:-1]) + ending # else return a space, followed by the string cut off at desired length, spliton space and remove the last character, then add '...' to end 
    
print("Finally, shorten each review into a summary script: ") 
for review in reviews: 
    review_summary = short_summary(review, 30, "...")  # call the function to each of our 'reviews'
    print(review_summary)    # print each new line 