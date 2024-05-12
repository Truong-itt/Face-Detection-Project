import cv2
import time
import os 
image_path = 'imgs/peoples.jpg'
face_getector = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')

image_path = 'imgs'

def get_faces(img_path):
    #  thuc hien truyen duong dan va xu li phan cac lien quan
    img = cv2.imread(img_path)
    img_gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    faces = face_getector.detectMultiScale(img_gray, 1.3, 4)   
    count = 0
    # duyet qua tung face va luu
    for (x,y, w, h) in faces:    
        img_face = cv2.resize(img[y+ 3: y+h - 3, x + 3 : x+w - 3], (100, 100))  
        # print(img_path.replace('imgs', 'imgs_processed').split('.jpg')[0])
        cv2.imwrite(img_path.replace('imgs', 'imgs_processed').split('.jpg')[0] + 'people_{}.jpg'.format(count), img_face)
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)   
        count +=  1
        
def get_foder(image_path):
    for whatelse in os.listdir(image_path):
        whatelse_path = os.path.join(image_path, whatelse)
        try:
            count = 1
            for sub_whatelse in os.listdir(whatelse_path):
                img_path = os.path.join(whatelse_path, sub_whatelse)
                #  xu li tao folder moi khi chua ton tai 
                if not os.path.isdir(whatelse_path.replace('imgs', 'imgs_processed')):
                    os.mkdir(whatelse_path.replace('imgs', 'imgs_processed'))
                if img_path.endswith('.jpg'):
                    get_faces(img_path)
                    print("Success "+ whatelse_path.replace('imgs', 'imgs_processed') + '\image_{}'.format(count) )
                    count += 1
                    
        except:
            print("this is not a folder")
            pass
        
if __name__ == '__main__':
    get_foder(image_path)
        

        
    
    
    
