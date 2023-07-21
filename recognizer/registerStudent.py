import face_recognition,cv2,pickle,os
from . import spreadsheet

photo_folder = 'C:/Users/mozub/Desktop/face_recognizer/Registered Face Photos/'
facial_encodings_folder='C:/Users/mozub/Desktop/face_recognizer/Registered Face Encodings/'


def encoding_of_enrolled_person(name,image):
    enroll_encoding=[]

    enroll_encoding.append(face_recognition.face_encodings(face_recognition.load_image_file(image))[0])
    f=open(facial_encodings_folder+name+'.txt','w+')
    
    with open(facial_encodings_folder+name+'.txt','wb') as fp:
        pickle.dump(enroll_encoding,fp)
    f.close
    
    

def enroll_via_camera(name,email,roll_no):
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    if name+'.txt' in os.listdir(facial_encodings_folder):
        return "Already Enrolled!!"
    else:
     print("hit y to capture and q to quit")   
     while True:
            ret,frame=cap.read()
            cv2.imshow('Enrolling new attendee',frame)
            k=cv2.waitKey(1)
            if k & 0xFF==ord('y'):
                cv2.imwrite(photo_folder+name+'.jpg',frame)
                encoding_of_enrolled_person(name,photo_folder+name+'.jpg')
                cv2.destroyAllWindows()
                break
            if k& 0xFF==ord('q'):
                print('quitting')
                cv2.destroyAllWindows()
                break
     cap.release()
     spreadsheet.enroll_person_to_sheet(name,email,roll_no)
     return "Enrolled Successfully!!"
    
    