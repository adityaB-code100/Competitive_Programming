def interpreter(program):
    ram = [0] * 1000
    reg = [0] * 10

    # Load program
    for i in range(len(program)):
        ram[i] = int(program[i]) % 1000

    pc = 0
    count = 0

    while True:
        pc = pc % 1000   

        instr = ram[pc]
        count += 1

        op = instr // 100
        d = (instr // 10) % 10
        s = instr % 10

        pc += 1

        if op == 1:
            break

        elif op == 2:
            reg[d] = s % 1000

        elif op == 3:
            reg[d] = (reg[d] + s) % 1000

        elif op == 4:
            reg[d] = (reg[d] * s) % 1000

        elif op == 5:
            reg[d] = reg[s] % 1000

        elif op == 6:
            reg[d] = (reg[d] + reg[s]) % 1000

        elif op == 7:
            reg[d] = (reg[d] * reg[s]) % 1000

        elif op == 8:
            reg[d] = ram[reg[s] % 1000] % 1000

        elif op == 9:
            ram[reg[s] % 1000] = reg[d] % 1000

        elif op == 0:
            if reg[s] != 0:
                pc = reg[d] % 1000

    return count


# Test input
program = [
    "299",
    "492",
    "495",
    "399",
    "283",
    "279",
    "689",
    "078",
    "100"
]

print(interpreter(program))