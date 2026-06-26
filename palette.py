def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip("#")
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return r, g, b

def lighten(r, g, b, amount=0.3):
    r = round(r + (255 - r) * amount)
    g = round(g + (255 - g) * amount)
    b = round(b + (255 - b) * amount)
    return r, g, b

def rgb_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

# --- Main program ---
base_color = input("Enter a hex color (e.g. #C46A82): ")

r, g, b = hex_to_rgb(base_color)
print("Your color in RGB:", (r, g, b))

light_r, light_g, light_b = lighten(r, g, b)
light_hex = rgb_to_hex(light_r, light_g, light_b)

print("Original color:", base_color)
print("Lighter version:", light_hex)