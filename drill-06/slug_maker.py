""" **Implement slug_maker(title). Remove leading and trailing spaces, convert the text to lowercase, remove commas and periods, and replace spaces with hyphens. Return the final slug.**"""


def slug_maker(title):
    title = title.strip()
    title = title.lower()
    title = title.replace(",", "")
    title = title.replace(".", "")
    title = title.replace(" ", "-")
    return title
print(slug_maker("  My First Blog, Today.  "))