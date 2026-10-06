def color_code(r, g, b):
    return f"#{r:02X}{g:02X}{b:02X}"

colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 128),
    "orange": (255, 128, 0),
}

for name, rgb in colors.items():
    r, g, b = rgb
    hex_value = color_code(r, g, b)
    print(f"{name}: {hex_value}")
    print(f"\033[38;2;{r};{g};{b}m{name} in color\033[0m")
