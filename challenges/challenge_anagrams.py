def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    firstWord = "".join(merge_sort(list(first_string.lower())))
    secondWord = "".join(merge_sort(list(second_string.lower())))

    return (firstWord, secondWord, firstWord == secondWord)


def merge_sort(word):
    if len(word) <= 1:
        return word

    mid = len(word) // 2
    left = word[:mid]
    right = word[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
