### **multC** is a simple python script that allow the Linux/Windows users mantain a small history of clipboard contents and access all the contents simple by shortkeys.

**The usual way is:**
  1. User copy contents from a source using *ctrl+c* shortkey.
  2. User navigate to destiny place.
  3. User paste content using *ctrl+v* shortkey.
  4. User repeat steps 1-3 to each new new content.

**The new way proposed is:**
  1. User copy all at once needed contents using *ctrl+c* (one copy action for each new content).
  2. User navigate to destiny place 
  3. User paste all at once needed contents using *ctrl+v*(changing the current clipboard content by *alt+<1-9>* shortkeys).

**The script work by monitoring pressed keys in keyboard:**
  * When is detected the use of *ctrl+c* shortkey the content of clipboard is storaged in a list (lenght of 9). 
  * When is detected the use of *alt+<1-9>* shortkey the current content of clipboard is changed according the position in list (1-9). At this moment the user can paste (ctrl+v) the selected content.
  * When is detected the use of *alt+delete* shortkey the current content of clipboard and list is erased.

**PS1:** The script only works with textual contents in clipboard.
**PS2:** When the user copies more than 9 contents, the oldest content is deleted and the new one is added at the end of the list, only the 9 most recent contents are preserved.
