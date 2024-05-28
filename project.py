import random
"""
pseudocode:

prompt the user to pick a mad libs sentence. mabye make 10-15 of them.
the sentences will be lists, so that the program can later combine them.

along with the sentence include a list of numbers, those numbers will
tell the program what to ask for, ex: verb, noun, etc.

prompt the user for the required inputs.

spit out the resulting chaos.

- with the sentences, include the list positions for the blank words.

- Sentences Were Taken From Google Images :P

input 0 to cancel

"""
def kill():
    try:
        net = 0 / 0
        return net
    except RangeError:
        print("Program Stopped.")

def Adjective():
    adjective = input("Give Me An Adjective. (describes a noun.) input 0 to cancel")
    if adjective == "0":
        print(kill())
    else:
        return adjective
def Noun():
    noun = input("Give Me A Noun. (Person, Place, Or Thing.) input 0 to cancel")
    if noun == "0":
        print(kill())
    else:
        return noun
def Type_Of_Bird():
    bird = input("Give Me A Type Of Bird. input 0 to cancel")
    if bird == "0":
        print(kill())
    else:
        return bird
def Room_In_House():
    room = input("Give Me A Room In A House. input 0 to cancel")
    if room == "0":
        print(kill())
    else:
        return room
def Verb():
    verb = input("Give Me A Verb. (describes an action.) input 0 to cancel")
    if verb == "0":
        print(kill())
    else:
        return verb
def Verb_PastTense():
    ptverb = input("Give Me A Past-Tense Verb. (describes an action already done.) input 0 to cancel")
    if ptverb == "0":
        print(kill())
    else:
        return ptverb
def Person():
    person = input("Give Me The Name Of A Person. input 0 to cancel")
    if person == "0":
        print(kill())
    else:
        return person
def Noun_Plural():
    pnoun = input("Give Me A Plural Noun. (people, places, or things.) input 0 to cancel")
    if pnoun == "0":
        print(kill())
    else:
        return pnoun
def Verb_EndingWith_ING():
    verbing = input("Give Me A Verb That Ends With 'ing'. (a verb describes an action.) input 0 to cancel")
    if verbing == "0":
        print(kill())
    else:
        return verbing
def Body_Part():
    bodypart = input("Give Me A Body Part. input 0 to cancel")
    if bodypart == "0":
        print(kill())
    else:
        return bodypart
def Place():
    place = input("Give Me The Name Of A Place. input 0 to cancel")
    if place == "0":
        print(kill())
    else:
        return place
def Activity():
    activity = input("Give Me An Activity/Something To Do. input 0 to cancel")
    if activity == "0":
        print(kill())
    else:
        return activity
def Relative():
    relative = input("Give Me A Relative (ex: Aunt, Mom, Dad) input 0 to cancel")
    if relative == "0":
        print(kill())
    else:
        return relative
def Item():
    item = input("Give Me An Item Name. input 0 to cancel")
    if item == "0":
        print(kill())
    else:
        return item
def Verb_EndingWith_ED():
    verbed = input("Give Me A Verb Ending With ED. (A Verb Describes An Action.) input 0 to cancel")
    if verbed == "0":
        print(kill())
    else:
        return verbed
def Exclaimation():
    exclaim = input("Give Me A Word You Would Use As An Exclaimation. input 0 to cancel")
    if exclaim == "0":
        print(kill())
    else:
        return exclaim
def Number():
    num = input("Give Me A Number Between 10 and 99. input 0 to cancel")
    if num == "0":
        print(kill())
    else:
        return num



def libs1():
    print(f"It Was A {Adjective()}, Cold November Day. I Woke Up To The {Adjective()} Smell Of {Type_Of_Bird()} Roasting In The {Room_In_House()} Downstairs. I {Verb_PastTense()} Down The Stairs To See If I Could Help {Verb()} The Dinner. My Mom Said; See If {Person()} Needs A Fresh {Noun()}. So I Carried A Tray Full Of {Noun_Plural()} Into The {Room_In_House()}. When I Got There, I Couldn't Beleive My {Body_Part()}s! There Were {Noun_Plural()} {Verb_EndingWith_ING()} On The {Noun()}!")
def libs2():
    print(f"A {Noun()} In {Place()} Was Arrested This Morning After They {Verb_PastTense()} A {Noun()} In Front Of {Place()}. {Person()} Had A History Of {Verb_EndingWith_ING()}, But Nobody, Not Even Their {Relative()} Ever Imagined They'd End Up With A {Item()} Stuck In Their {Body_Part()}. 'I Always Thought They Were {Adjective()}, But I Never Could've Imagined They'd Do Something Like This. Even Their {Relative()} Was Surprised.' After A Brief {Activity()}, Cops Followed Them To A {Place()}, Where They Reportedly {Verb_EndingWith_ED()} In The {Noun()}. Either Way, We Imagine That After Witnessing Them {Verb()} with a {Noun()}, There Will Probably Be A Whole Lot Of {Noun_Plural()} That Are Going To Need Therapy. This Is {Person()}, Channel 5 News.")
def libs3():
    print(f"PATIENT: Thank You So Very Much For Seeing Me Doctor {Person()}, And On Such {Adjective()} Notice Too. DOCTOR: What Is Your Problem, Young {Noun()}? PATIENT: I Have A Pain In My Upper {Body_Part()} Which Is Giving Me A Severe {Body_Part()}-Ache. DOCTOR: Let Me Take A Look. Open Your {Body_Part()} Wide. Good, Now I'm Going To Tap Your {Noun_Plural()} With My {Noun()}. PATIENT: Shouldn't You Give Me A {Noun()} Killer? DOCTOR: It's Not Neccessary Yet. {Exclaimation()}! I Think I See A {Noun()} In Your Upper {Body_Part()}! PATIENT: Are You Going To Pull My {Noun()} Out? DOCTOR: No, I'm Going To {Verb()} Your {Noun()} And Put It In A Temporary {Noun()}. PATIENT: When Do I Come Back For The {Noun()} Checkup? DOCTOR: A Day After I Cash My {Noun()}.")
def libs4():
    print(f"{Number()}% Of Internet {Noun_Plural()}, Or About {Number()} Million {Noun_Plural()} Said They Went {Adjective()} To Get News Or {Noun()} About The 20{Number()} Elections. We Call Them {Adjective()} {Noun()} Political Consumers. {Number()}% Of {Noun()} Users Or About {Number()} Million People Said They Used {Noun_Plural()} To Discuss {Noun()}, And One Of The Most {Adjective()} {Noun_Plural()} Was Jokes About The {Noun()} And The Election. {Number()}% Of {Noun_Plural()} Or More Than {Number()} Million People {Verb()} Online To {Verb()} Directly Into {Adjective()} Activities Such As Donating {Noun_Plural()}, Volunteering, Or Chatting About {Adjective()} Events To Attend. I Think President {Person()} is a {Adjective()} {Noun()} and should be {Verb_PastTense()} In The {Noun()}.")

def madlibs():
    libsum = random.randint(1,4)
    if libsum == 1:
        libs1()
    elif libsum == 2:
        libs2()
    elif libsum == 3:
        libs3()
    elif libsum == 4:
        libs4()
    else:
        print(f"Something Went {Adjective()} Wrong.")

madlibs()
