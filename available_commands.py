commands_list = """
JOINT{I} { "magnitude": <value> } - Moves joint I by the specified magnitude where positive means 'FORWARD' and negative means 'BACKWARD'.
PICKUP { "object": "cube" | "cylinder" | "prism" } - Picks up the specified object.
DROP {} - Releases the currently held object.
STACK { "object": "<object_name>" } - Stacks the given object on another.
MOVE { "direction": ["F", "B", "R", "L"], "magnitude": <value> } - Moves the arm in the given direction(s) by the specified magnitude.
MOVEINPATH { "path": "square" | "circle" } - Moves the robotic arm along the specified path shape.
MOVETOCOORDINATES { "object": "<object_name>", "coordinates": [x, y, z] } - Moves the specified object to the given (x, y, z) coordinates.
### **Response Format:**
You must **strictly** return a string formatted as a JSON object:
```json
{ "reply": "<your AI-style response>", "commands": [[<command_name>, <param>]] } ```
reply: A natural language response acknowledging the command.
commands: A list of lists, where each sublist contains a command name and its parameters. If no command is detected, return [[ "NONE", "{}" ]].
"""

sidebar_commands_list = """
## Welcome to the A.R.M. Voice Assistant!

Here are the commands you can give to control the robotic arm:

### 1. **JOINT{I}** 
- **What to say:** "Move joint [I] forward [magnitude]" or "Move joint [I] backward [magnitude]"
- **Example:** "Move joint 1 forward by 5 units" or "Move joint 2 backward by 3 units"

### 2. **PICKUP** 
- **What to say:** "Pick up [object type]"
- **Example:** "Pick up the cuboid" or "Pick up the cylinder"

### 3. **DROP**
- **What to say:** "Drop the object"
- **Example:** "Drop the object"

### 4. **STACK**
- **What to say:** "Stack the [object name] on top"
- **Example:** "Stack the cuboid on top of the cylinder"

### 5. **MOVE**
- **What to say:** "Move the arm [direction] [magnitude]"
- **Example:** "Move the arm forward by 10 units" or "Move the arm left by 5 units"
  - **Directions:** "F" for forward, "B" for backward, "L" for left, "R" for right

### You can also ask me for help or request status updates like:
- "How is the arm doing?"
- "Tell me the current position of the arm."

---

**Simply speak one of the above commands to control the robotic arm!**
"""
"""
## 🤖 Voice Commands for Controlling the Robotic Arm

You can speak the following commands to control the robotic arm:

### 1. **Move a Joint**
- **What to say:** "Move joint [I] forward [magnitude]" or "Move joint [I] backward [magnitude]"
- **Example:** "Move joint 1 forward by 5 units"  
- **Syntax:** `JOINT{I} { "direction": "F" | "B", "magnitude": <value> }`  
  - Moves joint **I** forward ("F") or backward ("B") by the specified magnitude.

### 2. **Pick Up an Object**
- **What to say:** "Pick up [object type]"
- **Example:** "Pick up the cube"  
- **Syntax:** `PICKUP { "object": "cube" | "cylinder" | "prism" }`  
  - Picks up the specified object.

### 3. **Drop an Object**
- **What to say:** "Drop the object"
- **Example:** "Drop it"  
- **Syntax:** `DROP {}`  
  - Releases the currently held object.

### 4. **Stack an Object**
- **What to say:** "Stack the [object name] on top"
- **Example:** "Stack the cube on top of the cylinder"  
- **Syntax:** `STACK { "object": "<object_name>" }`  
  - Stacks the given object on another.

### 5. **Move the Arm**
- **What to say:** "Move the arm [direction] [magnitude]"
- **Example:** "Move the arm forward by 10 units"  
- **Syntax:** `MOVE { "direction": ["F", "B", "R", "L"], "magnitude": <value> }`  
  - Moves the arm **forward (F), backward (B), right (R), or left (L)** by the specified magnitude.

---

### 6. **Move in a Path**
- **What to say:** "Move in a [square/circle] path"
- **Example:** "Move in a circle"  
- **Syntax:** `MOVEINPATH { "path": "square" | "circle" }`  
  - Moves the arm in the specified **predefined path** (square or circle).

### 7. **Move to Specific Coordinates**
- **What to say:** "Move [object] to coordinates [x, y, z]"
- **Example:** "Move the cube to coordinates 3, 5, 7"  
- **Syntax:** `MOVETOCOORDINATES { "object": "<object_name>", "coordinates": [x, y, z] }`  
  - Moves the specified object to the given **x, y, z** coordinates.

---

**Simply speak one of the above commands, and the robotic arm will execute your instructions!** 🎙️
"""