def popular_words(text, words):
    count_of_popular_words = {}
    text_words = text.lower().split()

    for word in words:
        count_of_popular_words[word] = text_words.count(word) if word not in (' '.join(text_words)).split(word) else 0

    return count_of_popular_words


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
