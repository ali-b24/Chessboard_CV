import numpy as np
import cv2

# Define the size of the chessboard
board_size = (8, 8)

# Create an empty black image
img = np.zeros((400, 400), dtype=np.uint8)

# Define the size of each square in the chessboard
square_size = img.shape[0] // board_size[0]

# Loop through each square in the chessboard
for i in range(board_size[0]):
    for j in range(board_size[1]):
        # Determine the color of the square based on its position
        if (i + j) % 2 == 0:
            color = 255
        else:
            color = 0
        # Draw the square on the image
        img[i * square_size:(i + 1) * square_size,
            j * square_size:(j + 1) * square_size] = color

# Show the resulting image
cv2.imshow("Chessboard", img)
cv2.waitKey(0)
cv2.destroyAllWindows()