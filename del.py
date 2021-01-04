#import java.util.Vector;

class MemoryEater:
  Vector v = new Vector()
    while (true)
      byte b[] = new byte[1048576]
      v.add(b)
      Runtime rt = Runtime.getRuntime()
      print( "free memory: " + rt.freeMemory())