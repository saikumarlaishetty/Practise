import pywhatkit as wu

with open("msgs.txt","r") as msg:
    lines = msg.readlines()
    for line in lines:
        #wu.sendwhatmsg_instantly("+91 9515373845",line.strip(),10,True,5)
        # print(line.strip())
        line_list = line.split(',')
        hours = int(line_list[0])
        minutes = int(line_list[1])
        phone_no = line_list[2]
        message = line_list[3]
        wu.sendwhatmsg(phone_no,message,hours,minutes,True,10)

# for i in range(5):
#     wu.sendwhatmsg_instantly("+91 9441121923", "I love you Amma",10,True,5)



#def main():
