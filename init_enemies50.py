NUM_CIRCLES = 30
NUM_SQUARES = 20
NUM_ENEMIES = NUM_CIRCLES + NUM_SQUARES

hp = [10]*NUM_CIRCLES + [20]*NUM_SQUARES
dmg = [2]*NUM_CIRCLES + [4]*NUM_SQUARES
speed = [1]*NUM_CIRCLES + [3]*NUM_SQUARES

def array_to_init(name, values):
    lines = []
    lines.append(f"int {name}[{len(values)}] = {{")
    for i in range(0, len(values), 10):
        lines.append("  " + ", ".join(map(str, values[i:i+10])) + ",")
    lines[-1] = lines[-1].rstrip(',')  # remove comma from last line
    lines.append("};")
    return "\n".join(lines)

# Array initializations
print(array_to_init("hp", hp))
print()
print(array_to_init("dmg", dmg))
print()
print(array_to_init("speed", speed))
print()

# Enemy template instantiations
for i in range(NUM_ENEMIES):
    print(f"E{i} = EnemyTemplate({i});")

print()

# System line
enemy_instances = ", ".join([f"E{i}" for i in range(NUM_ENEMIES)])
system_line = f"system {enemy_instances}, Monitor, ClockTick1, Basic1, Cannon1, Cannon3, Cannon4, Sniper1, Sniper2;"
print(system_line)

