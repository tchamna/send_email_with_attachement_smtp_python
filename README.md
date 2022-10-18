# send_email_with_attachements_smtp_python
This Python Script will help you <b>send emails containing attachment</b>, to many people, programmatically, using smtp (Simple Mail Transfer Protocol) service.

I used this module as the last module of a series of modules of a data analysis pipeline that I developed for analyzing data and send critical alerts to decision makers. The pipeline would collect data from a source, transform and process the data, look for critical information, store them in a directory, then send it out by email, on a daily-basis, <b>without any human intervention<</b>>.

<b> How to use it?</b>

1. Get a username and password from a SMTP server, and the port of the server that serves the smtp email. You can contact an administrator and ask him these information, or you can use free smtp servers of your choice.

2. Create a working directory where you will store your files. These are the files you would like to attach to your email

3. Provide the to_email addresses as an array. 

4. Provide the cc_email addresses as an array. the bcc_emails does not work for now, just provide an empty array here []

5. Provide the subject of your email and the message you want to send, and that is it!

I have a separate email for the case where the directory does not contain any files




