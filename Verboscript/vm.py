# this will house the virtual machine that executes bytecode

# fetch any inbuilt python functions
import operator as op

# fetch our code
from chunk import *
from common import *
from debug import *

# Global variables
interpretResult = {"INTERPRET_OK",
                   "INTERPRET_COMPILE_ERROR",
                   "INTERPRET_RUNTIME_ERROR",
                   }

# define the virtual machine class
class VM:
    def __init__(self):
        # store the current chunk to work on
        self.chunk = Chunk()
        # the instruction pointer
        self.ip = 0
        # and the stack
        self.stack = list()


# function to read the current byte, and increase the instruction pointer
def readByte():
    # increment the instruction pointer
    vm.ip += 1
    # and return the previous byte
    return vm.chunk.code[vm.ip - 1]

# function to read a constant
def readConstant():
    # fetch the constant id, and return the constant at that point
    return vm.chunk.constants.values[readByte()]

# function for binary operations
def BINARY_OP(op):
    # fetch the two operands (in reverse order because stack)
    b = pop()
    a = pop()
    # and push the operation result, using the op function
    push(op(a, b))

# function to run a chunk
def run():
    #continue looping
    while True:
        # check if we are debugging stuff
        if DEBUG_TRACE_EXECUTION:
            # print a large empty slot
            printn(" "*10)
            # iterate through and print the stack
            for x in vm.stack:
                printn("[ {} ]".format(x))
            # and show a default print
            print()
            # and disasemble each instruction
            disasembleInstruction(vm.chunk, vm.ip)
        # fetch the instruction
        instruct = readByte()
        # check the byte type is a valid opcode
        if instruct in OpCodes:
            if instruct == "OP_CONSTANT":
                # fetch the constant
                const = readConstant()
                # push the value to the stack
                push(const)
            elif instruct == "OP_ADD":
                # do the binary operation with addition
                BINARY_OP(op.add)
            elif instruct == "OP_SUBTRACT":
                # do the binary operation with addition
                BINARY_OP(op.sub)
            elif instruct == "OP_MULTIPLY":
                # do the binary operation with addition
                BINARY_OP(op.mul)
            elif instruct == "OP_DIVIDE":
                # do the binary operation with addition
                BINARY_OP(op.truediv)
            elif instruct == "OP_NEGATE":
                # fetch the value on top of the stack, negate it, and push it back
                push(-pop())
            elif instruct == "OP_RETURN":
                # show whatever is on top of the stack for now
                print(pop())
                # and return an interpret okay message
                return "INTERPRET_OK"

# interpret a chunk using the virtual machine
def interpret(chunk):
    # set the chunk that the vm will work on
    vm.chunk = chunk
    # set the instruction pointer back to zero
    vm.ip = 0
    # and return the execution
    return run()

# push to the stack
def push(value):
    vm.stack.append(value)

# and pop from the stack
def pop():
    return vm.stack.pop()

# and create the virtual machine
vm = VM()
