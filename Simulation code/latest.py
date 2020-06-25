import cv2
import os
import numpy as np

def para(texty):
    count=1
    y0, dy = 160, 15
    for i in texty:
        if count%100==0:
            b=count
            print("texty[b]")
            print(texty[b])
            print("ok")
            if ' ' in texty[b]:
                print("inside if")
                texty=texty[:count]+'^'+texty[count:]
                print(texty)
            else:
                print("inside else")
                for b in range((b- 1), -1,-1):
                    print(texty[b])
                    if ' ' in texty[b]:
                        print("replace")
                        print(b)
                        texty=texty[:b]+'^'+texty[b:]
                        break
                        break
        count=count+1
        #print(count)
        #print(i)
        print(texty)
        for i, line in enumerate(texty.split('^')):
            y = y0 + i*dy
            cv2.putText(weighted1, line, (10, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),1,cv2.LINE_AA)



def mousey(event,g,c,flags,param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        l1,m1,n1=weighted1.shape
        close=cv2.imread('close.jpg',1)
        close=cv2.resize(close,(15,15))
        weighted1[20:20+15,m1-25:m1-10]=close
        if ( g>u[0] and c>u[1] and  g<u[2] and  c<u[3]):
            print ("Erlich Bachman (Played by: T. J. Miller)")
            text4="Erlich is a software designer, founder of the company Aviato, and was a main character in this series. Erlich administers the Hacker Hostel, a tech incubator where Richard, Big Head, Dinesh, and Gilfoyle live and work in exchange for 10 percent of their potential businesses. Erlich clings to his glory days, when he sold aviation start-up Aviato, a move that, at least in his mind, qualifies him to be a svengali lording over other tech nerds. He still drives a car emblazoned with multiple Aviato logos and smokes copious amounts of weed. In Fiduciary Duties, a drunk Richard makes Erlich a Pied Piper board member, a decision he later regrets, only to later see Erlich's value to the company and re-offer him a seat on the board. In Two Days of the Condor, it is revealed that Erlich no longer codes due to carpal tunnel syndrome. This role is played by Todd Joseph Miller (born June 4, 1981), who  is an American actor, stand-up comedian, producer, and writer. Miller has also starring roles in films such as Cloverfield, She's Out of My League, Yogi Bear, Deadpool, Office Christmas Party and The Emoji Movie. Miller was born in Denver, Colorado, the son of Leslie Miller, a clinical  psychologist, and Kent Miller, an attorney. His father is of English, Swedish, German, and Scottish ancestry, whereas his mother is of German-Jewish, Austrian-Jewish, and Russian-Jewish descent. IMDb Page: http://www.imdb.com/name/nm2554352/"
            count=1
            y0, dy = 160, 15
            for i in text4:
                if count%100==0:
                    b=count
                    if ' ' in text4[b]:
                        text4=text4[:count]+'^'+text4[count:]
                    else:
                        for b in range((b- 1), -1,-1):
                            if ' ' in text4[b]:                               
                                text4=text4[:b]+'^'+text4[b:]
                                break
                                break
                count=count+1
            #print(text1)
            for i, line in enumerate(text4.split('^')):
                y = y0 + i*dy
                cv2.putText(weighted1, line, (10, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255),1,cv2.LINE_AA)                  

            mini=cv2.imread('erlich.jpg',1) 
            mini=cv2.resize(mini,(int(l1/6),int(m1/6)))
            d1,e1,f1=mini.shape
            weighted1[10:10+d1,10:10+e1]=mini
            cv2.putText(weighted1,"Erlich Bachman (Played by: T. J. Miller)",(10+int(l1/6)+20,10+int(m1/12)),font_heading,0.7,(255,255,255),1)
            cv2.imshow('frame',weighted1)
            cv2.waitKey(0)          

        elif ( g>m[0] and c>m[1] and  g<m[2] and  c<m[3]):
            print ("dinesh")
            text=" Dinesh is a software engineer, and a main fictional character in this series (Silicon Valley). He lives and works in the Hacker Hostel with Richard, Big Head, and Gilfoyle. He possesses a dry wit and skills at writing code, particularly Java. Dinesh often finds himself sparring with Gilfoyle. He is originally from Pakistan but is a US citizen, unlike Gilfoyle. He claims it took him five years to get US citizenship and was asked about Al-Qaeda like 14 times. His role is played by Kumail Nanjiani, who is a Pakistani-American stand-up comedian, actor, writer, and podcast host. Nanjiani was born in Karachi, Pakistan, the son of Shabana and Aijaz Nanjiani. He was raised as a Shia Muslim, but now identifies as an atheist. The Scottish radio presenter Shereen Nanjiani is his second cousin. Nanjiani is best known for being a main cast member on HBO's Emmy Award-nominated series Silicon Valley, as well as for providing the voice of Prismo on the Emmy Award-winning animated series Adventure Time. He starred on the TNT series Franklin & Bash and the Adult Swim series Newsreaders. Nanjiani also co-hosted the Comedy Central show The Meltdown with Jonah and Kumail. In addition to his television and film work, he hosted two podcasts: The Indoor Kids and The X-Files Files. In 2017, Nanjiani starred in the semi-autobiographical romantic comedy film The Big Sick, which he wrote with his wife Emily V. Gordon. They were nominated for the Academy Award for Best Original Screenplay at the 90th Academy Awards.IMDb Page: http://www.imdb.com/name/nm3529685/"
            count=1
            y0, dy = 160, 15
            for i in text:
                if count%100==0:
                    b=count
                    if ' ' in text[b]:
                        text=text[:count]+'^'+text[count:]
                    else:
                        for b in range((b- 1), -1,-1):
                            if ' ' in text[b]:                               
                                text=text[:b]+'^'+text[b:]
                                break
                                break
                count=count+1
            
            #print(text)
            for i, line in enumerate(text.split('^')):
                y = y0 + i*dy
                cv2.putText(weighted1, line, (10, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255),1,cv2.LINE_AA)
            mini=cv2.imread('dinesh.jpg',1) 
            mini=cv2.resize(mini,(int(l1/6),int(m1/6)))
            d1,e1,f1=mini.shape
            weighted1[10:10+d1,10:10+e1]=mini
            cv2.putText(weighted1,"Dinesh Chugtai (Played by: Kumail Nanjiani)",(10+int(l1/6)+20,10+int(m1/12)),font_heading,0.7,(255,255,255),1)
            #cv2.putText(weighted1,text,(10,20+e1),cv2.FONT_HERSHEY_SIMPLEX,0.4,(255,255,255),1)
            cv2.imshow('frame',weighted1)
            cv2.waitKey(0)
        elif ( g>n[0] and c>n[1] and  g<n[2] and  c<n[3]):
            print ("richard")
            text1=" Richard is a software designer, creator of the Pied Piper app and algorithm, and the protagonist in HBO's Silicon Valley. Richard invented and built the start-up Pied Piper, a program designed to find music matches, while living at Erlich’s Hacker Hostel alongside his best friend Big Head and fellow geeks Dinesh and Gilfoyle. Pied Piper’s compression algorithm triggered a bidding war and ultimately garnered funding from Peter Gregory's company Raviga. After winning TechCrunch Disrupt -- and $50,000 -- Richard and Pied Piper are in the spotlight more than ever, which for Richard means non-stop thrills. His role was played by Thomas Steven Middleditch (born March 10, 1982), who is a Canadian actor and television writer. He was cast in a play in grade eight which he said changed everything for him. He went from an indoorsy kid who was bullied, to becoming the funny, popular kid in high school. He discovered improv in grade school from performing with Theatresports. He was nominated for a Primetime Emmy Award for Outstanding Lead Actor in a Comedy Series. He voiced Harold Hutchins in Captain Underpants: The First Epic Movie (2017). Middleditch also appears in ads for Verizon Wireless. IMDb Page: http://www.imdb.com/name/nm3042755/"
            count=1
            y0, dy = 160, 15
            for i in text1:
                if count%100==0:
                    b=count
                    if ' ' in text1[b]:
                        text1=text1[:count]+'^'+text1[count:]
                    else:
                        for b in range((b- 1), -1,-1):
                            if ' ' in text1[b]:                               
                                text1=text1[:b]+'^'+text1[b:]
                                break
                                break
                count=count+1
            #print(text1)
            for i, line in enumerate(text1.split('^')):
                y = y0 + i*dy
                cv2.putText(weighted1, line, (10, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255),1,cv2.LINE_AA)  
            mini=cv2.imread('richard.jpg',1) 
            mini=cv2.resize(mini,(int(l1/6),int(m1/6)))
            d1,e1,f1=mini.shape
            weighted1[10:10+d1,10:10+e1]=mini
            cv2.putText(weighted1,"Richard Hendriks (Played by: Thomas Middleditch)",(10+int(l1/6)+20,10+int(m1/12)),font_heading,0.7,(255,255,255),1)
            cv2.imshow('frame',weighted1)
            cv2.waitKey(0)
        elif ( g>o[0] and c>o[1] and  g<o[2] and  c<o[3]):
            print ("Jared Dunn (Played by: Zach Woods)")
            text2=" Donald Jared Dunn was an executive at Hooli, and one of the main characters in this series. He is the right-hand man to the head of the company, Gavin Belson, but after gaining a particular interest in Richard’s algorithm, quit his job at Hooli to work for Pied Piper. Jared was raised by a series of foster parents, but despite this rocky early life went on to study at Vassar College, earning a B. A. in Economics. Although his real first name is Donald, Gavin Belson started calling him 'Jared' on his first day at Hooli, and the name stuck. He was also the writer and assistant stage manager of the opera American HerStory XX. His role is played by Zach Woods (born September 25, 1984). Woods was born in Trenton, New Jersey. He is Jewish. He is an American actor and comedian. He is best known for starring as Jared Dunn on the HBO comedy series Silicon Valley. Prior to that, he was a series regular for 3 seasons on the NBC sitcom The Office, playing the role of Gabe Lewis. He also recurs on the HBO series Veep and on the USA Network sitcom Playing House. IMDb Page: http://www.imdb.com/name/nm2046855/"
            count=1
            y0, dy = 160, 15
            for i in text2:
                if count%100==0:
                    b=count
                    if ' ' in text2[b]:
                        text2=text2[:count]+'^'+text2[count:]
                    else:
                        for b in range((b- 1), -1,-1):
                            if ' ' in text2[b]:                               
                                text2=text2[:b]+'^'+text2[b:]
                                break
                                break
                count=count+1
            #print(text1)
            for i, line in enumerate(text2.split('^')):
                y = y0 + i*dy
                cv2.putText(weighted1, line, (10, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255),1,cv2.LINE_AA)              
            mini1=cv2.imread('zach.jpg',1)
            mini1=cv2.resize(mini1,(int(l1/6),int(m1/6)))
            d1,e1,f1=mini1.shape
            weighted1[10:10+d1,10:10+e1]=mini1
            cv2.putText(weighted1,"Jared Dunn (Played by: Zach Woods)",(10+int(l1/6)+20,10+int(m1/12)),font_heading,0.7,(255,255,255),1)
            cv2.imshow('frame',weighted1)
            while (cv2.waitKey(0)=='27'):
                break
        elif ( g>p[0] and c>p[1] and  g<p[2] and  c<p[3]):
            print ("Gilfoyle (Plyed by: Martin Starr)")
            text3=" Bertram Gilfoyle is a Senior Security Architect and a main character in this series. Gilfoyle lives and works in the Hacker Hostel with Richard, Big Head, and Dinesh. Often Gilfoyle triumphs in these arguments or reaches an impasse with Dinesh. He is a self-described LaVeyan Satanist, and bears an upside-down cross tattoo on his right arm. His persona is an apathetic badass programmer that has libertarian tendencies. Gilfoyle is originally from Canada and was an illegal immigrant until Articles of Incorporation, in which he gained a visa after being put under pressure by Dinesh. Gilfoyle has a tectonic relationship with his girlfriend named Tara, a fellow member of the LaVeyan Satanists. His relationship with his mother is negative and lacks trust. His mother has betrayed him in the past as evidenced when Gilfoyle refers to her as a backstabbing bitch. This role is played by Martin Starr (born Martin James Pflieger Schienle; July 30, 1982), who  is an American actor and comedian. He is known for the television roles of Bill Haverchuck on the short-lived comedy-drama Freaks and Geeks (1999–2000), Roman DeBeers on the comedy series Party Down (2009–2010), and Bertram Gilfoyle in the HBO series Silicon Valley (2014–present), as well as for his film roles in Knocked Up (2007), Adventureland (2009) and Spider-Man: Homecoming (2017). Starr was born in Santa Monica, California, the son of actress Jean St. James (née Pflieger) and James Schienle. Of German, British and eastern European descent, he is a Buddhist. IMDb Page: http://www.imdb.com/name/nm0771414/"
            count=1
            y0, dy = 160, 15
            for i in text3:
                if count%100==0:
                    b=count
                    if ' ' in text3[b]:
                        text3=text3[:count]+'^'+text3[count:]
                    else:
                        for b in range((b- 1), -1,-1):
                            if ' ' in text3[b]:                               
                                text3=text3[:b]+'^'+text3[b:]
                                break
                                break
                count=count+1
            #print(text1)
            for i, line in enumerate(text3.split('^')):
                y = y0 + i*dy
                cv2.putText(weighted1, line, (10, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255),1,cv2.LINE_AA)              
            mini=cv2.imread('gilfoyle.jpg',1) 
            mini=cv2.resize(mini,(int(l1/6),int(m1/6)))
            d1,e1,f1=mini.shape
            weighted1[10:10+d1,10:10+e1]=mini
            cv2.putText(weighted1,"Gilfoyle (Plyed by: Martin Starr)",(10+int(l1/6)+20,10+int(m1/12)),font_heading,0.7,(255,255,255),1)
            cv2.imshow('frame',weighted1)
            cv2.waitKey(0)  

        else:
            print("out")
def prepare_training_data(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
recognizer.read('C:/Users/Pradeep/Documents/codacus - Copy/trainer/trainer.yml')
font_heading = cv2.FONT_HERSHEY_DUPLEX
font_content = cv2.FONT_HERSHEY_SIMPLEX
m=[10000,10000,10000,10000]
n=[10000,10000,10000,10000]
o=[10000,10000,10000,10000]
p=[10000,10000,10000,10000]
u=[10000,10000,10000,10000]
cap = cv2.VideoCapture('merged.mp4')
while(True):
    ret, frame = cap.read()
    key = cv2.waitKey(1) & 0xff
    if key == 32:#space
        while True:

            key2 = cv2.waitKey(1) or 0xff
            a,b,c=frame.shape
            img=np.zeros((frame.shape),np.uint8)
            weighted1=np.zeros((frame.shape),np.uint8)
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.2,5)
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x-20,y-20), (x+w+20,y+h+20), (0,0,160), 2)
                weighted=cv2.addWeighted(frame,0.39,img,0.69,0)
                weighted[y-20:y+h+20,x-20:x+20+w]=frame[y-20:y+h+20,x-20:x+20+w]
                cv2.namedWindow('frame')
                cv2.setMouseCallback('frame',mousey)
                Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                # if round(100 - confidence, 2)>35.00 :
                if(Id == 1):
                    Id = "Jared Dunn (Played by: Zach Woods) {0:.2f}%".format(round(100 - confidence, 2))
                    o=[x-20,y-20,x+w+20,y+h+20]
                if(Id == 2):
                    Id = "Gilfoyle (Plyed by: Martin Starr) {0:.2f}%".format(round(100 - confidence, 2))
                    p=[x-20,y-20,x+w+20,y+h+20]
                if(Id == 3):
                    Id = "Dinesh Chugtai (Played by: Kumail Nanjiani) "  
                    m=[x-20,y-20,x+w+20,y+h+20]
                if(Id == 4):
                    Id = "Richard Hendriks (Played by: Thomas Middleditch) {0:.2f}%".format(round(100 - confidence, 2)) 
                    n=[x-20,y-20,x+w+20,y+h+20]
                if(Id == 5):
                    Id = "Erlich Bachman (Played by: T. J. Miller) {0:.2f}%".format(round(100 - confidence, 2)) 
                    u=[x-20,y-20,x+w+20,y+h+20]
                if(Id == 6):
                    Id = "lady {0:.2f}%".format(round(100 - confidence, 2)) 
                cv2.rectangle(weighted, (x-22,y-50), (x+w+22, y-22), (0,0,160), -1)
                cv2.putText(weighted, str(Id), (x,y-30), font_heading, 0.6, (255,255,255), 1)
            cv2.imshow('frame', weighted)
            if key2 == 32:
                break
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame',frame)
    if key == ord('q'): 
        break
cap.release()
cv2.destroyAllWindows()
