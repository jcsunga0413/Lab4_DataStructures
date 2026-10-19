# Task 4: Student Identity

LAST_NAME = "Sunga"
STUDENT_ID = "TUPM-26-1215"
FAVORITE_ARTIST = "The Neighbourhood"

# Derive computational parameters
seed_digit = int(STUDENT_ID[-1])
id_checksum = sum(
    int(d) for d in STUDENT_ID if d.isdigit()
)
vector_dim = len(LAST_NAME)

# Store the system configuration
sys_config = {
    "operator": LAST_NAME,
    "auth_id": STUDENT_ID,
    "favorite_artist": FAVORITE_ARTIST,
    "base_seed": seed_digit,
    "checksum": id_checksum,
    "vector_dim": vector_dim,
    "status": "INITIALIZED"
}

# Display system configuration
print("=== SYSTEM CONFIGURATION ===")

for key, value in sys_config.items():
    print(f"{key.upper()}: {value}")



# TASK 5: Dynamic List Operations

base_val = sys_config["base_seed"]
number_sequence = [
    base_val,
    base_val + 15,
    sys_config["checksum"]
]

print(f"\nInitial Sequence: {number_sequence}")

number_sequence.append(base_val + 20)
print(f"After Append: {number_sequence}")

