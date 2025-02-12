commands_list = """
JOINT{I} { "magnitude": <value> } - Moves joint I by the specified magnitude where positive/plus means 'FORWARD' and negative/minus means 'BACKWARD'.
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