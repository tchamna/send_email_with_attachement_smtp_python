


import os

#Path of the working directory where the files you want to attach is stored

WD = r"C:\Users\Rtchamna\Desktop\Automated_Pipeline_v02"


###########################################################
# SMTP Server Setting
############################################################
server = 'smtp.office365.com' 
port = 587
username = 'Your User name on the server' 
password = "The password associated with your user name"

###########################################################
# EMail Setting
############################################################

# sender = username
to_address = ['email@domain.com']
cc_address = ['cc1@domain.com', 'cc2@domain.com']
bcc_address = ['bcc1@domain.com', 'bcc2@domain.com'] # This does not work with Outlook Server, for some reason

subject = "The subject of your email"
emailMsg = f"Your message, email content"

subject_rest = "The subject of your email if there is no attachement in the folder"
emailMsg_rest = "Other email if there is no attcahement in the folder"



#####################################################
## ATTACHMENTS
#####################################################
def get_files_name(folder_path):
    """ This function get the list of all files name from a directory"""
    files = []
    # Iterate directory
    for path in os.listdir(folder_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(folder_path, path)):
            files.append(path)
    return files 

def file_extention(file):
    """ This function returns the extension of a given file"""
    # this will return a tuple of root and extension
    split_tup = os.path.splitext(file)
#     print(split_tup)
    ext = split_tup[1]
    return ext

# WD IS the Working Directory where the files you want to attach are located
# WD = sys.argv[3] # Weak Module Directory
# WD = r"C:\Users\Rtchamna\Desktop\Automated_Pipeline_v02"

# Get All File names in the working directory
files_name = get_files_name(WD)

## Filter the type of file you would like to attch
# file_attachments = []
# for file in files_name:
#     if file_extention(file) in [ ".csv", ".txt"] :
#         file_attachments.append(file)
# print(files_name)

##If you just want some particular files, then select the files you are interrested in
file_attachments = [f for f in files_name if f.startswith(f"Weak_Batteries_All_Containers_") | f.endswith("_Level1_Images.zip")]
file_attachments

#####################################################
## END ATTACHMENTS
#####################################################

def send_mail(server, port, username, password, send_to, subject, email_text_content, cc=[], bcc=[], attachment_list=[]):
    import smtplib
    import base64

#     from email.MIMEMultipart import MIMEMultipart
    from email.mime.multipart import MIMEMultipart
    
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
#     from email import encoders
#     from email.utils
    from email.utils import COMMASPACE, formatdate
    from email import encoders
    assert type(send_to)==list
    assert type(bcc)==list
    assert type(cc)==list
    assert type(attachment_list)==list

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = COMMASPACE.join(send_to)
    msg['Bcc'] = COMMASPACE.join(bcc)
    msg['Cc'] = COMMASPACE.join(cc)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(email_text_content) )

    for f in attachment_list:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)
  
    smtp = smtplib.SMTP(server,port)
    
    smtp.ehlo() 
    smtp.starttls() 
    
    smtp.login(username, password) 
    smtp.sendmail(username, send_to, msg.as_string())
    smtp.close()
    
    
# send_mail(server, port, username, password, send_to, subject, email_text_content, cc=[], bcc=[], attachment_list=[])
### BCC DOES NOT WORK
# send_mail(server, port, username, password, send_to, subject, email_text_content, cc=[], bcc=[], attachment_list=[]):
    



if len(file_attachments) != 0:

    send_mail(server, port, username, password, to_address, subject, emailMsg, cc_address, [], file_attachments)

else:

    send_mail(server, port, username, password, to_address, subject_rest, emailMsg_rest, cc_address, [], file_attachments)

        
 