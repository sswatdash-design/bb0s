import os
import filewsys
import time
import sys
import random
import winsound
import math
import scrollart

sys.set_int_max_str_digits(100000000)
# System Context Initialization
def init_system_context():
    """Initialize and return the system state dictionary."""
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
        "shutdown": False,  # Global shutdown flag
        "gnlin": {
            1: "BBOS stands for Basic Build Operating software \n",
            2: "Entirety of this os is built through sheer python. \n",
            3: "The developer is Saswat Dash \n",
            4: "The order of a command is not sufficed. User may write '%pr home' or 'home %pr' \n",
            5: "This basic software doesn't utilize text files and hence it uses strings, which have been called 'Dash file' \n",
            6: "It has all the utilities that may make the life easier ;) \n",
            7: "Press 'Z' key in any program or type 'shutdown' to exit the system \n"
        }
    }

def get_current_dir_content(ctx):
    """Retrieve content of the current directory from the context."""
    if ctx["current_path"] == "/":
        return ctx["mdic"]["/"]
    else:
        # Check if current_path is a valid key in root
        if ctx["current_path"] in ctx["mdic"]["/"]:
             return ctx["mdic"]["/"][ctx["current_path"]]
        return {}

# Command Functions
def cmd_help(ctx, args):
    """Show help menu."""
    print("Choose: \n","Cmds \n","General Info (gnlin)")
    t = input(">> ")
    if t == "Cmds":
        print("Available programs/commands:", ", ".join(COMMANDS.keys()))
    else:
        for val in ctx["gnlin"].values():
            print(val)

def cmd_show(ctx, args):
    """Show files (%sw)."""
    content = get_current_dir_content(ctx)
    print(list(content.keys()))

def cmd_priority(ctx, args):
    """Change directory (%pr)."""
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
    """Open real file system."""
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

        print("If you want to stop type 's' or 'z' to shutdown system..")

        choice = input("?? ")
        if choice == "s":
            break
        elif choice == "z":
            ctx["shutdown"] = True
            print("System shutdown initiated...")
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
            ctx["shutdown"] = True
            print("System shutdown initiated...")
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
    # Get the directory where the script is located, then go up one level to find music folder
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

    # Play background music
    # SND_ASYNC: play in background
    # SND_LOOP: loop continuously
    # Play music using MCI (Media Control Interface) for MP3 support
    # This avoids external dependencies like playsound or pygame
    def play_music(file_path):
        # Enclose in quotes to handle spaces in filenames
        alias = "mp3player"
        cmd_close = f'close {alias}'
        cmd_open = f'open "{file_path}" type mpegvideo alias {alias}'
        cmd_play = f'play {alias} repeat'

        # Close any currently playing file
        ctypes.windll.winmm.mciSendStringW(cmd_close, None, 0, None)
        # Open the new file
        error = ctypes.windll.winmm.mciSendStringW(cmd_open, None, 0, None)
        if error:
            print(f"Error opening file: {error}")
            return
        # Play
        ctypes.windll.winmm.mciSendStringW(cmd_play, None, 0, None)

    current_song_index = 0
    try:
        play_music(songs[current_song_index])
    except Exception as e:
        print(f"Warning: Could not play background music: {e}")
    score = 0
    while True:
        try:

            def clear_console():
                """Clears the console screen."""
                sys.stdout.write("\x1b[H")

            # --- Constants & Configuration ---
            MAP_SIZE = 100

            # --- Map Generation ---
            # creating a simple map with borders and random obstacles
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
                """
                Casts a ray from player position at the given angle.
                Returns:
                    distance (float): Distance to the wall hit
                    hit_horizontal (bool): True if it hit a horizontal wall (or close enough distinction for shading)
                """
                curr_x, curr_y = player_x, player_y

                # Ray marching step size
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
                """Draws a minimap overlay on the screen buffer."""
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
                """Helper to draw text onto the 2D character buffer."""
                for i, char in enumerate(text):
                    if 0 <= x + i < len(screen_buffer[0]) and 0 <= y < len(screen_buffer):
                        screen_buffer[y][x + i] = char

            # --- Screen Settings ---
            SCREEN_HEIGHT = 70
            FOV = math.pi / 3
            SCREEN_WIDTH = 225

            sys.stdout.write("\x1b[2J")  # Clear entire screen initially
            half_screen_height = SCREEN_HEIGHT // 2
            started = False
            # --- Main Loop ---
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
                    # Radio controls
                    if key == "r":
                        # Cycle to the next song
                        current_song_index = (current_song_index + 1) % len(songs)
                        try:
                            play_music(songs[current_song_index])
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
                    # Shutdown system key
                    if key == "z":
                        ctx["shutdown"] = True
                        clear_console()
                        print("\n\nSystem shutdown initiated...")
                        print(f"Final Score: {int(score)}")
                        if scores:
                            print(f"Highest Score This Session: {max(scores)}")
                        time.sleep(1)
                        return  # Exit and trigger system shutdown

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

# Registry of commands
# Key: Command string
# Value: Function to execute
COMMANDS = {
    "help": cmd_help,
    "%sw": cmd_show,
    "%pr": cmd_priority,
    "realfs": cmd_realfs,
    "fibc": fibcalc,
    "god": god,
    "fsys": fsys,
    "rsg": randomsoundgen
}

# Add description strings for help
CMD_DESCRIPTIONS = {
    "%pr": "Priority or change directory",
    "%sw": "Show the files and folders in the current directory",
    "realfs": "Open the real file system writer",
    "help": "Show this help menu",
    "Fibbaniccio Calculator": "Shows the fibbanicio value up till the n'th integer.",
    "god": "God, in its binary form provides the user with his wise wisdom. (g for guidance, and a prompt to wait for heads or tails)"
}

def parse_and_execute(ctx, user_input):
    parts = user_input.split()
    if not parts:
        return

    # Check for shutdown command
    if user_input.strip().lower() in ["shutdown", "z"]:
        ctx["shutdown"] = True
        print("System shutdown initiated...")
        return

    # Try to find a command in the input
    cmd_func = None
    args = []

    found_cmd_name = None
    
    for part in parts:
        if part in COMMANDS:
            found_cmd_name = part
            cmd_func = COMMANDS[part]
            break
            
    # If help check (contains "help")
    if "help" in user_input:
         cmd_help(ctx, parts)
         return

    if found_cmd_name:
        # Remove the command from args
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
    # Initialize context as a dictionary
    ctx = init_system_context()
    
    while True:
        try:
            # Check shutdown flag
            if ctx["shutdown"]:
                print("\nShutting down BBOS...")
                time.sleep(1)
                break
                
            print(ctx["current_path"], end="$")
            user_input = input(" >> ")
            parse_and_execute(ctx, user_input)
            
            # Check shutdown flag after command execution
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
