class Square{
  Point topLeft;
  Point topRight;
  Point bottomLeft;
  Point bottomRight;
  
  Square(Point tl, Point tr, Point bl, Point br){
    topLeft = tl;
    topRight = tr;
    bottomLeft = bl;
    bottomRight = br;
  }
  
  void display(){
    l(topLeft, topRight);
    l(topRight, bottomRight);
    l(topLeft, bottomLeft);
    l(bottomLeft, bottomRight);
  }
  
  void l(Point a, Point b){
    stroke(a.c);
    line(a.x, a.y, b.x, b.y);
  }
  
}