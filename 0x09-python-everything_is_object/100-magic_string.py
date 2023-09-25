def magic_string():
    magic_string.count += 1
    return "BestSchool" + (", " + "BestSchool") * (magic_string.count - 1)
magic_string.count = 0
