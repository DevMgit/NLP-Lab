import nltk
import random
from nltk.corpus import framenet as fn

# Download (run once)
nltk.download('framenet_v17')

frames = list(fn.frames())

print("Total Frames Available:", len(frames))

# Display 10 random frame names
print("\n--- Random Frame Names ---")
random_frames = random.sample(frames, 10)

for f in random_frames:
    print("-", f.name)

# User input
user_input = input(
    "\nEnter a frame name from above: "
).strip()

# Display details
try:
    frame = fn.frame(user_input)

    print("\n--- Frame Details ---")
    print("Frame Name:", frame.name)
    print("Definition:", frame.definition)

    print("\nFrame Elements:")
    for fe in frame.FE:
        print("-", fe)

    print("\nLexical Units:")
    for lu in frame.lexUnit:
        print("-", lu)

except:
    print(
        "\nInvalid frame name! Please run again "
        "and choose from the list."
    )
