NUM_ENEMIES = 700

# Generate individual enemy instantiations
enemy_decls = [f"E{i} = EnemyTemplate({i});" for i in range(NUM_ENEMIES)]

# Generate system line
system_parts = [f"E{i}" for i in range(NUM_ENEMIES)]
system_parts += ["Monitor", "ClockTick1", "Basic1", "Cannon1", "Cannon2", "Cannon3", "Cannon4", "Sniper1", "Sniper2"]
system_line = "system " + ", ".join(system_parts) + ";"

# Combine everything
output = "\n".join(enemy_decls + ["", system_line])

# Optionally write to a file
with open("enemy_system_declarations_700.txt", "w") as f:
    f.write(output)

print(output)

