import cv2
import numpy as np
import webbrowser

MIN_MATCH_COUNT=58
MIN_MATCH_COUNT1=23
MIN_MATCH_COUNT2=40
font = cv2.FONT_HERSHEY_SIMPLEX
#detector=cv2.SIFT()
detector=cv2.xfeatures2d.SIFT_create()
FLANN_INDEX_KDITREE=0
flannParam=dict(algorithm=FLANN_INDEX_KDITREE,tree=5)
flann=cv2.FlannBasedMatcher(flannParam,{})

trainImg=cv2.imread("ios.jpg",0)
trainImg1=cv2.imread("mugss.jpg",0)
trainImg2=cv2.imread("lamp.jpg",0)

trainKP,trainDesc=detector.detectAndCompute(trainImg,None)
trainKP1,trainDesc1=detector.detectAndCompute(trainImg1,None)
trainKP2,trainDesc2=detector.detectAndCompute(trainImg2,None)
h1=10
j1=10
k1=10
count1=1
count2=1
count3=1
cam=cv2.VideoCapture('paapom.mp4')
while True:
    ret, QueryImgBGR=cam.read()
    QueryImgBGRCopy=QueryImgBGR.copy()
    QueryImg=cv2.cvtColor(QueryImgBGR,cv2.COLOR_BGR2GRAY)
    queryKP,queryDesc=detector.detectAndCompute(QueryImg,None)
    
    matches=flann.knnMatch(queryDesc,trainDesc,k=2)
    matches1=flann.knnMatch(queryDesc,trainDesc1,k=2)
    matches2=flann.knnMatch(queryDesc,trainDesc2,k=2)

    goodMatch=[]
    for m,n in matches:
        if(m.distance<0.75*n.distance):
            goodMatch.append(m)
    goodMatch1=[]
    for m1,n1 in matches1:
        if(m1.distance<0.75*n1.distance):
            goodMatch1.append(m1)
    goodMatch2=[]
    for m2,n2 in matches2:
        if(m2.distance<0.75*n2.distance):
            goodMatch2.append(m2)
            
    if(len(goodMatch)>MIN_MATCH_COUNT):
        tp=[]
        obj=2
        qp=[]
        for m in goodMatch:
            tp.append(trainKP[m.trainIdx].pt)
            qp.append(queryKP[m.queryIdx].pt)
        tp,qp=np.float32((tp,qp))
        H,status=cv2.findHomography(tp,qp,cv2.RANSAC,3.0)
        h,w=trainImg.shape
        trainBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
        queryBorder=cv2.perspectiveTransform(trainBorder,H)
        a=queryBorder[0][0]
        b=a[0]
        c=a[1]
        #macbook
        if count1==1:
            cv2.polylines(QueryImgBGR,[np.int32(queryBorder)],True,(0,0,160),3)
            #cv2.putText(QueryImgBGR,'MACBOOK',(b,c), font, 0.6,(255,255,255),1,cv2.LINE_AA)
            count1=count1+1
        cv2.putText(QueryImgBGR,"Product being advertised. Press SPACE if interested.",(h1,360), font, 0.6,(255,255,255),1,cv2.LINE_AA)
        h1+=2    
    if(len(goodMatch1)>MIN_MATCH_COUNT1):
        #print("coffee")
        obj=1
        tp1=[]
        
        qp1=[]
        for m1 in goodMatch1:
            tp1.append(trainKP1[m1.trainIdx].pt)
            qp1.append(queryKP[m1.queryIdx].pt)
        tp1,qp1=np.float32((tp1,qp1))
        H1,status1=cv2.findHomography(tp1,qp1,cv2.RANSAC,3.0)
        h,w=trainImg1.shape
        trainBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
        queryBorder=cv2.perspectiveTransform(trainBorder,H1)
        #print(queryBorder)
        a1=queryBorder[0][0]
        b1=a1[0]
        c1=a1[1]
        #print(b1,c1)
        #coffee mug
        if count2==1 or count2==2:
            cv2.polylines(QueryImgBGR,[np.int32(queryBorder)],True,(0,0,160),4)
            count2=count2+1
            #cv2.putText(QueryImgBGR,'COFFEE MUG',(b1,c1), font, 0.4,(255,255,255),1,cv2.LINE_AA)
        cv2.putText(QueryImgBGR,"Product being advertised. Press SPACE if interested.",(j1,360), font, 0.6,(255,255,255),1,cv2.LINE_AA)
        j1+=2
    if(len(goodMatch2)>MIN_MATCH_COUNT2):
        tp2=[]
        obj=3
        qp2=[]
        for m2 in goodMatch2:
            tp2.append(trainKP2[m2.trainIdx].pt)
            qp2.append(queryKP[m2.queryIdx].pt)
        tp2,qp2=np.float32((tp2,qp2))
        H2,status2=cv2.findHomography(tp2,qp2,cv2.RANSAC,3.0)
        h,w=trainImg2.shape
        trainBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
        queryBorder=cv2.perspectiveTransform(trainBorder,H2)
        
        a2=queryBorder[0][0]
        b2=a2[0]
        c2=a2[1]
      
        #lamp
        if count3==1:
            cv2.polylines(QueryImgBGR,[np.int32(queryBorder)],True,(0,0,160),3)
            #cv2.putText(QueryImgBGR,'TABLE LAMP',(b2,c2), font, 0.6,(255,255,255),1,cv2.LINE_AA)
            count3=count3+1
        cv2.putText(QueryImgBGR,"Product being advertised. Press SPACE if interested.",(k1,360), font, 0.6,(255,255,255),1,cv2.LINE_AA)
        k1+=2
    key = cv2.waitKey(1) & 0xff
    if key == 32:#space
        while True:
            key2 = cv2.waitKey(1) or 0xff
            ani=np.zeros((QueryImgBGR.shape),np.uint8)
            weighted=cv2.addWeighted(QueryImgBGRCopy,0.39,ani,0.69,0)
            cv2.polylines(weighted,[np.int32(queryBorder)],True,(0,0,160),3)
            if obj==1:
                text="COFFEE MUG"
                text1="Want to start your day with coffee in this beautiful mug? "
                text2="If so, press esc."
                cv2.putText(weighted,text1,(10,360), font, 0.6,(255,255,255),1,cv2.LINE_AA)
                cv2.putText(weighted,text2,(10,380), font, 0.6,(255,255,255),1,cv2.LINE_AA)
                url="https://www.amazon.com/Black-Coffee-Flag-11oz-Ceramic/dp/B00IXYSQSS"
            if obj==2:
                text="MACBOOK"
                text1="Cool, aint? If you want to be like Richard, press esc and buy it."
                url="https://www.amazon.com/Apple-MD711LL-11-6-Inch-Mavericks-Refurbished/dp/B01M0566PR/ref=sr_1_4?s=electronics&ie=UTF8&qid=1522159659&sr=1-4&keywords=macbook+air"
            if obj==3:
                text="TABLE LAMP"
                text1="Aesthetic lighting sets the mood for everything. Want to buy? Press esc."
                url="http://mesiablabs.com/28729/brown-table-lamp.html/simple-design-brown-table-lamp-vibrant-j-hunt-wood-and-script-tan-29-25-target"
            al=queryBorder[0][2]
            z=al[0]
            x=al[1]  
            cv2.putText(weighted,text,(int(z),int(x)-15), font, 0.6,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(weighted,text1,(10,360), font, 0.6,(255,255,255),1,cv2.LINE_AA)
            cv2.imshow('result',weighted)
            if cv2.waitKey(0) & 0xFF == 27:
                new=2;
                webbrowser.open(url,new=new);
            elif cv2.waitKey(0) & 0xFF == 32:
                break
    #else:
     #   print ("Not Enough match found- %d/%d"%(len(goodMatch),MIN_MATCH_COUNT))
      #  print
       # ("Not Enough match found1- %d/%d"%(len(goodMatch1),MIN_MATCH_COUNT1))
    cv2.imshow('result',QueryImgBGR)
    if key == ord('q'): 
        break
cam.release()
cv2.destroyAllWindows()
