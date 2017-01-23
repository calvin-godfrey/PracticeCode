window.onload = function(){
  var canvas = document.getElementById("canvas");
  canvas.width = screen.width;
  canvas.height = screen.height;
  var RADIUS = 200;
  var X_CENTER = canvas.width/2;
  var Y_CENTER = canvas.height/2;
  var INNER_RADIUS = RADIUS/2;
  var ctx = canvas.getContext("2d");

  Point = function(x, y, angle, life){
    this.x = x;
    this.y = y;
    this.angle = angle;
    this.life = life;
  }

  Point.prototype.calcPoint = function(){
    this.x = 200*Math.cos(this.life);
    this.y = 0;
    this.life = this.life + Math.PI/72;
    this.farX = this.x*1.5;
  }

  Point.prototype.draw = function(){
    ctx.save();
    ctx.translate(X_CENTER, Y_CENTER);
    ctx.rotate(this.angle);
    ctx.beginPath();
    ctx.arc(this.x, this.y, 5, 0, Math.PI*2);
    ctx.strokeStyle = "#000";
    ctx.stroke();
    ctx.fillStyle = "#000";
    ctx.fill();
    ctx.restore();
  }

  function drawBackground(){
    ctx.fillStyle = "#FFF";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
    ctx.arc(X_CENTER, Y_CENTER, RADIUS, 0, Math.PI*2);
    ctx.strokeStyle = "#F00";
    ctx.stroke();
  }

  function drawLine(){
    ctx.save();
    ctx.translate(X_CENTER, Y_CENTER);
    ctx.rotate(points[0].angle);
    ctx.beginPath();
    ctx.moveTo(points[0].farX, points[0].x);
    ctx.lineWidth = 2;
    ctx.strokeStyle = "#0FF";
    ctx.restore();
    ctx.save();
    ctx.translate(X_CENTER, Y_CENTER);
    ctx.rotate(points[4].angle);
    ctx.lineTo(points[4].x, points[4].y);
    ctx.stroke();
    ctx.restore();
  }

  var points = [];
  for(var i=0;i<8;i++){
    points.push(new Point(X_CENTER, Y_CENTER, i*Math.PI/8, 12.964*i)); //Legit last one is a magic number. Now clue why it is what it is
  }

  function loop(){
    drawBackground();
    for(var i=0;i<points.length;i++){
      points[i].calcPoint();
      points[i].draw();
    }
    drawLine();
    requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);

}
