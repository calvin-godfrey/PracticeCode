class Point{
  float x;
  float y;
  color c;
  int radius;
  boolean isUsed;
  
  Point(float x_, float y_){
     x = x_;
     y = y_;
     c = 155; //Grayish thing
     isUsed = false;
     radius = 40;
  }
  
  boolean isEqual(Point other){
    return (x==other.x&&y==other.y&&c==other.c&&isUsed==other.isUsed);
  }
}