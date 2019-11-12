# code execuation related functions

import subprocess
import lldb
import os

STD_PATH = '/home/sd/code/c/'
STD_FILENAME = 'source.c'
STD_EXE = 'a.out'


def create_source_file(src):
    f = open(STD_PATH + STD_FILENAME, 'w')
    f.write(src)
    f.close()


def compile():
    proc = subprocess.run(['clang', '-g', STD_PATH + STD_FILENAME, '-o', STD_PATH + STD_EXE], capture_output=True)
    return proc.stderr, proc.stdout


def get_program_output():
    proc = subprocess.run([STD_PATH + STD_EXE], capture_output=True)
    return proc.stderr, proc.stdout

def load_in_lldb():
    # Path to executable
    exe = STD_PATH + STD_EXE

    # debugger instance
    debugger = lldb.SBDebugger.Create()
    debugger.SetAsync(False)

    target = debugger.CreateTargetWithFileAndArch(exe, lldb.LLDB_ARCH_DEFAULT)

    if target:
        # set a breakpoint at main
        main_bp = target.BreakpointCreateByName(
            "main", target.GetExecutable().GetFilename())

        print (main_bp)
