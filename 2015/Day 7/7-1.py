# The most difficult challenge so far. Surprisingly, my iterative solution works pretty fast!

import re

with open("2015/Day 7/input.txt") as f:
    instructions = f.readlines()
    ignored = [False for instruction in instructions]

    # Create a dictionary that holds all wires and their signals
    # Go through instructions, skipping those which have insufficient information for the arguments
    # The ones that can be connected, ignore the instructions in the future
    # Continue until there are no further instructions

    wires = dict()

    binary_pattern = r"([a-z\d]+) [A-Z]+ ([a-z\d]+) -> ([a-z\d]+)"
    NOT_pattern = r"NOT ([a-z]+) -> ([a-z]+)"
    assignment_pattern = r"^([a-z\d]+) -> ([a-z]+)"

    finished = False
    while not finished:
        finished = True
        for i in range(len(instructions)):
            if ignored[i] == True:
                continue
            finished = False
            instruction = instructions[i]

            # Determine which of the 6 instructions it is
            match = None
            if "AND" in instruction:
                # Numerical arguments are only ever the first, and if they are, they're "1"
                match = re.match(binary_pattern, instruction)
                arg1 = None
                arg2 = None

                source2 = match.groups()[1]
                if source2 not in wires:
                    continue
                else:
                    arg2 = wires[source2]
                source1 = match.groups()[0]
                if source1.isnumeric():
                    arg1 = int(source1)
                elif source1 not in wires:
                    continue
                else:
                    arg1 = wires[source1]

                assignto = match.groups()[2]
                wires[assignto] = arg1 & arg2
                # Ignore instruction in future
                ignored[i] = True

            elif "OR" in instruction:
                # OR only takes named wires as arguments
                match = re.match(binary_pattern, instruction)
                arg1 = None
                arg2 = None

                source2 = match.groups()[1]
                if source2 not in wires:
                    continue
                else:
                    arg2 = wires[source2]
                source1 = match.groups()[0]
                if source1 not in wires:
                    continue
                else:
                    arg1 = wires[source1]

                assignto = match.groups()[2]
                wires[assignto] = arg1 | arg2
                # Ignore instruction in future
                ignored[i] = True
                
            elif "NOT" in instruction:
                match = re.match(NOT_pattern, instruction)
                arg = None

                source = match.groups()[0]
                if source not in wires:
                    continue
                else:
                    arg = wires[source]
                
                assignto = match.groups()[1]
                wires[assignto] = ~arg
                # Ignore instruction in future
                ignored[i] = True

            elif "RSHIFT" in instruction:
                # The SHIFTs always take a wire and a signal, in that order
                match = re.match(binary_pattern, instruction)
                arg1 = None
                arg2 = int(match.groups()[1])

                source1 = match.groups()[0]
                if source1 not in wires:
                    continue
                else:
                    arg1 = wires[source1]

                assignto = match.groups()[2]
                wires[assignto] = arg1 >> arg2
                # Ignore instruction in future
                ignored[i] = True

            elif "LSHIFT" in instruction:
                # The SHIFTs always take a wire and a signal, in that order
                match = re.match(binary_pattern, instruction)
                arg1 = None
                arg2 = int(match.groups()[1])

                source1 = match.groups()[0]
                if source1 not in wires:
                    continue
                else:
                    arg1 = wires[source1]

                assignto = match.groups()[2]
                wires[assignto] = arg1 << arg2
                # Ignore instruction in future
                ignored[i] = True

            else: # Simple assignment [->]
                # Can be an assignment of a numerical literal or a wire
                match = re.match(assignment_pattern, instruction)
                arg = None

                source = match.groups()[0]
                if source.isnumeric():
                    arg = int(source)
                elif source not in wires:
                    continue
                else:
                    arg = wires[source]

                assignto = match.groups()[1]
                wires[assignto] = arg
                # Ignore instruction in future
                ignored[i] = True

    output = wires["a"]
    print(f"Ultimately, wire a's signal is {output}")