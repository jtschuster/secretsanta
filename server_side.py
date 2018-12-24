# from flask import Flask, redirect, url_for, request
# app = Flask(__name__)

# usern = []

# @app.route('/success/<name>')
# def success(name):
#     res = ""
#     for nm in name:
#         res = res + str(nm)
#     return 'welcome %s' % res

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       usern.append(request.form['nm'])
#       return ""
#    else:
#       usern.append(request.args.get('nm'))
#       return ""

# @app.route("/addname", methods = ['POST', 'GET'])
# def showlist():
#     if request.method == 'POST':
#       return redirect(url_for('success',name = usern))
#     else:
#       return redirect(url_for('success',name = usern))


# if __name__ == '__main__':
#    app.run(debug = True)

from flask import Flask, make_response, render_template, request, redirect, url_for
app = Flask(__name__)
from collections import defaultdict
import random


def pickNames(names):     
    justnames = []  # has a list of names used for choosing at random
    for name in names:
        justnames.append(name[0])

    # a hash table with names as a key and a list of people they can't have as the value
    # represents a graph where people already have themselves and anyone in their family
    adjacency_list = {}

    for name in names:  # populated the graph with data from the names array of tuples
        li = []
        for name2 in names:
            if name2[1] == name[1]:
                li.append(name2[0])
        adjacency_list[name[0]] = li


    # a hashtable with sizes of groups as the keys and names as the values - used to order those in the largest groups/families first
    group_sizes = defaultdict(list)
    for name in adjacency_list.keys():
        size = len(adjacency_list[name])
        group_sizes[size].append(name)

    # list of sizes of families to
    group_sizes_list = sorted(group_sizes, reverse=True)

    if group_sizes_list[0] > len(justnames)/2:
        return -1

    keyhasgotval = {}  # to hold the final picks of who has who
    for size in group_sizes_list:  # picks who has who, starting with those in the largest groups going to the smallest
        # for each group size, go through the names of those in those group sizes
        for name in group_sizes[size]:
            # randomly assign it a name from the justname array (should be renamed namehat)
            namehas = justnames[random.randrange(len(justnames))]
            #print(name + " has " + namehas)
            # change the name if it appears in the list of names he can't have
            while (namehas in adjacency_list[name]):
                namehas = justnames[random.randrange(len(justnames))]
                #print(name + " has " + namehas)
            # once we found a name that works, remove name from hat
            justnames.remove(namehas)
            # key is person, value is who they have, or could be the other way, doesn't actually matter
            keyhasgotval[name] = namehas

    for key, val in keyhasgotval.items():
        print(key + " has " + val)
    return keyhasgotval


def sendEmail(receiver, message):
    import smtplib, ssl
    from flask import Flask

    port = 465  # For SSL
    password = "ssjtschuster"

    # Create a secure SSL context
    context = ssl.create_default_context()

    sender_email = "secret.santa.name.picker@gmail.com"
    receiver_email = receiver

    # receiver_email = "jackson.schuster345@gmail.com"
    message = "Subject: Your name(s) for Secret Santa \n" + message

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("secret.santa.name.picker@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)

def parsePreview(formdata): #returns in order of 
    result = formdata
    names = []
    emails = defaultdict(list)
    email = "ope"
    for key, val in result.items():
        print(key + " = " + val + " from " + email)
        if key == val: #must be the email
            email = val
        elif key == "creatorName":
            creatorName = val
        elif key == "eventName":
            eventName = val
        else:
            names.append([val, email])
            emails[email].append(key)
    for email in emails:
        message = f"Hello!\n{creatorName} created a Secret Santa gift exchange for {eventName}. You have been assigned the following name(s):\n\n"
        for name in emails[email]:
            message = message + name + " has " + result[name] + "\n"
        print(message)
        sendEmail(email, message)

@app.route('/')
def index():
   return render_template('index.html')

@app.route("/preview", methods = ["POST", "GET"])
def previewSend():
    print("it's connected at least")
    if request.method == 'POST':
        result = request.form
        parsePreview(result)
        return "Emails have been sent"


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        names = []
        emails = defaultdict(list)
        fam = "whoops"
        preview = False
        for key, val in result.items():
            if key == "eventName":
                eventName = val
            elif key == "creatorName":
                creatorName = val
            elif key[0:5] == "email":
                email = val
            elif key == "preview":
                preview = True
                print("preview = " + str(preview))
            else:
                names.append([val, email])
                emails[email].append(val)
        for tup in names:
            print(tup[0] + " " + tup[1])
        result = pickNames(names)
        if result == -1:
            return "can't do this shit"
        else:
            if preview:
                # put an array of tuples with who has who as the
                #   values for a dictionary to use as the values
                #   to  prefill a new form as
                res = {}
                newresult = {}
                for email, names in emails.items():
                    reassign = []
                    for name in names:
                        hasgot = [name, result[name]]
                        reassign.append(hasgot)
                    newresult[email] = reassign
                print(newresult)
                return render_template("preview.html", result = newresult, eventName = eventName, creatorName = creatorName)
            else:
                for email in emails:
                    message = f"Hello!\n{creatorName} created a Secret Santa gift exchange for {eventName}. You have been assigned the following name(s):\n\n"
                    for name in emails[email]:
                        message = message + name + " has " + result[name] + "\n"
                    print(message)
                    sendEmail(email, message)
                return render_template("result.html",result = result)

if __name__ == '__main__':
    app.run(debug = True)


# if preview return a page with names in a new form and a submit
#   button that will take in all the data already there and send
#   the emails
