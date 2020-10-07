import cv2
path="C:/Users/Hp/Desktop/star.jpg"
img=cv2.imread(path)

print(img.shape)
a=int(input("Enter the height: "))
b=int(input("Enter the width: ")) 
width ,height=b ,a
#width ,height=400 ,400
imgResize=cv2.resize(img,(width,height))
#imgCropped=img[0:900,300:540]
print(imgResize.shape)
cv2.imshow("cloud",img)
cv2.imshow("cloud Resized",imgResize)
#cv2.imshow("cloud Cropped",imgCropped)
cv2.waitKey(0)