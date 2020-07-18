import cv2
import numpy as np


def draw_circles(amount=20, min_r=5, max_r=200, colors_RGB=(True, True, True),
                 size=300, fill=0, path='saved_img.jpg'):

    dim = (size, size, 3)
    img = np.empty(dim, dtype=np.uint8)
    img.fill(fill)
    colors_BGR = (colors_RGB[2], colors_RGB[1], colors_RGB[0])
    for _ in range(amount):
        radius = np.random.randint(min_r, max_r + 1)
        center = tuple(np.random.randint(0, size + 1, 2))
        color = np.random.randint(0, 256, 3).tolist()
        color = [color[i] if channel else 0 for i,
                 channel in enumerate(colors_BGR)]
        cv2.circle(img, center, radius, color, -1)
    # cv2.imshow('Press y to save image', img)
    # key = cv2.waitKey(0)
    # if key == 121:
    #     cv2.imwrite(path, img)
    #     print(f'Image saved to {path}')

    cv2.imwrite(path, img)


# draw_circles(colors_RGB=(False, False, True))
