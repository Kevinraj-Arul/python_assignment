def generate_logo(thickness):
    if thickness % 2 == 0:
        raise ValueError("Thickness must be an odd number.")

    c = 'H'
    logo_lines = []

    # Top cone
    for i in range(thickness):
        line = (c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1)
        logo_lines.append(line)

    # Top pillars
    for i in range(thickness + 1):
        line = (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)
        logo_lines.append(line)

    # Middle belt
    for i in range((thickness + 1) // 2):
        line = (c * thickness * 5).center(thickness * 6)
        logo_lines.append(line)

    # Bottom pillars
    for i in range(thickness + 1):
        line = (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)
        logo_lines.append(line)

    # Bottom cone
    for i in range(thickness):
        line = (
            (c * (thickness - i - 1)).rjust(thickness)
            + c
            + (c * (thickness - i - 1)).ljust(thickness)
        ).rjust(thickness * 6)
        logo_lines.append(line)

    return logo_lines