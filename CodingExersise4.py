sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#TODO: convert sentence in to a list of words using split method
sentence = sentence.split(" ")
#TODO:
result = {word:len(word) for word in sentence}
print(result)
