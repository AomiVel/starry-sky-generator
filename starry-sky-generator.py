from PIL import Image
import random


rates = {
    "1": 1000, # サイズ 1 の星が生成される確率
    "2": 5,    # サイズ 2 の星が生成される確率(s1 x s2)
    "3": 10,   # サイズ 3 の星が生成される確率(s1 x s2 x s3)
    "4": 30    # サイズ 4 の星が生成される確率(s1 x s2 x s3 x s4)
}


img = Image.new("RGB", (1920, 1080))

img_list = []
for y in range(1080):
    img_list.append([])
    for x in range(1920):
        img_list[y].append((0, 0, 0))

for y in range(1080):
    for x in range(1920):
        if random.randrange(rates["1"]) == 1:
            size = 1
            if random.randrange(rates["2"]) == 1:
                size = 2
                if random.randrange(rates["3"]) == 1:
                    size = 3
                    if random.randrange(rates["4"]) == 1:
                        size = 4

            rgb = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            # r = random.randint(0, 255)
            # rgb = (
            #     r, r, r
            # )

            
            for xx in range(size):
                for yy in range(size):
                    try:
                        # img.putpixel((x + xx, y + yy), rgb)
                        img_list[y - yy][x - xx] = rgb
                    except IndexError:
                        ...
                        pass

        else:
            img_list[y][x] = (0, 0, 0)

for x in range(1920):
    for y in range(1080):
        img.putpixel((x, y), img_list[y][x])

# img.show()
with open("num.txt", "r") as f:
    number = int(f.read())

img.save(f"star-ish{number}.png")

with open("num.txt", "w") as f:
    f.write(str(number + 1))
