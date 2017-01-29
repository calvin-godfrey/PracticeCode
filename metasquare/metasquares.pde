Point[][] points;
int clicks = 0;
ArrayList<Square> squares;
int blue = 0;
int red = 0;

void setup(){
  size(800, 1000); 
  frameRate(60);
  points = new Point[10][10];
  squares = new ArrayList<Square>();
  for(int r=0;r<points.length;r++){
    for(int c=0;c<points[0].length;c++){
        points[r][c] = new Point(80*r+40, 80*c+40);
    }
  }
}

void draw(){
   background(255);
   for(int i=0;i<squares.size();i++){
     squares.get(i).display();
   }
   stroke(155);
   for(int r=0;r<points.length;r++){
       for(int c=0;c<points[0].length;c++){
         Point point = points[r][c];
         fill(point.c);
         ellipse(point.x, point.y, point.radius, point.radius);
       }
   }
   fill(0);
   textSize(20);
   text("blue: " + blue, 50, 850);
   text("red: " + red, 50, 900);
}

void mousePressed(){
   boolean finished = false;
   for(int r=0;r<points.length&&!finished;r++){
      for(int c=0;c<points[0].length&&!finished;c++){
        Point point = points[r][c];
        if(point.isUsed)continue;
        if(sqrt(sq(mouseX-point.x)+sq(mouseY-point.y))<point.radius/2){
          finished = true;
          point.isUsed = true;
          if(clicks%2==0)point.c = #0000FF;
          else{point.c = #FF0000;}
          clicks++;
          checkSquares();
        }
      }
   }
}

void checkSquares(){
  for(int topX=0;topX<points.length-1;topX++){
    for(int topY=0;topY<points[0].length-1;topY++){
      for(int deltaY=0;deltaY<points.length;deltaY++){
        for(int deltaX=0;deltaX<points[0].length;deltaX++){
          Point topLeft = points[topY][topX];
          color match = topLeft.c;
          if(topX+deltaX>=points[0].length||topY+deltaX+deltaY>=points.length)break;
          if(topLeft.c==155||topY+deltaY>=points.length||topX-deltaY<0||topY+deltaX>=points.length||topX+deltaX-deltaY>=points[0].length||topX+deltaX-deltaY<0)continue;
          Point topRight = points[topY+deltaY][topX+deltaX];
          if(topRight.c!=match)continue;
          Point bottomLeft = points[topY+deltaX][topX-deltaY];
          if(bottomLeft.c!=match)continue;
          Point bottomRight = points[topY+deltaX+deltaY][topX+deltaX-deltaY];
          if(bottomRight.c!=match)continue;
          if(!bottomLeft.isUsed||!bottomRight.isUsed||!topRight.isUsed||!topLeft.isUsed)continue;
          Square sq = new Square(topLeft, topRight, bottomLeft, bottomRight);
          boolean inArray = false;
          for(int i=0;i<squares.size();i++){
            inArray = false;
            Square s = squares.get(i);
            if(s.topLeft.isEqual(sq.topLeft)&&s.topRight.isEqual(sq.topRight)&&s.bottomLeft.isEqual(sq.bottomLeft)&&s.bottomRight.isEqual(sq.bottomRight)){
              inArray = true;
              break;
            }
          }
          if(inArray)continue;
          squares.add(sq);
          float sum = (sq(deltaX)+sq(deltaY));
          if((deltaX==1&&deltaY==0)||(deltaY==0&&deltaY==1)) sum = sum/2; //Shouldn't have to do this but oh well
          if(match==#FF0000)red += sum;
          else{blue += sum;}
          if((sq(deltaX)+sq(deltaY))==2)System.out.println(deltaX+"\t"+deltaY);
        }
      }
    }
  }
}