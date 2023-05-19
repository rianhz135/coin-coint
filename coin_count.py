import cv2
import numpy as np

# Load image
image = cv2.imread('coin.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# Perform edge detection
edges = cv2.Canny(blurred, 30, 150)

# Perform a Hough transform
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=30, minRadius=20, maxRadius=60)

# Initialize counter for counting coins
total_coins = 0

# Check if any circles were found
if circles is not None:
    # Convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")

    # Loop over all detected circles
    for (x, y, r) in circles:
        # Draw the circle on the original image
        cv2.circle(image, (x, y), r, (0, 255, 0), 2)

        # Increment the coin counter
        total_coins += 1

# Display the total number of coins
print("Total coins:", total_coins)
cv2.putText(image, 'Jumlah Koin: ' + str(total_coins), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
# Display the image with detected circles
cv2.imshow("Coins", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

