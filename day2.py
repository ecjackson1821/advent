
def dive(plot):
    """
    """
    aim, horizontal, depth = (0, 0, 0)
    for movement in plot:
        split = movement.split(" ")
        direction = split[0]
        unit = int(split[1])
        if direction == "forward":
            horizontal = horizontal + unit
            depth = depth + (aim * unit)
            continue
        elif direction == "down":
            aim = aim + unit
            continue
        elif direction == "up":
            aim = aim - unit
    product = horizontal * depth
    return product 

