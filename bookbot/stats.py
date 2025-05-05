def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content


def word_counter(content):
    return len(content.split())


def sort_on(dict):
    return dict["num"]


def char_stats(content):
    stats = {}
    for i in content:
        if not i.lower() in stats:
            stats[i.lower()] = 0
        stats[i.lower()] += 1

    char_list = [{"char": c, "num": n} for c, n in stats.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list
