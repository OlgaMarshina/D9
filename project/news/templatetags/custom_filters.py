from django import template


register = template.Library()


@register.filter()
def censor(text):

    spl_text = text.split()

    explicitwords = ['мода', 'тренд', 'диета']

    for ex_word in explicitwords:
        ex_word = ex_word.title()

        for word in spl_text:

            word1 = word[0].upper() + word[1:]

            if word1 == ex_word:

                text = text.replace(word, word[0] + '*' * (len(word) - 1))

    """Removes all values of arg from the given string"""
    return text