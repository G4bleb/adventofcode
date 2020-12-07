import string


def resolvePart1():
    count = 0
    f = open('6', 'r')
    paragraphs = f.read().split('\n\n')
    f.close()
    for paragraph in paragraphs:
        paragraph = paragraph.replace('\n', '')
        count += len(dict.fromkeys(paragraph))
    return count


def resolvePart2():
    count = 0
    f = open('6', 'r')
    paragraphs = f.read().split('\n\n')
    f.close()
    for paragraph in paragraphs:
        n_people = paragraph.count('\n') + 1
        for letter in string.ascii_lowercase:
            count += n_people == paragraph.count(letter)
    return count


print(resolvePart1())
print(resolvePart2())
