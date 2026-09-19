import cv2

# Read the image
img = cv2.imread("image.jpg")

# Get image dimensions
height, width = img.shape[:2]

# ---------------- ROTATION ----------------
# Rotate by 45 degrees around the center
center = (width // 2, height // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

rotated = cv2.warpAffine(
    img, rotation_matrix, (width, height)
)

# ---------------- SCALING ----------------
# Scale image to 50% of original size
scaled = cv2.resize(
    img, None, fx=0.5, fy=0.5,
    interpolation=cv2.INTER_LINEAR
)

# ---------------- TRANSLATION ----------------
# Move image 100 pixels right and 50 pixels down
translation_matrix = cv2.getRotationMatrix2D(center, 0, 1)
translation_matrix[0, 2] = 100
translation_matrix[1, 2] = 50

translated = cv2.warpAffine(
    img, translation_matrix, (width, height)
)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotated)
cv2.imshow("Scaled Image", scaled)
cv2.imshow("Translated Image", translated)

cv2.waitKey(0)
cv2.destroyAllWindows()