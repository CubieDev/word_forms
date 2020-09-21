from word_forms.word_forms import get_word_forms


def lemmatize(word):
    """
    Out of all the related word forms of ``word``, return the smallest form that appears first in the dictionary
    """
    forms = {word for pos_form in get_word_forms(word).values() for word in pos_form}
    if forms:
        return sorted(forms, key=len)[0]
    else:
        raise ValueError("{} is not a real word".format(word))


