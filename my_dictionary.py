# what we have to do is to create a dictionary, similar to the real-world dictionary.
# There is no limit to the definition you provide to any word as this exercise is just for your practice.

# The details and functionalities that are essential and must be present are:

# User will give a word as an input.
# Suppose that the word is present in your dictionary along with its definition or meaning.
# The program will print the meaning or definition of that word.

d1 = {"abandon": "cease to support or look after (someone); desert",
      "inhibit": "hinder, restrain, or prevent (an action or process)",
      "pandemic": "(of a disease) prevalent over a whole country or the world.",
      "bolster": "support or strengthen"}
word = input("Enter a word to find its meaning : ")
print("The meaning of " + word + " is " + d1[word])
