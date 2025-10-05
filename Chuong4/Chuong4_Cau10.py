import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

shapes = [
    """
       *  
       * *  
       * * *
 * * * * * * * 
 * * *
 * *
 *
""",
    """
       *  
       * *  
       *   *
 * * * * * * * 
 *   *
 * *
 *
""",
    """
      * * * *
      * * *
      * *
      *
    * * 
  * * * 
* * * * 
""",

""""
      * * * *
      *   *
      * *
      *
    * * 
  *   * 
* * * * 
""",
]

# In từng hình sau mỗi 5 giây
for shape in shapes:
    clear()
    print(shape)
    time.sleep(5)