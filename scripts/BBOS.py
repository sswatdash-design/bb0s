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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
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
            clear_screen()
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

    frequency = 1800
    duration = 100
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
        clear_screen()
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
    

    print("(Type each line and press ENTER. Type 'DONE' on a new line when finished)\n")
    user_lines = []
    while True:
        line = input()
        if line == "DONE":
            break
        if line.lower() == "z":
            print("going back...")
            scrollart.math_func(max_rows=150)
            clear_screen()
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
    

    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    wpm = (words_typed / time_taken) * 60 if time_taken > 0 else 0

    correct_chars = 0
    total_chars = len(target_text)
    
    for i, char in enumerate(target_text):
        if i < len(user_input) and user_input[i] == char:
            correct_chars += 1
    
    accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0
    

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

def screensaver(ctx, args):
    import random
    import msvcrt
    
    print("\n" + "="*60)
    print(" "*20 + "SCREENSAVER MODE")
    print("="*60)

    print("\nStarting screensaver...")

    print("Press ENTER or 'z' to exit\n")
    
    time.sleep(2)
 
    animation = random.choice(['math_func', 'ducklings'])
    
    print(f"Animation: {animation}\n")

    time.sleep(1)

    while True:
        if animation == 'math_func':
            scrollart.math_func(max_rows=50)
        else:
            scrollart.ducklings(max_rows=50)
        

        if msvcrt.kbhit():
            key = msvcrt.getch().decode().lower()
            if key == 'z':
                print("\n\ngoing back...")
                scrollart.math_func(max_rows=150)
                clear_screen()
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
            elif key == '\r': 
                print("\n\ngoing back...")
                scrollart.math_func(max_rows=150)
                clear_screen()
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
    
        time.sleep(0.5)

def easter_egg(ctx, args):
    import random
    
  
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
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ", 
        "https://www.youtube.com/watch?v=9bZkp7q19f0",  
        "https://youtu.be/d6mGHwHMB5s?si=WMVpNDjkwPjYiAzG",  
        "https://www.youtube.com/watch?v=ZZ5LpwO-An4",  
        "https://www.youtube.com/watch?v=eBGIQ7ZuuiU",
        "https://youtu.be/J6RH4rJjwFc?si=PrRmS24SLGT8yy-u",
        "https://youtu.be/7pnzR6kD2Q4?si=vKFQ24eRW1DC9qsh",
        "https://youtu.be/7pnzR6kD2Q4?si=vKFQ24eRW1DC9qsh",
        "https://youtu.be/7pnzR6kD2Q4?si=vKFQ24eRW1DC9qsh",
        "https://youtu.be/7pnzR6kD2Q4?si=vKFQ24eRW1DC9qsh",
        "https://youtu.be/7pnzR6kD2Q4?si=vKFQ24eRW1DC9qsh"   
    ]
    

    action = random.choices(['text', 'video'], weights=[60, 40])[0]
    
    if action == 'text':

        selected_message = random.choice(text_messages)
        print(selected_message)
        print("\nhit enter when ready...")
        input()
    
    else:

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
        clear_screen()
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
            clear_screen()


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
        

        if choice == "1":
            clear_screen()
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
                g = 9.8 
                

                angle_rad = math.radians(angle)
                v0x = v0 * math.cos(angle_rad)
                v0y = v0 * math.sin(angle_rad)
                

                t_flight = (2 * v0y) / g
                

                h_max = (v0y ** 2) / (2 * g)
                

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
        

        elif choice == "2":
            clear_screen()
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

                    print("\nSimplified Bernoulli for horizontal flow:")
                    print("P₁ + ½ρv₁² = P₂ + ½ρv₂²")
                    
                    rho = float(input("\nFluid density (kg/m³, water=1000): "))
                    p1 = float(input("Pressure at point 1 (Pa): "))
                    v1 = float(input("Velocity at point 1 (m/s): "))
                    v2 = float(input("Velocity at point 2 (m/s): "))
                    

                    p2 = p1 + 0.5 * rho * (v1**2 - v2**2)
                    
                    print("\n" + "-"*60)
                    print(f"Pressure at point 2 (P₂): {p2:.2f} Pa")
                    print(f"                        = {p2/1000:.2f} kPa")
                    print("-"*60)
                
                elif sub_choice == "4":

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
    #ty shaswat
    
    def b2d(A: str):
        y, ans, temp, l1 = 2, 0, 0, []
        for j in range(len(A)):
            l1.append(y ** j)
        for k in range(len(A) - 1, -1, -1):
            ans += int(A[k]) * l1[temp]
            temp += 1
        return ans

    def o2d(A: str):
        y, ans, temp, l1 = 8, 0, 0, []
        for j in range(len(A)):
            l1.append(y ** j)
        for k in range(len(A) - 1, -1, -1):
            ans += int(A[k]) * l1[temp]
            temp += 1
        return ans

    def h2d(A: str):
        y, temp, ans, l1 = 16, 0, 0, []
        d = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
        for j in range(len(A)):
            l1.append(y ** j)
        for k in range(len(A) - 1, -1, -1):
            if A[k].isalpha():
                ans += d[A[k].upper()] * l1[temp]
            else:
                ans += int(A[k]) * l1[temp]
            temp += 1
        return ans

    def d2b(n):
        z, l = 2, []
        while n >= 1:
            l.append(n % z)
            n //= z
        out = ""
        for i in range(len(l) - 1, -1, -1):
            out += str(l[i])
        return out

    def d2o(n):
        z, l = 8, []
        while n >= 1:
            l.append(n % z)
            n //= z
        out = ""
        for i in range(len(l) - 1, -1, -1):
            out += str(l[i])
        return out

    def d2h(n):
        z, l, o = 16, [], ""
        while n >= 1:
            l.append(n % z)
            n //= z
        d2 = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        for i in range(len(l) - 1, -1, -1):
            o += d2[l[i]] if l[i] >= 10 else str(l[i])
        return o

    # Main loop
    while True:
        clear_screen()

        print("BC program")
        base = input("enter base (b/o/d/h): ").lower()
        num = input("enter number: ")

        if base == "b":
            d = b2d(num)
        elif base == "o":
            d = o2d(num)
        elif base == "h":
            d = h2d(num)

        elif base == "d":
            d = int(num)
        elif base == "z" or base == "exit":
            print("going back...")
            scrollart.math_func(max_rows=150)
            clear_screen()
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
        else:
            print("Invalid base")
            continue

        print("decimal:", d)
        print("binary:", d2b(d))
        print("octal:", d2o(d))
        print("hexadecimal:", d2h(d))
        
        input("\nhit enter when ready...")

def clear_terminal(ctx, args):
    #i rarely used this as i added it way later so who cares
    clear_screen()

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
            clear_screen()
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
    #used to look wayy better with the good ai written variable names and structures. unfortunately sir didn't allow it, so. :)
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
    pygame.mixer.init()  
    
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
                        # ranm obstcles with 5% chance
                        if random.random() < 0.05:
                            row_string += "#"
                        else:
                            row_string += " "
                world_map.append(row_string)
            # ftp
            FLOOR_TEXTURE = [
                "=Saswat===||",
                "====||====||",
                "|||B|B|O|S=|",
                "||||====||||"
            ]

            map_width = len(world_map[0])
            map_height = len(world_map)

            # currnt state of the player
            player_x = 3.5
            player_y = 3.5
            player_angle = 0.0

            player_speed = 0.0
            player_pitch = 0.0
            player_altitude = 0.5  # 0.5 is standard eye level (ty wikipedia <3)

            def cast_ray(ray_angle):
                curr_x, curr_y = player_x, player_y

                step_distance = 0.1

                for _ in range(50):  # limit draw distance (max steps)
                    next_x = curr_x + math.cos(ray_angle) * step_distance
                    next_y = curr_y + math.sin(ray_angle) * step_distance

                    # check collision
                    if world_map[int(curr_y)][int(next_x)] == "#":
                        distance = math.sqrt((next_x - player_x) ** 2 + (curr_y - player_y) ** 2)
                        return distance, True  #horizontlish hit

                    if world_map[int(next_y)][int(curr_x)] == "#":
                        distance = math.sqrt((curr_x - player_x) ** 2 + (next_y - player_y) ** 2)
                        return distance, False  # verticalish hit

                    curr_x = next_x
                    curr_y = next_y

                # no hit then return the max steps lol
                return 50, True

            def draw_minimap(screen_buffer):
                scale = 2  
                view_size = 16  
                minimap_w = view_size * scale
                minimap_h = view_size * scale

                screen_start_x = SCREEN_WIDTH - minimap_w - 2
                screen_start_y = 2

                start_map_x = int(player_x) - view_size // 2
                start_map_y = int(player_y) - view_size // 2

                for dy in range(view_size):
                    for dx in range(view_size):
                        mx = start_map_x + dx
                        my = start_map_y + dy

                        
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

                       
                        for sy in range(scale):
                            for sx in range(scale):
                                scx = screen_start_x + dx * scale + sx
                                scy = screen_start_y + dy * scale + sy
                                if 0 <= scx < SCREEN_WIDTH and 0 <= scy < SCREEN_HEIGHT:
                                    screen_buffer[scy][scx] = display_char

               
                rel_player_x = (player_x - start_map_x) * scale
                rel_player_y = (player_y - start_map_y) * scale

                px_on_screen = int(screen_start_x + rel_player_x)
                py_on_screen = int(screen_start_y + rel_player_y)

                if 0 <= px_on_screen < SCREEN_WIDTH and 0 <= py_on_screen < SCREEN_HEIGHT:
                    screen_buffer[py_on_screen][px_on_screen] = "P"

                
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
                # input handling with mscvcrt
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
                    
                    if key == "q":
                        player_altitude = min(player_altitude + 0.02, 0)
                    if key == "e":
                        player_altitude = max(player_altitude - 0.02, -1.0)
                        
                    if key == "i":
                        player_pitch = min(player_pitch + 2.0, 100.0)
                    if key == "k":
                        player_pitch = max(player_pitch - 2.0, -100.0)
                   
                    if key == "r":
                        radio[0] = radio[0] + 1  # next song
                        if radio[0] >= len(songs):  # if last song then loops abck
                            radio[0] = 0  
                        try:
                            pygame.mixer.music.stop()  
                            pygame.mixer.music.load(songs[radio[0]]) 
                            pygame.mixer.music.play(-1) 
                        except Exception as e:
                            print(f"Radio Error: {e}")
                
                    if key == "x":
                        clear_console()
                        print("\n\nExiting flight simulator...")
                        print(f"Final Score: {int(score)}")
                        if scores:
                            print(f"Highest Score This Session: {max(scores)}")
                        time.sleep(1)
                        return  # Exit the fsys function completely
                   
                    if key == "z":
                        clear_console()
                        print("\n\ngoing back...")
                        print(f"Final Score: {int(score)}")
                        if scores:
                            print(f"Highest Score This Session: {max(scores)}")
                        time.sleep(1)
                        scrollart.math_func(max_rows=150)
                        clear_screen()
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

                
                player_x += math.cos(player_angle) * player_speed

                player_y += math.sin(player_angle) * player_speed

                player_altitude += (player_pitch * 0.001) * (player_speed / 6)  

                if int((player_altitude) * 10000) > 1000:
                    player_altitude -= 0.00002

                # ily if u are reading this
                screen_buffer = [[" "] * SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]

                # calcs the horizntl line based on pitch
                horizon_line = int(SCREEN_HEIGHT / 2 + player_pitch)

                # raycasting
                for col in range(SCREEN_WIDTH):
                    #the ray angle
                    ray_angle = player_angle - FOV / 2 + (col / SCREEN_WIDTH) * FOV

                    dist, is_horizontal_hit = cast_ray(ray_angle)

                    # this one line avoids the division by zero error which had bugged me for a day
                    if dist == 0: dist = 0.001

                    # the distance between the player and the wall provides the height of the wall
                    line_height = int(SCREEN_HEIGHT / (dist * 0.1 + 0.01))

                    # gives back the top and bottom of the wall wrt the player
                    wall_top = int(horizon_line - (1.0 - player_altitude) * line_height)
                    wall_bottom = int(horizon_line + (player_altitude) * line_height)

                    # if the terminal is a grid then this bounds the clamps of the corner
                    draw_top = max(0, min(SCREEN_HEIGHT, wall_top))
                    draw_bottom = max(0, min(SCREEN_HEIGHT, wall_bottom))

                    # inspired by the doom (gives the // texture to walls)
                    for row in range(draw_top, draw_bottom):
                        
                        if is_horizontal_hit:
                            block_char = "█"
                        else:
                            block_char = "▓"

                        # fog shading
                        if dist <= 4:
                            screen_buffer[row][col] = block_char
                        elif dist <= 30:
                            screen_buffer[row][col] = "▓" if is_horizontal_hit else "▒"
                        elif dist <= 65:
                            screen_buffer[row][col] = "▒" if is_horizontal_hit else "░"
                        else:
                            screen_buffer[row][col] = "░"

                #floor csating
                for row in range(horizon_line + 1, SCREEN_HEIGHT):
                    if row == horizon_line: continue

                    p = row - horizon_line

            
                    row_distance = (player_altitude * SCREEN_HEIGHT) / (p * 0.1 + 0.001)

                    for col in range(SCREEN_WIDTH):
                        ray_angle = player_angle - FOV / 2 + (col / SCREEN_WIDTH) * FOV

                        #the floor coords
                        floor_x = player_x + math.cos(ray_angle) * row_distance
                        floor_y = player_y + math.sin(ray_angle) * row_distance

                        #texture mapping (pls dont ask me about this i just read it online and have l;itle idea )
                        tex_x = int(floor_x * len(FLOOR_TEXTURE[0])) % len(FLOOR_TEXTURE[0])
                        tex_y = int(floor_y * len(FLOOR_TEXTURE)) % len(FLOOR_TEXTURE)

                        # draws the floor if no wall is between
                        if screen_buffer[row][col] == " ":
                            screen_buffer[row][col] = FLOOR_TEXTURE[tex_y][tex_x]

                # mc like hud elmnts
                draw_minimap(screen_buffer)

                draw_text_on_screen(screen_buffer, 2, 2, f"ALT:   {int((player_altitude) * 10000):.0f}ft")
                draw_text_on_screen(screen_buffer, 2, 3, f"SPD:   {(player_speed) * 10000:.0f} kmph")
                draw_text_on_screen(screen_buffer, 2, 4, f"PITCH: {int(player_pitch)}")
                draw_text_on_screen(screen_buffer, 2, 5, f"ANGLE: {int(player_angle * 180 / math.pi) % 360}")
                draw_text_on_screen(screen_buffer, 2, 6, f"SCORE: {int(score)}")

                # shows the casting in the terminal baby!
                clear_console()
                sys.stdout.write("\n".join("".join(row) for row in screen_buffer))
                sys.stdout.flush()

        except Exception as e:
            print(f"Game Over: {e}")
            time.sleep(0.0001)
            continue

def akpr(ctx, args):
    import shutil
    import math
    import time

    while True:
        size = shutil.get_terminal_size()
        WIDTH = size.columns
        HEIGHT = size.lines


        x = WIDTH // 2
        y = HEIGHT - 3

        vy_input = input("Initial upward velocity (or z/exit to return): ")
        if vy_input.lower() in ['z', 'exit']:
            print("going back...")
            scrollart.math_func(max_rows=150)
            clear_screen()


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

        vy = float(vy_input)


        g = 0.3
        k = 0.02         
        scale = 20        
        dt = 0.2

        rocket = [
            "  ^  ",
            " ### ",
            "#^#^#",
            " ### ",
            "  #  ",
            "  #  ",
            "|||||"
        ]

        height = []
        trail = []

        while True:

        
            screen = []
            for j in range(HEIGHT):
                row = []
                for i in range(WIDTH):
                    row.append(' ')
                screen.append(row)

        
            altitude = HEIGHT - y

            
            density = math.exp(-altitude / scale)
            drag = -k * vy * abs(vy) * density

            print("Density:", round(density, 4), " Drag:", round(drag, 4))

            ay = g + drag

            vy = vy + ay * dt

            y = y + vy * dt

            trail.append(y)
            if len(trail) > 40:
                trail.pop(0)

            for i in range(WIDTH):
                screen[HEIGHT-1][i] = '-'

            for ty in trail:
                iy = int(ty)
                if 0 <= iy < HEIGHT:
                    screen[iy][x-2] = '.'#
            
            #for rocket
            for ry in range(len(rocket)):
                for rx in range(len(rocket[0])):
                    ch = rocket[ry][rx]
                    if ch != ' ':
                        py = iy + ry - 2
                        px = x + rx -4
                        if 0 <= px < WIDTH and 0 <= py < HEIGHT:
                            screen[py][px] = ch

            for row in screen:
                for c in row:
                    print(c, end='')
                print()

            print("height:", round(altitude,2), "velocity:", round(vy,2))

            height.append(altitude)


            if y >= HEIGHT-4:
                print("LANDED")
                print("MAX HEIGHT REACHED:", round(max(height),2))
                break
        
            time.sleep(0.05)


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
    "screensaver": screensaver,
    "easteregg": easter_egg,
    "clear": clear_terminal,
    "physics": physics_calc,
    "baseconv": base_converter,
    "akpr": akpr
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
    "baseconv": "Number base converter (Binary, Decimal, Hexadecimal, Octal)",
    "akpr": "Rocket simulation with atmospheric drag and gravity physics"
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
    clear_screen()

    '''behold my scrollart symbphonium or however the flip it is spelled lmao'''
    scrollart.ducklings(max_rows=70)
    scrollart.in_and_out(max_rows=100)
    scrollart.cube_wall(max_rows=70)
    scrollart.in_and_out(max_rows=100)
    scrollart.bundfc(max_rows=150)
    scrollart.forth_and_back(max_rows=100)

    clear_screen()
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
