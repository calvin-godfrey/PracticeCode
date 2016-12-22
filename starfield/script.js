window.onload = function(){
  var c = document.getElementById("canvas");
  var ctx = c.getContext("2d");
  var width = c.width;
  var height = c.height;
  var SHIFT = 3;
  var MAX_DIST = Math.sqrt(Math.pow(width/2,2)+Math.pow(height/2,2));
  ctx.fillStyle="#000";
  ctx.fillRect(0,0,width,height);
  ctx.beginPath();

  pointArray = [];

  var point = function(){
    this.x = width/2;
    this.prevX = this.x;
    this.y = height/2;
    this.prevY = this.y;
    this.angle = Math.random()*2*Math.PI;
  };

  point.prototype.getDistance = function(){
    return Math.sqrt(Math.pow(width/2-this.x,2)+Math.pow(height/2-this.y,2));
  };

  point.prototype.getOldDistance = function(){
    return Math.sqrt(Math.pow(width/2-this.prevX,2)+Math.pow(height/2-this.prevY,2));
  };

  point.prototype.draw = function(){
    var radius = 5*(this.getOldDistance()/MAX_DIST);
    ctx.arc(this.preV, this.prevY, radius, 0, Math.PI*2);
    ctx.fillStyle = "#000";
    ctx.fill();
    ctx.strokeStyle = "#000";
    ctx.stroke();
    if(this.x>0 && this.x<width && this.y>0 && this.y < height)
    {
      var radius = 1*(this.getDistance()/MAX_DIST);
      ctx.arc(this.x, this.y, radius, 0, Math.PI*2);
      ctx.fillStyle = "#FFF";
      ctx.fill();
      ctx.strokeStyle = "#FFF";
      ctx.stroke();
      return true;
    }
    else{
      return false;
    }
  };

  point.prototype.shift = function(){
      this.x += Math.cos(this.angle)*SHIFT;
      this.y += Math.sin(this.angle)*SHIFT;
  };

  function addPoint(){
    pointArray.push(new point());
    pointArray[pointArray.length-1].draw();
  };

  for(var i=0;i<1;i++){
    pointArray.push(new point());
    pointArray[i].draw();
  }

  var loop = window.setInterval(function(){
    for(var i=0;i<pointArray.length;i++){
      var current = pointArray[i];
      current.shift();
      if(current.draw()==false){
        pointArray.pop(i);
        i--;
        addPoint();
      }
    }
  }, 16);
};
