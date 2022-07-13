import cv2

# Đọc ảnh
image = cv2.imread('kl.jpg')
cv2.imshow('Image', image)
cv2.waitKey()
cv2.destroyAllWindows()

# Chuyển đổi ảnh sang ảnh xám
image = cv2.imread('face.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey()
cv2.destroyAllWindows()

# Làm mờ ảnh
image = cv2.imread('kl.jpg')
blur = cv2.GaussianBlur(image, (7,7), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)
cv2.waitKey()
cv2.destroyAllWindows()

# Lấy ra cạnh của ảnh
canny = cv2.Canny(blur, 125, 175)
cv2.imshow('Canny', canny)
cv2.waitKey()
cv2.destroyAllWindows()

# Giãn các cạnh của ảnh ra
dilated = cv2.dilate(canny, (7,7), iterations=3)
cv2.imshow('Dilated', dilated)
cv2.waitKey()
cv2.destroyAllWindows()

# Xói mòn các cạnh của ảnh ra
eroded = cv2.erode(dilated, (7,7), iterations=3)
cv2.imshow('Eroded', eroded)
cv2.waitKey()
cv2.destroyAllWindows()

# Thay đổi kích thước của ảnh
resized = cv2.resize(image, (300,300), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)
cv2.waitKey()
cv2.destroyAllWindows()

# Cắt một phần ảnh
cropped = image[50:200, 200:400]
cv2.imshow('Cropped', cropped)
cv2.waitKey()
cv2.destroyAllWindows()
