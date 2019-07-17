import random

fileName = "words.txt"
with open(fileName) as f:
  wordList = f.readlines()

index = random.randint(0, len(wordList))
string = wordList[index]
word = list(string[0:-1])
List = []

for letter in word:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        List.append(letter)
    else:
        List.append("_")

print(List)
count = 6

while count > 0 and "_" in List:
    guess = input("Guess a letter: ")

    if guess in word:
        print("Right match")
        print("\n")
        List[word.index(guess)] = guess
    else:
        print("Wrong guess!")
        count -= 1

        if count > 0:
            print("\n")
            print("You have " + str(count) + " chance left")
        else:
            print("\n")
            print("Sorry, You Loose")
            print("The correct word was: " + string)
            break;

    if "_" not in List:
        print("Great, You won!")
        print("The word is: " + string)
        break;

    print(List)
