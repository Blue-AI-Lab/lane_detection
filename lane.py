import cv2 as cv

image = cv.imread('road.jpg')

gray =  cv.cvtColor(image,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(5,5),0)
canny = cv.Canny(blur,200,300)
cv.imshow('hello',canny)
cv.imshow('hello',image)

cv.waitKey(0)
