def piglat():
    word=str(input('Please enter your string: '))
    first_letter=word[0]
    if first_letter in 'aeiou':
        pig_word=word+'ay'
    else:
        pig_word=word[1:]+first_letter+'ay'
    print(pig_word)

piglat()

