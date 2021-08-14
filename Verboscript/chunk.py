# script that will deal with manipulating chunks of bytecode

# fetch any inbuilt python functions

# fetch our code
from OpCodes import OpCodes

# global variables

# initialise an empty chunk
def initChunk():
    return list()

# write a byte to a chunk
def writeChunk(chunk, byte):
    chunk.append(byte)

# completely empty a chunk
def freeChunk(chunk):
    # while there are elements in the list
    while len(chunk) > 0:
        # remove the last
        chunk.pop()

# add a constant and its bytecode to the stack
def addConstant(constant):
    # write the constant opcode
    write("OP_CONSTANT")
    # and write the constant value
    write(constant)
