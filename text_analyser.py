def char_counter(text, char):
    counter = 0

    for i in text:
        if i == char or i.upper() == char:
            counter += 1
    return counter


filename = input('please input the filename:')
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * char_counter(text, char) / len(text)
    print('{} - {}%'.format(char, round(perc, 2)))
