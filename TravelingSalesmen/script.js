window.onload = function(){
  var canvas = document.getElementById("canvas");
  var points = document.getElementById("getPoints");
  var minDistance = 1e20;
  var bestWay = [];
  canvas.width = screen.width;
  canvas.height = screen.height;
  var ctx = canvas.getContext('2d');

  Point = function(){
    this.x = Math.random()*canvas.width;
    this.y = Math.random()*canvas.height;
    this.radius = 6;
  };

  Point.prototype.draw = function(){
    ctx.beginPath();
    ctx.moveTo(this.x, this.y);
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI*2);
    ctx.strokeStyle = "#ddd";
    ctx.stroke();
    ctx.fillStyle = "#ddd";
    ctx.fill();
  };

  Point.prototype.line = function(other){
    ctx.beginPath();
    ctx.moveTo(this.x, this.y);
    ctx.strokeStyle = "#ddd";
    ctx.strokeWidth = 4;
    ctx.lineTo(other.x, other.y);
    ctx.stroke();
  }

  Point.prototype.getDistance = function(other){
    return Math.sqrt(Math.pow(this.x-other.x,2)+Math.pow(this.y-other.y,2));
  };

  function factorial(n){
    return n>1?n*factorial(n-1):1;
  };

  function drawBackground(){
    ctx.fillStyle = "#000";
    ctx.fillRect(0,0,canvas.width,canvas.height);
    for(var i=0;i<pointList.length;i++){
      pointList[i].draw();
    };
  };

  function calcDistance(){
    var ans = 0;
    for(var i=1;i<pointList.length;i++){
      ans+=pointList[i].getDistance(pointList[i-1]);
    };
    return ans;
  };

  function drawLines(){
    for(var i=1;i<bestWay.length;i++){
      bestWay[i].line(bestWay[i-1]);
    }
  }

  var pointList = [];

  function animate(){
    drawBackground();
    drawLines();
    //Do math here
    requestAnimationFrame(animate);
  }

  points.addEventListener('mousedown', function(event){
    for(var i=0;i<document.getElementById('points').value;i++){
      pointList.push(new Point());
      bestWay.push(pointList[i]);
    };
    requestAnimationFrame(animate);
    });
  };
