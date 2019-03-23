
def wallpaper(wall_length, wall_width, wall_height, wallpaper_width, wallpaper_length):
    room_perimetr = (float(wall_length) + float(wall_width)) * 2
    cloth_quantity = round(room_perimetr / wallpaper_width)
    cloth_in_one_roll = float(wallpaper_length / wall_height)
    result = float(cloth_quantity / cloth_in_one_roll) + 1
    return result

print(wallpaper(2,2,2,2,10))