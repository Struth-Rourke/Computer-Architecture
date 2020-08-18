"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # ram holds 256 bytes of memory
        self.ram = [0] * 256
        # holding 8 general-purpose registers
        self.reg = [0] * 8
        # program counter (pc)
        self.pc = 0
        # stack pointer (sp)
        self.sp = 7
        # CPU running
        self.running = True


    def ram_read(self, address):
        # return the ram at the specified, indexed address
        return self.ram[address]


    # defining a function to overwrite the ram value at the given address
    def ram_write(self, value, address):
        # set the ram at the specified, indexed address, as the value
        self.ram[address] = value


    def load(self):
        """Load a program into memory."""
        # instantiate address counter
        address = 0
        # open the file (f) as read ('r')
        with open(filename, 'r') as f:
            # loop through the lines in f
            for line in f:
                # set the variable line as a list of values on #, and stripped
                line = line.split("#")[0].strip()
                # if the line is blank
                if line == '':
                    # continue
                    continue
                # set the ram at the specified, indexed address, as the int of
                # line 
                self.ram[address] = int(line, 2)
                # increment the address by one to move to the next line and ram
                # spot
                address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""


    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()


    def run(self):
        """Run the CPU."""
        