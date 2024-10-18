import math
import skimage as ski

# ascii_gradient = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"[::-1]
ascii_gradient = " .:-=+*#%@"
print(ascii_gradient)

while True:
    try: 
        filename = input("filename (place in program folder): ")
        image = ski.io.imread(filename, as_gray=True)
        break
    except:
        print("enter a valid image filename!")

stripped_filename = ".".join(filename.split(".")[0:-1])
out = open(f"out/{stripped_filename}.txt", "w")

old_size = (len(image[0]), len(image))

while True:
    try:
        new_width = int(input("text width: "))
        new_height = int(input("text height: "))
        break
    except:
        print("enter integers only!")

new_size = (new_width, new_height)

new_image = [[0 for i in range(new_size[0])] for j in range(new_size[1])]

hratio = old_size[0]/new_size[0]
vratio = old_size[1]/new_size[1]

projected_points = [ [(i*hratio,j*vratio) for i in range(new_size[0])] for j in range(new_size[1])]

for row_num in range(len(projected_points)):
    row = projected_points[row_num]

    for pixel_num in range(len(projected_points[row_num])):
        pixel = row[pixel_num]
        
        overlap = []

        for old_row_num in range(math.floor(pixel[1]),min(math.ceil(pixel[1]+vratio),old_size[1])):
            old_row = image[old_row_num]
            for old_pixel_num in range(math.floor(pixel[0]),min(math.ceil(pixel[0]+hratio),old_size[0])):
                old_pixel = old_row[old_pixel_num]
                overlap.append((old_row_num, old_pixel_num))

        average_value = 0

        for overlapping_pixel in overlap:
            average_value += image[overlapping_pixel[0]][overlapping_pixel[1]]
        
        try:
            average_value /= len(overlap)
        except:
            average_value = 0

        new_image[row_num][pixel_num] = ascii_gradient[round(average_value*(len(ascii_gradient)-1))]

for row in new_image:
    char_row = ""
    for pixel in row:
        char_row += pixel
    char_row += "\n"
    out.write(char_row)
print(f"output in out/{stripped_filename}.txt!")