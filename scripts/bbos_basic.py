import os
import time

def init_system_context():

    return {
        "mdic": {
            "/": {
                "home": {
                    "notes.txt": " "
                },
                "tmp": {},
                "logs": {}
            }
        },
        "current_path": "/",
        "shutdown": False,
        "gnlin":{1: "BBOS stands for Basic Build Operating software \n",
            2: "Entirety of this os is built through sheer python. \n",
            3: "The developer is Saswat Dash \n",
            4: "The order of a command is not sufficed. User may write '%pr home' or 'home %pr' \n",
            5: "This basic software doesn't utilize text files and hence it uses strings. \n",
            6: "It has all the utilities that may make the life easier ;) \n"
        }
    }

def get_current_dir_content(ctx):

    if ctx["current_path"] == "/":
        return ctx["mdic"]["/"]
    else:
        if ctx["current_path"] in ctx["mdic"]["/"]:
            return ctx["mdic"]["/"][ctx["current_path"]]
        return {}
    
def cmd_help(ctx,args):

    print("Choose: \n", "Cmds \n", "General info (gnlin) =")
    t = input(">> ")

    if t == "Cmds" or t == "cmds":
        print("available programs/commands:", ", ".join(COMMANDS.keys()))
    else:
        for val in ctx["gnlin"].values():
            print(val)

def cmd_show(ctx, args):

    content = get_current_dir_content(ctx)
    print(list(content.keys()))

def cmd_priority(ctx, args):

    target  = None
    if len(args) > 0:
        target = args[0]

    if not target:
        ctx["current_path"] = "/"
        return
    if target in ctx["mdic"]["/"].keys():
        ctx["current_path"] = target
    else:
        print("Directory not found..")

def cmd_realfs(ctx, args):
    """Open real file system."""
    print("Launching Real File System...")
    harambe.run_file_system()

COMMANDS = {
    "help": cmd_help,
    "%sw" : cmd_show,
    "%pr": cmd_priority,
    "realfs": cmd_realfs}

def parse_and_execute(ctx, user_input):
    parts = user_input.split()

    if not parts:
        return
    

    if user_input.strip().lower() in ["shutdown", "z"]:
        ctx["shutdown"] = True
        print("System shutdown initiated..")
        return
    cmd_func = None
    found_cmd_name = None

    for part in parts:
        if part in COMMANDS:
            found_cmd_name = part
            cmd_func = COMMANDS[part]
            break
    if "help" in user_input:
        cmd_help(ctx, parts)
        return
    if found_cmd_name:
        args = [p for p in parts if p!= found_cmd_name]
        cmd_func(ctx, args)
    else:
        print("Unknown command")
def main():
    print("Booting BBOS CORE...")
    time.sleep(1)

    ctx = init_system_context()

    while True:
        try:
            print(ctx["current_path"], end="$")
            user_input = input(">> ")

            if user_input.lower() in ["exit", "shutdown"]:
                print("Shutting down...")
                break

            parse_and_execute(ctx,user_input)

            if ctx["shutdown"]:
                print("\n Shutting down BBOS...")
                time.sleep(1)
                
                break
        except KeyboardInterrupt:
            print("\n Force Shutting down...")
            break
        except Exception as e:
            print(f"an error occured: {e}")
if __name__ == "__main__":
    main()