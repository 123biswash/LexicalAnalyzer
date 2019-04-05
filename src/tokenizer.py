#!/usr/bin/env python2


import sys
import collections

Config = collections.namedtuple("Config", ("nfa_program", "input"))

Instruction = collections.namedtuple("Instruction", ("op", "a", "b"))
MATCH = (lambda: Instruction("MATCH", None, None))
JMP = (lambda a: Instruction("JMP", int(a), None))
CHAR = (lambda a,b: Instruction("CHAR", int(a), int(b)))
SPLIT = (lambda a,b: Instruction("SPLIT", int(a), int(b)))



def parse_nfa_program(string):
    lines = string.strip().split("\n")
    instructions = list()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(" ")
        if len(parts) < 2:
              pass
        instruction_index = int(parts[0])
        opcode = str(parts[1])
        if instruction_index != len(instructions):
            pass
        if opcode == "CHAR":
            instruction=CHAR(parts[2], parts[3])
            instructions.append(instruction)
        elif opcode == "JMP":
            instruction=JMP(parts[2])
            instructions.append(instruction)
        elif opcode == "SPLIT":
            instruction=SPLIT(parts[2], parts[3])
            instructions.append(instruction)
        elif opcode == "MATCH":
            instructions.append(MATCH())
        
    return instructions


def tokenize(config):

    program = parse_nfa_program(config.nfa_program)

    lexer_engine(program, config.input)
    
    return 0

def lexer_engine(program, string):
    
    cqueue = set()
    clist = []
    nlist = []
    nqueue = set()
    match_pc = -1
    match_tc = -1
    start_tc = 0
    success = 0
    matches = list()
    clist.append(0)
    cqueue.add(0)
    tc = 0
    while tc <= len(string):
        while clist:
            pc = clist.pop(0)
            inst = program[pc]
            if inst.op == 'CHAR':
                if tc < len(string) and ord(string[tc]) >= inst.a and ord(string[tc]) <= inst.b:
                    if pc+1 not in nqueue:
                        nqueue.add(pc+1)
                        nlist.append(pc+1)
            elif inst.op == 'MATCH':
                if match_tc < tc:
                    match_pc = pc
                    match_tc = tc
                elif match_pc>pc:
                    match_pc = pc
                    match_tc = tc
                else:
                    pass
            elif inst.op == 'JMP':
                if inst.a not in cqueue:
                    clist.append(inst.a)
                    cqueue.add(inst.a)
            elif inst.op == 'SPLIT':
                if inst.a not in cqueue:
                    clist.append(inst.a)
                    cqueue.add(inst.a)
                if inst.b not in cqueue:
                    clist.append(inst.b)
                    cqueue.add(inst.b)
            else:
                pass
        cqueue, nqueue = nqueue, set()
        clist, nlist = nlist, clist
        if not cqueue and match_pc != -1:
            printString=string[start_tc:match_tc]
            printPc=match_pc
            printStr=repr(printString)
            printStr=printStr.strip("'")
            print('%d:"%s"' % (printPc,printStr))
            clist.append(0)
            cqueue.add(0)
            start_tc = tc
            match_pc = -1
            tc -= 1
        tc += 1
    if match_tc == len(string):
        success = 1
        return matches
    else:
        success = 0
        return "lexing failure"
       
         
                
                
            
    
    