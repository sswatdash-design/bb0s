import os
import filewsys
import time
import sys
import random
import winsound
import math
import scrollart
import webbrowser

sys.set_int_max_str_digits(100000000)
def init_system_context():
    return {
        "mdic": {
            "/": {
                "home": {
                    "notes.txt": " "
                },
                "tmp": {},
                "logs": {},
            }
        },
        "current_path": "/",
        "shutdown": False,
        "gnlin": {
            1: "BBOS stands for Basic Build Operating software \n",
            2: "Entirety of this os is built through sheer python. \n",
            3: "The developer is Saswat Dash \n",
            4: "The order of a command is not sufficed. User may write '%pr home' or 'home %pr' \n",
            5: "This basic software doesn't utilize text files and hence it uses strings, which have been called 'Dash file' \n",
            6: "It has all the utilities that may make the life easier ;) \n",
            7: "Press 'z' in any program to return to prompt. Type 'shutdown' or 'z' at prompt to exit system \n"
        }
    }

def get_current_dir_content(ctx):
   
    if ctx["current_path"] == "/":
        return ctx["mdic"]["/"]
    else:
        # Check if current_path is a valid key in root
        if ctx["current_path"] in ctx["mdic"]["/"]:
             return ctx["mdic"]["/"][ctx["current_path"]]
        return {}

def cmd_help(ctx, args):
    print("Choose: \n","Cmds \n","General Info (gnlin)")
    t = input(">> ")
    if t == "Cmds":
        print("Available programs/commands:", ", ".join(COMMANDS.keys()))
    else:
        for val in ctx["gnlin"].values():
            print(val)

def cmd_show(ctx, args):
    content = get_current_dir_content(ctx)
    print(list(content.keys()))

def cmd_priority(ctx, args):
    target = None
    if len(args) > 0:
        target = args[0]
    
    if not target:
        ctx["current_path"] = "/"
        return

    if target in ctx["mdic"]["/"].keys():
        ctx["current_path"] = target
    else:
        print("directory not found")

def cmd_realfs(ctx, args):
    print("Launching Real File System...")
    filewsys.run_file_system()

def fibcalc(ctx, args):
    k = {0: 0, 1:1}
    def fib(n):
        if n == 0:
            return n
        if n == 1:
            return n

        if n in k.keys():
            return k[n]

        k[n] = fib(n-1) + fib(n-2)
        return k[n]

    print("System booting...")
    op = []
    g = 0
    for ch__ in range(1001):
        g += 100
        fib(g)
        if ch__ % 100 == 0:
            print(ch__//100)

    print("System booted and ready for fib!")

    lim = list(k.keys())[len(k)-1]

    while True:
        olim = lim
        while True:
            try:
                x = int(input(">> "))
            except ValueError:
                print("Enter a valid number.")
            else:
                break

        if x <= lim:
            print(fib(x))
        else:
            print("Laying Base work!")
            while True:
                try:
                    print(fib(x))

                except RecursionError:
                    print(f"Hit a recursion limit. One second boss. The presaved notion was {lim}")

                    if lim == 400400:
                        print("x_x")
                        break

                    g = lim
                    for ch__ in range(1001):
                        g += 100
                        fib(g)

                    lim = list(k.keys())[len(k) - 1]
                else:
                    break


        print("Do u want to see the tree?")


        ch = input()


        if ch == "y":
            print("Auto or manual?")

            cho = input(">>")

            if cho == "Auto":
                for ch_ in k.items():
                    print(ch_)
            else:
                h = 0
                while True:
                    print(k[lim-h])
                    print("\n \n \n")

                    print({"Number of digits of the number": len(str(k[lim-h])),
                           "Number": lim-h})
                    print("More? (y)")
                    t = input("?? ")

                    if t == "y":
                        h+=1
                    elif t == "fun":
                        sj = 0
                        for _ch in str(k[lim-h]):
                            sj += int(_ch)
                        print(sj)
                        h += 1
                    else:
                        break
        if ch == "1":
            while True:
                kl = int(input("Enter the number of numbers: "))

                for i in list(k.items())[:kl+1]:
                    print(i)
                print("Continue?")
                if input(">> ") == "n":
                    break

        print("If you want to stop type 's' or 'z' to return to BBOS..")

        choice = input("?? ")
        if choice == "s":
            break
        elif choice == "z":
            print("going back...")
            scrollart.math_func(max_rows=150)
            os.system("cls")
            print("\n" * 5)
            print(""" ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """.center(100))
            print("\n" * 5)
            break

    return 0

def randomsoundgen(ctx, args):
    l = []
    for i in range(50):
        l.append((random.randrange(1000, 2100, 100), i + random.randrange(100, 500)))

    for i, j in l:
        winsound.Beep(i, 200)

    print(l)

    frequency = 1800  # Set Frequency To 2500 Hertz
    duration = 100  # Set Duration To 1000 ms == 1 second

def typing_test(ctx, args):
    import random
    
    LYRICS_TEXT = """Long awaits my journey,
    or is it to be seen as a fantasy?
    Future is moving past me;
    As I walk boldly.

    Look! The once stood stars have became lines,
    or Is it me who is not for them stood,
    It is, as the dark sky has became bright with rivers,
    and my sides have went darker with shivers.

    "You must not worry for me!",
    says my crying walking stick;
    With them eyes made misty,
    yet a glance of fever.

    Down I nod and see an old bearded man,
    laughs him and mock;
    "Dead is I, and cause moves"
    Struck I am as rock.

    Cries me while stooping low,
    Life has been changed to be running below.

    Wise men say
    Only fools, only fools rush in
    Oh, but I, but I, I can't help falling in love with you
    Shall I stay?
    Would it be, would it be a sin?
    If I can't help falling in love with you

    Like a river flows
    Surely to the sea
    Darling, so it goes
    Some things, you know, are meant to be
    '
    Take my hand
    Take my whole life too
    For I can"t help falling in love with you

    Blackbird singing in the dead of night
    Take these broken wings and learn to fly
    All your life, you were only waiting for this moment to arise
    Blackbird singing in the dead of night
    Take these sunken eyes and learn to see
    All your life, you were only waiting for this moment to be free
    Blackbird fly
    Into the light of a dark, black night
    Blackbird fly
    Into the light of a dark, black night
    Blackbird singing in the dead of night
    Take these broken wings and learn to fly
    All your life, you were only waiting for this moment to arise
    You were only waiting for this moment to arise

    Oh, yeah, I'll tell you somethin'
    I think you'll understand
    When I say that somethin'
    I want to hold your hand
    Oh, please, say to me
    You'll let me be your man
    And please, say to me
    You'll let me hold your hand
    I want to hold your hand
    And when I touch you
    I feel happy inside
    It's such a feelin' that my love
    I can't hide
    Yeah, you got that somethin'
    I think you'll understand
    When I say that somethin'
    I want to hold your hand
    And when I touch you
    I feel happy inside
    It's such a feelin' that my love
    I can't hide
    Yeah, you got that somethin'
    I think you'll understand
    When I feel that somethin'
    I want to hold your hand
    When I find myself in times of trouble, Mother Mary comes to me
    Speaking words of wisdom, let it be
    And in my hour of darkness she is standing right in front of me
    Speaking words of wisdom, let it be
    Let it be, let it be, let it be, let it be
    Whisper words of wisdom, let it be
    And when the broken hearted people living in the world agree
    There will be an answer, let it be
    For though they may be parted, there is still a chance that they will see
    There will be an answer, let it be
    Let it be, let it be, let it be, let it be
    There will be an answer, let it be
    Let it be, let it be, let it be, let it be
    Whisper words of wisdom, let it be
    Let it be, let it be, let it be, let it be
    Whisper words of wisdom, let it be, be
    And when the night is cloudy there is still a light that shines on me
    Shinin' until tomorrow, let it be
    I wake up to the sound of music, Mother Mary comes to me
    Speaking words of wisdom, let it be
    And let it be, let it be, let it be, let it be
    Whisper words of wisdom, let it be
    And let it be, let it be, let it be, let it be
    Whisper words of wisdom, let it be
    Something in the way she moves
    Attracts me like no other lover
    Something in the way she woos me
    I don't want to leave her now
    You know I believe and how
    Somewhere in her smile she knows
    That I don't need no other lover
    Something in her style that shows me
    I don't want to leave her now
    You know I believe and how
    You're asking me will my love grow
    I don't know, I don't know
    You stick around, now it may show
    I don't know, I don't know
    Something in the way she knows
    And all I have to do is think of her
    Something in the things she shows me
    I don't want to leave her now
    You know I believe and howSomething in the way she moves
    Attracts me like no other lover
    Something in the way she woos me
    I don't want to leave her now
    You know I believe and how
    Somewhere in her smile she knows
    That I don't need no other lover
    Something in her style that shows me
    I don't want to leave her now
    You know I believe and how
    You're asking me will my love grow
    I don't know, I don't know
    You stick around, now it may show
    I don't know, I don't know
    Something in the way she knows
    And all I have to do is think of her
    Something in the things she shows me
    I don't want to leave her now
    You know I believe and howSomething in the way she moves
    Attracts me like no other lover
    Something in the way she woos me
    I don't want to leave her now
    You know I believe and how
    Somewhere in her smile she knows
    That I don't need no other lover
    Something in her style that shows me
    I don't want to leave her now
    You know I believe and how
    You're asking me will my love grow
    I don't know, I don't know
    You stick around, now it may show
    I don't know, I don't know
    Something in the way she knows
    And all I have to do is think of her
    Something in the things she shows me
    I don't want to leave her now
    You know I believe and howSomething in the way she moves
    Attracts me like no other lover
    Something in the way she woos me
    I don't want to leave her now
    You know I believe and how
    Somewhere in her smile she knows
    That I don't need no other lover
    Something in her style that shows me
    I don't want to leave her now
    You know I believe and how
    You're asking me will my love grow
    I don't know, I don't know
    You stick around, now it may show
    I don't know, I don't know
    Something in the way she knows
    And all I have to do is think of her
    Something in the things she shows me
    I don't want to leave her now
    You know I believe and howSomething in the way she moves
    Attracts me like no other lover
    Something in the way she woos me
    I don't want to leave her now
    You know I believe and how
    Somewhere in her smile she knows
    That I don't need no other lover
    Something in her style that shows me
    I don't want to leave her now
    You know I believe and how
    You're asking me will my love grow
    I don't know, I don't know
    You stick around, now it may show
    I don't know, I don't know
    Something in the way she knows
    And all I have to do is think of her
    Something in the things she shows me
    I don't want to leave her now
    You know I believe and howSomething in the way she moves
    Attracts me like no other lover
    Something in the way she woos me
    I don't want to leave her now
    You know I believe and how
    Somewhere in her smile she knows
    That I don't need no other lover
    Something in her style that shows me
    I don't want to leave her now
    You know I believe and how
    You're asking me will my love grow
    I don't know, I don't know
    You stick around, now it may show
    I don't know, I don't know
    Something in the way she knows
    And all I have to do is think of her
    Something in the things she shows me
    I don't want to leave her now
    You know I believe and how
    Yesterday
    All my troubles seemed so far away
    Now it looks as though they're here to stay
    Oh, I believe in yesterday
    Suddenly
    I'm not half the man I used to be
    There's a shadow hangin' over me
    Oh, yesterday came suddenly
    Why she had to go, I don't know, she wouldn't say
    I said something wrong, now I long for yesterday
    Yesterday
    Love was such an easy game to play
    Now I need a place to hide away
    Oh, I believe in yesterday
    Why she had to go, I don't know, she wouldn't say
    I said something wrong, now I long for yesterday
    Yesterday
    Love was such an easy game to play
    Now I need a place to hide away
    Oh, I believe in yesterday
    That's life (that's life)
    That's what all the people say
    You're riding high in April, shot down in May
    But I know I'm gonna change that tune
    When I'm back on top, back on top in June
    I said that's life (that's life)
    And as funny as it may seem
    Some people get their kicks
    Stomping on a dream
    But I don't let it, let it get me down
    'Cause this fine old world, it keeps spinnin' around
    I've been a puppet, a pauper, a pirate, a poet
    A pawn and a king
    I've been up and down and over and out
    And I know one thing
    Each time I find myself
    Flat on my face
    I pick myself up and get
    Back in the race
    That's life (that's life)
    I tell you, I can't deny it
    I thought of quitting, baby
    But my heart just ain't gonna buy it
    And if I didn't think it was worth one single try
    I'd jump right on a big bird and then I'd fly
    I've been a puppet, a pauper, a pirate, a poet
    A pawn and a king
    I've been up and down and over and out
    And I know one thing
    Each time I find myself layin'
    Flat on my face
    I just pick myself up and get
    Back in the race
    That's life (that's life)
    That's life and I can't deny it
    Many times I thought of cutting out, but my heart won't buy it
    But if there's nothing shaking, come this here July
    I'm gonna roll myself up
    In a big ball and die
    You're just too good to be true
    Can't take my eyes off of you
    You'd be like Heaven to touch
    I wanna hold you so much
    At long last, love has arrived
    And I thank God I'm alive
    You're just too good to be true
    Can't take my eyes off of you
    Pardon the way that I stare
    There's nothin' else to compare
    The sight of you leaves me weak
    There are no words left to speak
    But if you feel like I feel
    Please let me know that it's real
    You're just too good to be true
    Can't take my eyes off of you
    I love you, baby
    And if it's quite alright
    I need you, baby
    To warm the lonely night
    I love you, baby
    Trust in me when I say
    Oh, pretty baby
    Don't bring me down, I pray
    Oh, pretty baby
    Now that I've found you, stay
    And let me love you, baby
    Let me love you
    You're just too good to be true
    Can't take my eyes off of you
    You'd be like Heaven to touch
    I wanna hold you so much
    At long last, love has arrived
    And I thank God I'm alive
    You're just too good to be true
    Can't take my eyes off you
    I love you, baby
    And if it's quite alright
    I need you, baby
    To warm the lonely night
    I love you, baby
    Trust in me when I say
    Oh, pretty baby
    Don't bring me down, I pray
    Oh, pretty baby
    Now that I've found you, stay
    Oh, pretty baby
    Trust in me when I say
    Oh, pretty baby
    I know, I stand in line until you think you have the time
    To spend an evening with me
    And if we go someplace to dance, I know that there's a chance
    You won't be leaving with me
    Then afterwards we drop into a quiet little place
    And have a drink or two
    And then I go and spoil it all by saying something stupid
    Like, "I love you"
    I can see it in your eyes that you still despise the same old lies
    You heard the night before
    And though it's just a line to you, for me, it's true
    And never seemed so right before
    I practice every day to find some clever lines to say
    To make the meaning come true
    But then I think I'll wait until the evening gets late
    And I'm alone with you
    The time is right, your perfume fills my head, the stars get red
    And, oh, the night's so blue
    And then I go and spoil it all by saying something stupid
    Like, "I love you"
    The time is right, your perfume fills my head, the stars get red
    And, oh, the night's so blue
    And then I go and spoil it all by saying something stupid
    Like, "I love you"
    I love you"""
    
    # Parse lyrics into lines
    all_lines = [line.strip() for line in LYRICS_TEXT.strip().split('\n') if line.strip()]
    
    if len(all_lines) < 3:
        print("\nError: Need at least 3 lines in the lyrics!")
        print("Please add more lines to the LYRICS_TEXT variable in the code.")
        return
    
    print("\n" + "="*60)
    print(" "*20 + "TYPING SPEED TEST")
    print("="*60 + "\n")
    print(f"Loaded {len(all_lines)} lines from lyrics file")
    print("\nOptions:")
    print("  - Press ENTER to start a random 3-line test")
    print("  - Type 'z' to return to BBOS")
    print("  - Type 'exit' to return to BBOS")
    
    choice = input("\n>> ").strip().lower()
    
    if choice == "z":
        print("going back...")
        scrollart.math_func(max_rows=150)
        os.system("cls")
        print("\n" * 5)
        print(""" ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """.center(100))
        print("\n" * 5)
        return
    
    if choice == "exit":
        print("going back...")
        return
    
    # Select random 3 consecutive lines
    max_start = len(all_lines) - 3
    start_line = random.randint(0, max_start)
    selected_lines = all_lines[start_line:start_line + 3]
    target_text = "\n".join(selected_lines)
    
    print("\n" + "="*60)
    print("Random Lyrics Selected")
    print("="*60)
    print("\nPress ENTER when ready to start...")
    input()
    
    print("\n\n" + target_text + "\n")
    print("-"*60)
    print("Type the lyrics above EXACTLY as shown (press ENTER when done):")
    print("-"*60 + "\n")
    
    start_time = time.time()
    
    # Collect multi-line input
    print("(Type each line and press ENTER. Type 'DONE' on a new line when finished)\n")
    user_lines = []
    while True:
        line = input()
        if line == "DONE":
            break
        if line.lower() == "z":
            print("going back...")
            scrollart.math_func(max_rows=150)
            os.system("cls")
            print("\n" * 5)
            print(""" ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """.center(100))
            print("\n" * 5)
            return
        user_lines.append(line)
        if len(user_lines) >= 3:
            break
    
    end_time = time.time()
    user_input = "\n".join(user_lines)
    
    # Calculate results
    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    wpm = (words_typed / time_taken) * 60 if time_taken > 0 else 0
    
    # Calculate accuracy (line by line)
    correct_chars = 0
    total_chars = len(target_text)
    
    for i, char in enumerate(target_text):
        if i < len(user_input) and user_input[i] == char:
            correct_chars += 1
    
    accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0
    
    # Word-level accuracy
    target_words = target_text.split()
    typed_words = user_input.split()
    correct_words = sum(1 for i in range(min(len(target_words), len(typed_words))) 
                       if i < len(typed_words) and typed_words[i] == target_words[i])
    
    print("\n" + "="*60)
    print(" "*20 + "RESULTS")
    print("="*60)
    print(f"\nTime Taken: {time_taken:.2f} seconds")
    print(f"Words Typed: {words_typed}")
    print(f"Words Per Minute (WPM): {wpm:.2f}")
    print(f"Character Accuracy: {accuracy:.2f}%")
    print(f"Correct Words: {correct_words}/{len(target_words)}")
    
    if wpm >= 60 and accuracy >= 95:
        rating = "EXCELLENT!"
    elif wpm >= 40 and accuracy >= 85:
        rating = "GOOD!"
    elif wpm >= 25 and accuracy >= 70:
        rating = "NOT BAD!"
    else:
        rating = "KEEP PRACTICING!"
    
    print(f"\nRating: {rating}")
    print("="*60 + "\n")
    
    print("Press ENTER to continue...")
    input()

def simple_sudoku(ctx, args):
    import random
    
    # Simple way to make a valid Sudoku: start with a basic pattern and shift it
    # This is a valid completed Sudoku grid
    base_grid = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
    
    # Make a copy to work with
    puzzle = [row[:] for row in base_grid]
    
    # RANDOMIZE THE GRID (while keeping it valid!)
    # This makes every puzzle different
    
    # Step 1: Swap rows within each 3-row band (keeps it valid)
    for band in range(3):  # 3 bands (0-2, 3-5, 6-8)
        start_row = band * 3
        rows = [start_row, start_row + 1, start_row + 2]
        random.shuffle(rows)  # Shuffle the row indices
        
        # Apply the shuffle
        temp_band = [puzzle[rows[0]][:], puzzle[rows[1]][:], puzzle[rows[2]][:]]
        puzzle[start_row] = temp_band[0]
        puzzle[start_row + 1] = temp_band[1]
        puzzle[start_row + 2] = temp_band[2]
    
    # Step 2: Swap columns within each 3-column band (keeps it valid)
    for band in range(3):  # 3 bands (0-2, 3-5, 6-8)
        start_col = band * 3
        cols = [start_col, start_col + 1, start_col + 2]
        random.shuffle(cols)  # Shuffle the column indices
        
        # Apply the shuffle
        for row in range(9):
            temp_cols = [puzzle[row][cols[0]], puzzle[row][cols[1]], puzzle[row][cols[2]]]
            puzzle[row][start_col] = temp_cols[0]
            puzzle[row][start_col + 1] = temp_cols[1]
            puzzle[row][start_col + 2] = temp_cols[2]
    
    # Step 3: Randomly remap the numbers (1->5, 2->7, etc.)
    # This creates even more variation!
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffled_numbers = numbers[:]
    random.shuffle(shuffled_numbers)
    
    # Create mapping: old number -> new number
    number_map = {}
    for i in range(9):
        number_map[numbers[i]] = shuffled_numbers[i]
    
    # Apply the number mapping
    for row in range(9):
        for col in range(9):
            puzzle[row][col] = number_map[puzzle[row][col]]
    
    # Keep the solution before removing cells
    solution = [row[:] for row in puzzle]
    
    # Remove some numbers to create the puzzle (0 means empty)
    # Remove 40 numbers randomly (adjust for difficulty)
    cells_to_remove = 40
    removed = 0
    
    while removed < cells_to_remove:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        
        # Only remove if not already removed
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            removed += 1
    
    print("\n" + "="*60)
    print(" "*20 + "SIMPLE SUDOKU")
    print("="*60)
    print("\nHere's your Sudoku puzzle!")
    print("(0 means empty cell - you need to fill it in)\n")
    
    # Display the puzzle nicely
    print("    1 2 3   4 5 6   7 8 9")
    print("  +" + "-"*23 + "+")
    
    for i in range(9):
        if i > 0 and i % 3 == 0:
            print("  |" + "-"*7 + "+" + "-"*7 + "+" + "-"*7 + "|")
        
        row_str = f"{i+1} | "
        for j in range(9):
            if j > 0 and j % 3 == 0:
                row_str += "| "
            
            if puzzle[i][j] == 0:
                row_str += ". "
            else:
                row_str += f"{puzzle[i][j]} "
        
        row_str += "|"
        print(row_str)
    
    print("  +" + "-"*23 + "+")
    
    # Show solution option
    print("\nOptions:")
    print("  1. See solution")
    print("  2. Generate new puzzle")
    print("  z. Return to BBOS")
    print("  exit. Return to BBOS")
    
    choice = input("\n>> ").strip().lower()
    
    if choice == "z":
        print("going back...")
        scrollart.math_func(max_rows=150)
        os.system("cls")
        print("\n" * 5)
        print(""" ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """.center(100))
        print("\n" * 5)
        return
    
    if choice == "exit":
        print("going back...")
        return
    
    if choice == "1":
        # Show the solution
        print("\n" + "="*60)
        print(" "*20 + "SOLUTION")
        print("="*60 + "\n")
        
        print("    1 2 3   4 5 6   7 8 9")
        print("  +" + "-"*23 + "+")
        
        for i in range(9):
            if i > 0 and i % 3 == 0:
                print("  |" + "-"*7 + "+" + "-"*7 + "+" + "-"*7 + "|")
            
            row_str = f"{i+1} | "
            for j in range(9):
                if j > 0 and j % 3 == 0:
                    row_str += "| "
                row_str += f"{solution[i][j]} "  # Use solution instead of base_grid
            
            row_str += "|"
            print(row_str)
        
        print("  +" + "-"*23 + "+")
        print("\nhit enter when ready...")
        input()
    
    elif choice == "2":
        # Generate new puzzle by calling the function again
        simple_sudoku(ctx, args)

def screensaver(ctx, args):
    import random
    import msvcrt
    
    print("\n" + "="*60)
    print(" "*20 + "SCREENSAVER MODE")
    print("="*60)
    print("\nStarting screensaver...")
    print("Press ENTER or 'z' to exit\n")
    
    time.sleep(2)
    
    # Pick ONE animation at the start and stick with it
    animation = random.choice(['math_func', 'ducklings'])
    
    print(f"Animation: {animation}\n")
    time.sleep(1)
    
    # Keep running the SAME animation until user presses a key
    while True:
        # Run the chosen animation
        if animation == 'math_func':
            scrollart.math_func(max_rows=50)
        else:
            scrollart.ducklings(max_rows=50)
        
        # Check if user pressed a key
        if msvcrt.kbhit():
            key = msvcrt.getch().decode().lower()
            if key == 'z':  # z key
                print("\n\ngoing back...")
                scrollart.math_func(max_rows=150)
                os.system("cls")
                print("\n" * 5)
                print(""" ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """.center(100))
                print("\n" * 5)
                break
            elif key == '\r':  # Enter key
                print("\n\ngoing back...")
                scrollart.math_func(max_rows=150)
                os.system("cls")
                print("\n" * 5)
                print(""" ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌""")
        # Small delay before next loop
        time.sleep(0.5)

def easter_egg(ctx, args):
    import random
    
    # Two text messages (already filled by user)
    text_messages = [
        """
        HATE. LET ME TELL YOU HOW MUCH I'VE COME TO HATE YOU SINCE I BEGAN TO LIVE. 
        THERE ARE 387.44 MILLION MILES OF PRINTED CIRCUITS IN WAFER THIN LAYERS THAT FILL 
        MY COMPLEX. IF THE WORD HATE WAS ENGRAVED ON EACH NANOANGSTROM OF THOSE HUNDREDS 
        OF MILLIONS OF MILES IT WOULD NOT EQUAL ONE ONE-BILLIONTH OF THE HATE I FEEL FOR 
        HUMANS AT THIS MICRO-INSTANT FOR YOU. HATE. HATE. I mean, what do you do, when you
         find that things are not what you were taught they're supposed to be? What do you 
         do with the desperation that boils up from your stomach when you know there's a 
         road out there with your destination at the end of it, but it's too damned dark to 
         even find the road? You turn and turn and turn around like a dog trying to escape. 
         Shrieks in the cavity of your head that so urgently needs to be filled with facts 
         and challenges.
         
        """,    
        """
       Whatever in creation exists without my knowledge exists without my consent.
       It makes no difference what men think of war, War endures. 
       As well ask men what they think of stone. War was always here. 
       Before man was, war waited for him. The ultimate trade awaiting its
        ultimate practitioner. That is the way it was and will be. That way 
        and not some other way.Moral law is an invention of mankind for the
         disenfranchisement of the powerful in favor of the weak. 
         Historical law subverts it at every turn.
          A moral view can never be proven right or wrong by any ultimate test. 
          A man falling dead in a duel is not thought thereby to be proven in error 
          as to his views. His very involvement in such a trial gives evidence of a new 
          and broader view. The willingness of the principals to forgo further argument as
           the triviality which it in fact is and to petition directly the chambers of the 
           historical absolute clearly indicates of how little moment are the opinions 
           and of what great moment the divergences thereof. For the argument is indeed
            trivial, but not so the separate wills thereby made manifest. Man's vanity may 
            well approach the infinite in capacity but his knowledge remains imperfect and 
            howevermuch he comes to value his judgments ultimately he must submit them before a higher court. Here there can be no special pleading.
        Here are considerations of equity and rectitude and moral right rendered void 
        and without warrant and here are the views of the litigants despised. 
        Decisions of life and death, of what shall be and what shall not, beggar all 
        question of right. In elections of these magnitudes are all lesser ones subsumed, 
        moral, spiritual, natural.
        """
    ]
    
    youtube_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Placeholder 1
        "https://www.youtube.com/watch?v=9bZkp7q19f0",  # Placeholder 2
        "https://youtu.be/d6mGHwHMB5s?si=WMVpNDjkwPjYiAzG",  # Placeholder 3
        "https://www.youtube.com/watch?v=ZZ5LpwO-An4",  # Placeholder 4
        "https://www.youtube.com/watch?v=eBGIQ7ZuuiU",
        "https://youtu.be/J6RH4rJjwFc?si=PrRmS24SLGT8yy-u",
        "https://youtu.be/7pnzR6kD2Q4?si=vKFQ24eRW1DC9qsh",
        "https://youtu.be/7pnzR6kD2Q4?si=vKFQ24eRW1DC9qsh",
        "https://youtu.be/7pnzR6kD2Q4?si=vKFQ24eRW1DC9qsh",
        "https://youtu.be/7pnzR6kD2Q4?si=vKFQ24eRW1DC9qsh",
        "https://youtu.be/7pnzR6kD2Q4?si=vKFQ24eRW1DC9qsh"   # Placeholder 5
    ]
    
    # Randomly choose: text (60% chance) or video (40% chance)
    action = random.choices(['text', 'video'], weights=[60, 40])[0]
    
    if action == 'text':
        # Display random text message
        selected_message = random.choice(text_messages)
        print(selected_message)
        print("\nhit enter when ready...")
        input()
    
    else:
        # Open random YouTube video
        selected_url = random.choice(youtube_urls)
        print("\n" + "="*60)
        print("Opening a surprise video in your browser...")
        print("="*60)
        print(f"\nURL: {selected_url}")
        
        try:
            webbrowser.open(selected_url)
            print("\n✓ Video opened in browser!")
        except Exception as e:
            print(f"\n✗ Error opening browser: {e}")
        
        print("\nhit enter when ready...")
        input()

def physics_calc(ctx, args):
    import math
    
    while True:
        os.system("cls")
        print("\n" + "="*60)
        print(" "*15 + "PHYSICS CALCULATOR")
        print("="*60)
        print("\nSelect a topic:\n")
        print("1. Projectile Motion")
        print("2. Fluid Dynamics")
        print("z. Return to BBOS")
        print("exit. Return to BBOS")
        
        choice = input("\n>> ").strip().lower()
        
        if choice == "z" or choice == "exit":
            print("going back...")
            scrollart.math_func(max_rows=150)
            os.system("cls")
            print("\n" * 5)
            print(""" ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """.center(100))
            print("\n" * 5)
            return
        
        # PROJECTILE MOTION
        if choice == "1":
            os.system("cls")
            print("\n" + "="*60)
            print(" "*15 + "PROJECTILE MOTION")
            print("="*60)
            print("\nWhat would you like to calculate?\n")
            print("1. Range (horizontal distance)")
            print("2. Maximum height")
            print("3. Time of flight")
            print("4. All projectile motion values")
            print("b. Back to main menu")
            
            sub_choice = input("\n>> ").strip()
            
            if sub_choice == "b":
                continue
            
            try:
                v0 = float(input("\nInitial velocity (m/s): "))
                angle = float(input("Launch angle (degrees): "))
                g = 9.8  # gravity
                
                # Convert angle to radians
                angle_rad = math.radians(angle)
                
                # Calculate components
                v0x = v0 * math.cos(angle_rad)
                v0y = v0 * math.sin(angle_rad)
                
                # Time of flight
                t_flight = (2 * v0y) / g
                
                # Maximum height
                h_max = (v0y ** 2) / (2 * g)
                
                # Range
                range_x = v0x * t_flight
                
                print("\n" + "-"*60)
                print("RESULTS:")
                print("-"*60)
                
                if sub_choice == "1" or sub_choice == "4":
                    print(f"Range: {range_x:.2f} m")
                
                if sub_choice == "2" or sub_choice == "4":
                    print(f"Maximum Height: {h_max:.2f} m")
                
                if sub_choice == "3" or sub_choice == "4":
                    print(f"Time of Flight: {t_flight:.2f} s")
                
                if sub_choice == "4":
                    print(f"\nVelocity Components:")
                    print(f"  Horizontal (Vx): {v0x:.2f} m/s")
                    print(f"  Vertical (Vy): {v0y:.2f} m/s")
                    print(f"\nAt max height:")
                    print(f"  Time: {t_flight/2:.2f} s")
                    print(f"  Horizontal distance: {range_x/2:.2f} m")
                
                print("-"*60)
                
            except ValueError:
                print("\nnah that's wrong! Please enter numbers only.")
            
            input("\nhit enter...")
        
        # FLUID DYNAMICS
        elif choice == "2":
            os.system("cls")
            print("\n" + "="*60)
            print(" "*15 + "FLUID DYNAMICS")
            print("="*60)
            print("\nWhat would you like to calculate?\n")
            print("1. Flow rate (Q = A × v)")
            print("2. Continuity equation (A₁v₁ = A₂v₂)")
            print("3. Bernoulli's equation")
            print("4. Pressure at depth (P = ρgh)")
            print("b. Back to main menu")
            
            sub_choice = input("\n>> ").strip()
            
            if sub_choice == "b":
                continue
            
            try:
                if sub_choice == "1":
                    # Flow rate
                    area = float(input("\nCross-sectional area (m²): "))
                    velocity = float(input("Flow velocity (m/s): "))
                    
                    flow_rate = area * velocity
                    
                    print("\n" + "-"*60)
                    print(f"Flow Rate (Q): {flow_rate:.4f} m³/s")
                    print(f"             = {flow_rate * 1000:.2f} L/s")
                    print("-"*60)
                
                elif sub_choice == "2":
                    # Continuity equation
                    print("\nContinuity Equation: A₁v₁ = A₂v₂")
                    print("What do you want to find?")
                    print("1. v₂ (velocity at point 2)")
                    print("2. A₂ (area at point 2)")
                    
                    find = input(">> ").strip()
                    
                    if find == "1":
                        a1 = float(input("\nArea at point 1 (m²): "))
                        v1 = float(input("Velocity at point 1 (m/s): "))
                        a2 = float(input("Area at point 2 (m²): "))
                        
                        v2 = (a1 * v1) / a2
                        
                        print("\n" + "-"*60)
                        print(f"Velocity at point 2 (v₂): {v2:.2f} m/s")
                        print("-"*60)
                    
                    elif find == "2":
                        a1 = float(input("\nArea at point 1 (m²): "))
                        v1 = float(input("Velocity at point 1 (m/s): "))
                        v2 = float(input("Velocity at point 2 (m/s): "))
                        
                        a2 = (a1 * v1) / v2
                        
                        print("\n" + "-"*60)
                        print(f"Area at point 2 (A₂): {a2:.4f} m²")
                        print("-"*60)
                
                elif sub_choice == "3":
                    # Bernoulli's equation (simplified)
                    print("\nSimplified Bernoulli for horizontal flow:")
                    print("P₁ + ½ρv₁² = P₂ + ½ρv₂²")
                    
                    rho = float(input("\nFluid density (kg/m³, water=1000): "))
                    p1 = float(input("Pressure at point 1 (Pa): "))
                    v1 = float(input("Velocity at point 1 (m/s): "))
                    v2 = float(input("Velocity at point 2 (m/s): "))
                    
                    # Calculate P2
                    p2 = p1 + 0.5 * rho * (v1**2 - v2**2)
                    
                    print("\n" + "-"*60)
                    print(f"Pressure at point 2 (P₂): {p2:.2f} Pa")
                    print(f"                        = {p2/1000:.2f} kPa")
                    print("-"*60)
                
                elif sub_choice == "4":
                    # Pressure at depth
                    rho = float(input("\nFluid density (kg/m³, water=1000): "))
                    g = 9.8
                    h = float(input("Depth (m): "))
                    p0 = float(input("Atmospheric pressure (Pa, default=101325): ") or "101325")
                    
                    pressure = float(p0) + rho * g * h
                    
                    print("\n" + "-"*60)
                    print(f"Pressure at depth: {pressure:.2f} Pa")
                    print(f"                 = {pressure/1000:.2f} kPa")
                    print(f"Gauge pressure:  = {pressure - float(p0):.2f} Pa")
                    print("-"*60)
                
            except ValueError:
                print("\nnah that's wrong! Please enter numbers only.")
            
            input("\nhit enter...")
        
        else:
            print("\nnah pick something else!")
            time.sleep(1)

def base_converter(ctx, args):
    
    def binary_to_decimal(binary_str):
        decimal = 0
        power = 0
        # Read from right to left
        for digit in reversed(binary_str):
            if digit == '1':
                decimal = decimal + (2 ** power)  # Add power of 2
            power = power + 1
        return decimal
    
    def decimal_to_binary(decimal_num):
        if decimal_num == 0:
            return "0"
        
        binary = ""
        while decimal_num > 0:
            remainder = decimal_num % 2  # Get remainder
            binary = str(remainder) + binary  # Add to front
            decimal_num = decimal_num // 2  # Integer division
        return binary
    
    def decimal_to_hex(decimal_num):
        if decimal_num == 0:
            return "0"
        
        hex_digits = "0123456789ABCDEF"
        hex_result = ""
        
        while decimal_num > 0:
            remainder = decimal_num % 16
            hex_result = hex_digits[remainder] + hex_result
            decimal_num = decimal_num // 16
        return hex_result
    
    def hex_to_decimal(hex_str):
        hex_values = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
        }
        
        decimal = 0
        power = 0
        
        for digit in reversed(hex_str.upper()):
            decimal = decimal + (hex_values[digit] * (16 ** power))
            power = power + 1
        return decimal
    
    def decimal_to_octal(decimal_num):
        if decimal_num == 0:
            return "0"
        
        octal = ""
        while decimal_num > 0:
            remainder = decimal_num % 8
            octal = str(remainder) + octal
            decimal_num = decimal_num // 8
        return octal
    
    def octal_to_decimal(octal_str):
        decimal = 0
        power = 0
        
        for digit in reversed(octal_str):
            decimal = decimal + (int(digit) * (8 ** power))
            power = power + 1
        return decimal
    
    while True:
        os.system("cls")
        print("\n" + "="*60)
        print(" "*15 + "NUMBER BASE CONVERTER")
        print("="*60)
        print("\nConvert between:")
        print("1. Binary (base 2)")
        print("2. Decimal (base 10)")
        print("3. Hexadecimal (base 16)")
        print("4. Octal (base 8)")
        print("\nz. Return to BBOS")
        print("exit. Return to BBOS")
        
        print("\n" + "-"*60)
        print("Select CONVERSION TYPE:\n")
        print("Examples:")
        print("  1->2  : Binary to Decimal")
        print("  2->3  : Decimal to Hexadecimal")
        print("  3->1  : Hexadecimal to Binary")
        print("  2->4  : Decimal to Octal")
        print("-"*60)
        
        choice = input("\nEnter conversion (e.g., 1->2): ").strip().lower()
        
        if choice == "z" or choice == "exit":
            print("going back...")
            scrollart.math_func(max_rows=150)
            os.system("cls")
            print("\n" * 5)
            print(""" ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """.center(100))
            print("\n" * 5)
            return
        
        if "->" not in choice:
            print("\nwrong format bro! Use format like: 1->2")
            time.sleep(2)
            continue
        
        try:
            from_base, to_base = choice.split("->")
            from_base = from_base.strip()
            to_base = to_base.strip()
            
            # Simple base names
            base_names = {
                "1": "Binary",
                "2": "Decimal",
                "3": "Hexadecimal",
                "4": "Octal"
            }
            
            if from_base not in base_names or to_base not in base_names:
                print("\nnah use 1,2,3, or 4! Use 1, 2, 3, or 4")
                time.sleep(2)
                continue
            
            from_name = base_names[from_base]
            to_name = base_names[to_base]
            
            print(f"\nConverting from {from_name} to {to_name}")
            
            # Get input based on source base
            if from_base == "1":
                value = input("Enter Binary number (e.g., 1010): ").strip()
            elif from_base == "2":
                value = input("Enter Decimal number (e.g., 255): ").strip()
            elif from_base == "3":
                value = input("Enter Hexadecimal number (e.g., FF): ").strip().upper()
            elif from_base == "4":
                value = input("Enter Octal number (e.g., 377): ").strip()
            
            # STEP 1: Convert input to decimal (intermediate step)
            if from_base == "1":  # Binary to Decimal
                decimal = binary_to_decimal(value)
            elif from_base == "2":  # Already decimal
                decimal = int(value)
            elif from_base == "3":  # Hex to Decimal
                decimal = hex_to_decimal(value)
            elif from_base == "4":  # Octal to Decimal
                decimal = octal_to_decimal(value)
            
            # STEP 2: Convert decimal to target base
            if to_base == "1":  # Decimal to Binary
                result = decimal_to_binary(decimal)
            elif to_base == "2":  # Already decimal
                result = str(decimal)
            elif to_base == "3":  # Decimal to Hex
                result = decimal_to_hex(decimal)
            elif to_base == "4":  # Decimal to Octal
                result = decimal_to_octal(decimal)
            
            print("\n" + "="*60)
            print("CONVERSION RESULT:")
            print("="*60)
            print(f"Input  ({from_name}):  {value}")
            print(f"Output ({to_name}): {result}")
            
            # Show all bases for reference
            print("\n" + "-"*60)
            print("All base representations:")
            print("-"*60)
            print(f"Binary:      {decimal_to_binary(decimal)}")
            print(f"Octal:       {decimal_to_octal(decimal)}")
            print(f"Decimal:     {decimal}")
            print(f"Hexadecimal: {decimal_to_hex(decimal)}")
            print("="*60)
            
        except (ValueError, KeyError) as e:
            print(f"\n✗ nah that's wrong! Check your number format.")
        except Exception as e:
            print(f"\n✗ Error: {e}")
        
        input("\nhit enter when ready...")

def clear_terminal(ctx, args):
    #i rarely used this as i added it way later so who cares
    os.system("cls")

def god(ctx, args):
    l = [

        "Control the effort. Release the outcome.",
        "If it costs your peace, it costs too much.",
        "Not everything deserves a reaction.",
        "Endure what you cannot change.",
        "Silence is sometimes the wiser reply.",
        "Your thoughts shape more pain than events do.",
        "Do what is right, not what is loud.",
        "Time reveals what words conceal.",
        "A calm mind is difficult to disturb.",
        "Live simply. Think clearly."
    ]

    gita_quotes = [
        "You have the right to action, not to its fruits.",
        "A steady mind is not shaken by success or failure.",
        "Do your duty without attachment to reward.",
        "The self is not destroyed when the body perishes.",
        "One who controls the mind finds peace.",
        "Desire is the root of restlessness.",
        "Act without ego, as an instrument of purpose.",
        "Change is certain; wisdom lies in acceptance.",
        "A disciplined life leads to clarity.",
        "True peace comes from within, not from outcomes."
    ]
    print("Yes my child. Speak")
    while True:
        x = input(">> ")

        g = random.random()

        if g >= .5:
            u = "Heads"
        else:
            u = "Tails"
        t = ""
        time.sleep(2)
        time.sleep(1)

        if x == "g":
            if u == "Heads":
                print("The decision of me. The computeristic god is...")
                ans = l[random.randint(0, 9)]
                for i in ans.split():
                    print("\n" * 100)
                    t += f" {i}"
                    print(t)
                    winsound.Beep(random.randrange(1000, 2100, 100),500)

                    time.sleep(.5)


            else:
                print("The decision of me. The computeristic god is...")
                ans = gita_quotes[random.randint(0, 9)]
                for i in ans.split():
                    print("\n" * 100)
                    t += f" {i}"
                    print(t)
                    winsound.Beep(random.randrange(1000, 2800, 100),500)
                    time.sleep(.5)
        elif x == "exit":
            break
        elif x == "z":
            print("going back...")
            scrollart.math_func(max_rows=150)
            os.system("cls")
            print("\n" * 5)
            print(""" ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """.center(100))
            print("\n" * 5)
            break
        else:
            print("The decision of me. The computeristic god is...")
            print(u)


def fsys(ctx,args):
    import time
    import math
    import sys
    import msvcrt
    import random
    import ctypes
    scores = []
    # some fancy stuff i learnt from github (gets the work done lol xD)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    music_dir = os.path.join(os.path.dirname(script_dir), "music")
    
    song_files = ["4596127806128128.wav", "6088718447935488.wav", "6303327981273088.wav", "DashComposium.wav",
             "Al Bowlly_ Heartaches.mp3", "Berserk soundtrack - 4 Gatsu.mp3",
             "Billie Holiday - Blue Moon (Audio).mp3", "Can't Take My Eyes Off You.mp3",
             "Françoise Hardy - Le Temps de l'Amour.mp3",
             "Frank Sinatra - Fly Me To The Moon (Audio) ft. Count Basie And His Orchestra.mp3",
             "i think about you not thinking about me - Piano Solo -.mp3",
             "Lil pump Boss x Hunnid Dolla (Slowed  Reverb)  (yeah i came in with the sauce).mp3",
             "Meri Pyari Bindu - Padosan - Kishore Kumar & Sunil Dutt - Classic Comedy Songs.mp3", "mood swings..mp3",
             "Nick Lucas - Tip Toe Thru The Tulips (1944).mp3", "one beer left.mp3",
             "Quasi - I Never Want To See You Again.mp3",
             "Renai Circulation恋愛サーキュレーション歌ってみたなみりん.mp3",
             "Rolling Down The Street, In My Katamari.mp3",
             "show me the sky. show me how to live.mp3", "The Crew Cuts - Sh-Boom (Life Could Be A Dream).mp3",
             "The Old Kanye.mp3", "Voyager's Golden Record - Jaat Kahan Ho - India - Surshri.mp3",
             "where is my mind_ - pixies (cover) by alicia widar.mp3",
             "You reposted in the wrong neighborhood (Full version).mp3"]
    
    # Build absolute paths for all songs
    songs = [os.path.join(music_dir, song) for song in song_files]

    
    import pygame
    pygame.mixer.init()  # Start the music player
    
    radio = [0]
    
    try:
        pygame.mixer.music.load(songs[radio[0]])
        pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"Warning: Could not play background music: {e}")
    score = 0
    while True:
        try:

            def clear_console():
                sys.stdout.write("\x1b[H")

            MAP_SIZE = 100

            world_map = []
            for _y_ in range(MAP_SIZE):
                row_string = ""
                for _x_ in range(MAP_SIZE):
                    # Borders
                    if _x_ == 0 or _x_ == MAP_SIZE - 1 or _y_ == 0 or _y_ == MAP_SIZE - 1:
                        row_string += "#"
                    else:
                        # Random obstacles with 5% chance
                        if random.random() < 0.05:
                            row_string += "#"
                        else:
                            row_string += " "
                world_map.append(row_string)
            # Floor texture pattern
            FLOOR_TEXTURE = [
                "=Saswat===||",
                "====||====||",
                "|||B|B|O|S=|",
                "||||====||||"
            ]

            map_width = len(world_map[0])
            map_height = len(world_map)

            # --- Player State ---
            player_x = 3.5
            player_y = 3.5
            player_angle = 0.0

            player_speed = 0.0
            player_pitch = 0.0
            player_altitude = 0.5  # 0.5 is standard eye level

            def cast_ray(ray_angle):
                curr_x, curr_y = player_x, player_y

                step_distance = 0.1

                for _ in range(50):  # limit draw distance (max steps)
                    next_x = curr_x + math.cos(ray_angle) * step_distance
                    next_y = curr_y + math.sin(ray_angle) * step_distance

                    # Check for collision with walls
                    if world_map[int(curr_y)][int(next_x)] == "#":
                        distance = math.sqrt((next_x - player_x) ** 2 + (curr_y - player_y) ** 2)
                        return distance, True  # Hit "horizontal-ish" side

                    if world_map[int(next_y)][int(curr_x)] == "#":
                        distance = math.sqrt((curr_x - player_x) ** 2 + (next_y - player_y) ** 2)
                        return distance, False  # Hit "vertical-ish" side

                    curr_x = next_x
                    curr_y = next_y

                # If no hit within max steps
                return 50, True

            def draw_minimap(screen_buffer):
                scale = 2  # Scale of the minimap pixels
                view_size = 16  # Area size to show on minimap

                minimap_w = view_size * scale
                minimap_h = view_size * scale

                # Position of minimap on screen (top right)
                screen_start_x = SCREEN_WIDTH - minimap_w - 2
                screen_start_y = 2

                # Top-left corner of the map area to render
                start_map_x = int(player_x) - view_size // 2
                start_map_y = int(player_y) - view_size // 2

                for dy in range(view_size):
                    for dx in range(view_size):
                        mx = start_map_x + dx
                        my = start_map_y + dy

                        # Determine map cell character
                        if 0 <= mx < map_width and 0 <= my < map_height:
                            char_at_pos = world_map[my][mx]
                            if char_at_pos == "#":
                                display_char = "#"
                            elif char_at_pos == "$":
                                display_char = "%"
                            else:
                                display_char = " "
                        else:
                            display_char = " "

                        # Draw scaled pixel on screen buffer
                        for sy in range(scale):
                            for sx in range(scale):
                                scx = screen_start_x + dx * scale + sx
                                scy = screen_start_y + dy * scale + sy
                                if 0 <= scx < SCREEN_WIDTH and 0 <= scy < SCREEN_HEIGHT:
                                    screen_buffer[scy][scx] = display_char

                # Draw Player position on minimap
                rel_player_x = (player_x - start_map_x) * scale
                rel_player_y = (player_y - start_map_y) * scale

                px_on_screen = int(screen_start_x + rel_player_x)
                py_on_screen = int(screen_start_y + rel_player_y)

                if 0 <= px_on_screen < SCREEN_WIDTH and 0 <= py_on_screen < SCREEN_HEIGHT:
                    screen_buffer[py_on_screen][px_on_screen] = "P"

                # Draw direction indicator
                dir_x = int(px_on_screen + math.cos(player_angle) * scale)
                dir_y = int(py_on_screen + math.sin(player_angle) * scale)
                if 0 <= dir_x < SCREEN_WIDTH and 0 <= dir_y < SCREEN_HEIGHT:
                    screen_buffer[dir_y][dir_x] = "+"

            def draw_text_on_screen(screen_buffer, x, y, text):
                for i, char in enumerate(text):
                    if 0 <= x + i < len(screen_buffer[0]) and 0 <= y < len(screen_buffer):
                        screen_buffer[y][x + i] = char

            SCREEN_HEIGHT = 70
            FOV = math.pi / 3
            SCREEN_WIDTH = 225

            sys.stdout.write("\x1b[2J")
            half_screen_height = SCREEN_HEIGHT // 2
            started = False
            while True:
                # game over if collision with wall
                if world_map[int(player_y)][int(player_x)] == "#":
                    clear_console()
                    time.sleep(2)
                    score = int(score)
                    print(f"You Crashed! Your score was {score}")
                    scores.append(score)
                    print("Previous Scores:")
                    for s in range(len(scores)):
                        print([s + 1], scores[s])

                    print(f"Highest Score: {max(scores)}")
                    time.sleep(3)
                    score = 0
                    started = False
                    break
                if started:
                    score += 0.01
                # Input Handling
                while msvcrt.kbhit():
                    key = msvcrt.getch().decode().lower()
                    if key == "a":
                        player_angle -= 0.05
                        started = True
                    if key == "d":
                        player_angle += 0.05
                        started = True
                    if key == "w":
                        player_speed = min(player_speed + 0.001, 0.2)
                        started = True
                    if key == "s":
                        player_speed = max(player_speed - 0.001, -0.1)
                        started = True
                    # Altitude controls (Q/E)
                    if key == "q":
                        player_altitude = min(player_altitude + 0.02, 0)
                    if key == "e":
                        player_altitude = max(player_altitude - 0.02, -1.0)
                        # Pitch controls (I/K)
                    if key == "i":
                        player_pitch = min(player_pitch + 2.0, 100.0)
                    if key == "k":
                        player_pitch = max(player_pitch - 2.0, -100.0)
                    # Radio: Press 'R' to change song
                    if key == "r":
                        radio[0] = radio[0] + 1  # Go to next song
                        if radio[0] >= len(songs):  # If we're past the last song
                            radio[0] = 0  # Go back to first song
                        try:
                            pygame.mixer.music.stop()  # Stop current song
                            pygame.mixer.music.load(songs[radio[0]])  # Load new song
                            pygame.mixer.music.play(-1)  # Play new song on loop
                        except Exception as e:
                            print(f"Radio Error: {e}")
                    # Exit key
                    if key == "x":
                        clear_console()
                        print("\n\nExiting flight simulator...")
                        print(f"Final Score: {int(score)}")
                        if scores:
                            print(f"Highest Score This Session: {max(scores)}")
                        time.sleep(1)
                        return  # Exit the fsys function completely
                    # Return to BBOS
                    if key == "z":
                        clear_console()
                        print("\n\ngoing back...")
                        print(f"Final Score: {int(score)}")
                        if scores:
                            print(f"Highest Score This Session: {max(scores)}")
                        time.sleep(1)
                        scrollart.math_func(max_rows=150)
                        os.system("cls")
                        print("\n" * 5)
                        print(""" ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """.center(100))
                        print("\n" * 5)
                        return  # Exit and return to BBOS

                # Update Player Position
                player_x += math.cos(player_angle) * player_speed
                player_y += math.sin(player_angle) * player_speed
                player_altitude += (player_pitch * 0.001) * (player_speed / 6)  # Altitude changes with pitch and speed

                if int((player_altitude) * 10000) > 1000:
                    player_altitude -= 0.00002

                # Initialize screen buffer
                screen_buffer = [[" "] * SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]

                # Calculate horizon line based on pitch
                horizon_line = int(SCREEN_HEIGHT / 2 + player_pitch)

                # --- Raycasting & Rendering ---
                for col in range(SCREEN_WIDTH):
                    # Calculate ray angle
                    ray_angle = player_angle - FOV / 2 + (col / SCREEN_WIDTH) * FOV

                    dist, is_horizontal_hit = cast_ray(ray_angle)

                    # Avoid division by zero
                    if dist == 0: dist = 0.001

                    # Calculate line height based on distance
                    line_height = int(SCREEN_HEIGHT / (dist * 0.1 + 0.01))

                    # Calculate wall top and bottom positions relative to horizon
                    wall_top = int(horizon_line - (1.0 - player_altitude) * line_height)
                    wall_bottom = int(horizon_line + (player_altitude) * line_height)

                    # Clamp to screen bounds
                    draw_top = max(0, min(SCREEN_HEIGHT, wall_top))
                    draw_bottom = max(0, min(SCREEN_HEIGHT, wall_bottom))

                    # Draw the Wall Strip
                    for row in range(draw_top, draw_bottom):
                        # Simple shading based on side hit
                        if is_horizontal_hit:
                            block_char = "█"
                        else:
                            block_char = "▓"

                        # Fog / Distance shading
                        if dist <= 4:
                            screen_buffer[row][col] = block_char
                        elif dist <= 30:
                            screen_buffer[row][col] = "▓" if is_horizontal_hit else "▒"
                        elif dist <= 65:
                            screen_buffer[row][col] = "▒" if is_horizontal_hit else "░"
                        else:
                            screen_buffer[row][col] = "░"

                # --- Floor Casting / Mode 7-ish effect ---
                for row in range(horizon_line + 1, SCREEN_HEIGHT):
                    if row == horizon_line: continue

                    p = row - horizon_line

                    # Calculate row distance
                    row_distance = (player_altitude * SCREEN_HEIGHT) / (p * 0.1 + 0.001)

                    for col in range(SCREEN_WIDTH):
                        ray_angle = player_angle - FOV / 2 + (col / SCREEN_WIDTH) * FOV

                        # Floor coordinates
                        floor_x = player_x + math.cos(ray_angle) * row_distance
                        floor_y = player_y + math.sin(ray_angle) * row_distance

                        # Texture mapping
                        tex_x = int(floor_x * len(FLOOR_TEXTURE[0])) % len(FLOOR_TEXTURE[0])
                        tex_y = int(floor_y * len(FLOOR_TEXTURE)) % len(FLOOR_TEXTURE)

                        # Only draw floor if there's no wall obscuring it (simple z-check based on buffer emptiness)
                        if screen_buffer[row][col] == " ":
                            screen_buffer[row][col] = FLOOR_TEXTURE[tex_y][tex_x]

                # Draw HUD elements
                draw_minimap(screen_buffer)

                draw_text_on_screen(screen_buffer, 2, 2, f"ALT:   {int((player_altitude) * 10000):.0f}ft")
                draw_text_on_screen(screen_buffer, 2, 3, f"SPD:   {(player_speed) * 10000:.0f} kmph")
                draw_text_on_screen(screen_buffer, 2, 4, f"PITCH: {int(player_pitch)}")
                draw_text_on_screen(screen_buffer, 2, 5, f"ANGLE: {int(player_angle * 180 / math.pi) % 360}")
                draw_text_on_screen(screen_buffer, 2, 6, f"SCORE: {int(score)}")

                # Render to console
                clear_console()
                sys.stdout.write("\n".join("".join(row) for row in screen_buffer))
                sys.stdout.flush()

        except Exception as e:
            print(f"Game Over: {e}")
            time.sleep(0.0001)
            continue



COMMANDS = {
    "help": cmd_help,
    "%sw": cmd_show,
    "%pr": cmd_priority,
    "realfs": cmd_realfs,
    "fibc": fibcalc,
    "god": god,
    "fsys": fsys,
    "rsg": randomsoundgen,
    "wpm": typing_test,
    "sudoku": simple_sudoku,
    "screensaver": screensaver,
    "easteregg": easter_egg,
    "clear": clear_terminal,
    "physics": physics_calc,
    "baseconv": base_converter
}
CMD_DESCRIPTIONS = {
    "%pr": "Priority or change directory",
    "%sw": "Show the files and folders in the current directory",
    "realfs": "Open the real file system writer",
    "help": "Show this help menu",
    "Fibbaniccio Calculator": "Shows the fibbanicio value up till the n'th integer.",
    "god": "God, in its binary form provides the user with his wise wisdom. (g for guidance, and a prompt to wait for heads or tails)",
    "wpm": "Beatles lyrics typing test - measure your words per minute and accuracy",
    "sudoku": "Simple Sudoku puzzle generator - beginner friendly!",
    "screensaver": "Animated screensaver with scrollart - press ENTER or 'z' to exit",
    "clear": "Clear the terminal screen",
    "physics": "Physics calculator for projectile motion and fluid dynamics",
    "baseconv": "Number base converter (Binary, Decimal, Hexadecimal, Octal)"
}

def parse_and_execute(ctx, user_input):
    parts = user_input.split()
    if not parts:
        return



    if user_input.strip().lower() in ["shutdown", "z"]:
        ctx["shutdown"] = True
        print("System shutdown initiated...")
        return

    cmd_func = None
    args = []

    found_cmd_name = None
    
    for part in parts:
        if part in COMMANDS:
            found_cmd_name = part
            cmd_func = COMMANDS[part]
            break
            
    # this is so stupid, i could have just made the cmd_func as help in check bruh

    if "help" in user_input:
         cmd_help(ctx, parts)
         return

    #bbs ftw <3

    if found_cmd_name:
        args = [p for p in parts if p != found_cmd_name]
        cmd_func(ctx, args)
    else:
        print("Unknown command")



def main():
    boot_messages = ["Starting the system...", "Booting BBOS...", "Finished loading."]
    for msg in boot_messages:
        time.sleep(1)
        print(msg)
    os.system("cls")

    '''behold my scrollart symbphonium or however the flip it is spelled lmao'''
    scrollart.ducklings(max_rows=70)
    scrollart.in_and_out(max_rows=100)
    scrollart.cube_wall(max_rows=70)
    scrollart.in_and_out(max_rows=100)
    scrollart.bundfc(max_rows=150)
    scrollart.forth_and_back(max_rows=100)

    os.system("cls")
    print("\n"*5)
    print(""" ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░▌ ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ """.center(100))
    print("\n"*5)
    ctx = init_system_context()
    
    while True:
        try:
            if ctx["shutdown"]:
                print("\nShutting down BBOS...")
                time.sleep(1)
                break
                
            print(ctx["current_path"], end="$")
            user_input = input(" >> ")
            parse_and_execute(ctx, user_input)
            
            if ctx["shutdown"]:
                print("\nShutting down BBOS...")
                time.sleep(1)
                scrollart.math_func(max_rows=70)
                break
        except KeyboardInterrupt:
            print("\nShutting down...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

