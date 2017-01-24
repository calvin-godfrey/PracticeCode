window.onload = function(){
  var canvas = document.getElementById("canvas");
  canvas.width = screen.width;
  canvas.height = screen.height;
  var RADIUS = 200;
  var X_CENTER = canvas.width/2;
  var Y_CENTER = canvas.height/2;
  var INNER_RADIUS = RADIUS/2;
  var ctx = canvas.getContext("2d");
  ctx.translate(0.5,0.5);
  window.requestAnimFrame = (function() { //Dunno if this is right but it works so I'm not removing it
    var lastTime = 0;
    var vendors = ['ms', 'moz', 'webkit', 'o'];
    for(var x = 0; x < vendors.length && !window.requestAnimationFrame; ++x) {
        window.requestAnimationFrame = window[vendors[x]+'RequestAnimationFrame'];
        window.cancelAnimationFrame = window[vendors[x]+'CancelAnimationFrame']
                                   || window[vendors[x]+'CancelRequestAnimationFrame'];
    }

    if (!window.requestAnimationFrame)
        window.requestAnimationFrame = function(callback, element) {
            var currTime = new Date().getTime();
            var timeToCall = Math.max(0, 16 - (currTime - lastTime));
            var id = window.setTimeout(function() { callback(currTime + timeToCall); },
              timeToCall);
            lastTime = currTime + timeToCall;
            return id;
        };

    if (!window.cancelAnimationFrame)
        window.cancelAnimationFrame = function(id) {
            clearTimeout(id);
        };
}());

  Point = function(x, y, angle, life){
    this.x = x;
    this.y = y;
    this.angle = angle;
    this.life = life;
  }

  Point.prototype.calcPoint = function(){
    distance = 200*Math.cos(this.life);
    this.x = distance*Math.cos(this.angle);
    this.y = distance*Math.sin(this.angle);
    this.life = this.life + Math.PI/128;
  }

  Point.prototype.draw = function(){
    ctx.save();
    ctx.translate(X_CENTER, Y_CENTER);
    ctx.beginPath();
    ctx.arc(this.x, this.y, 2, 0, Math.PI*2);
    ctx.strokeStyle = "#000";
    ctx.stroke();
    ctx.fillStyle = "#000";
    ctx.fill();
    ctx.restore();
  }

  function drawBackground(){
    ctx.fillStyle = "#FFF";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    /*ctx.beginPath();
    ctx.arc(X_CENTER, Y_CENTER, RADIUS, 0, Math.PI*2);
    ctx.strokeStyle = "#000";
    ctx.stroke();*/
    if(drawTracks){
    for(var i=0;i<points.length;i++){
        var j = i*Math.PI/points.length;
        ctx.beginPath();
        ctx.lineWidth = 1;
        ctx.moveTo(X_CENTER+200*Math.cos(j), Y_CENTER+200*Math.sin(j));
        ctx.lineTo(X_CENTER-200*Math.cos(j), Y_CENTER-200*Math.sin(j));
        ctx.stroke();
      }
    }
  }

  function drawLine(){
    for(var i=0;i<Math.floor(points.length/2);i++){
      var other = Math.floor(points.length/2)+i
      ctx.save();
      ctx.translate(X_CENTER, Y_CENTER);
      ctx.beginPath();
      ctx.moveTo(points[i].x, points[i].y);
      ctx.lineWidth = 1;
      ctx.strokeStyle = getColor(Math.pow(Math.pow(points[i].x-points[other].x, 2)+Math.pow(points[i].y-points[other].y, 2), 0.5));
      ctx.lineTo(points[other].x, points[other].y);
      ctx.stroke();
      ctx.restore();
    }
  }

  var points;
  var drawLines = false;
  var drawTracks = false;
  var restart = false;
  var stopped = false;
  var doloop = undefined;
  function loop(){
    drawBackground();
    for(var i=0;i<points.length;i++){
      points[i].calcPoint();
      points[i].draw();
    }
    if(drawLines)drawLine();
    if(restart){stopped=true;return;}
    if(!restart)var doloop = window.requestAnimationFrame(loop);
  }

  function stop(){
    if(doloop){
      cancelRequestAnimationFrame(doloop);
      doloop = undefined;
    }
  }

  function start(){
    if(!doloop)loop();
  }

  function getColor(n){ //Returns color of line given its distance
    console.log(n);
    if(n<100)return "#F00";
    if(n>300)return "#00F";
    if(n>225)var red=0;
    else{var red = Math.min(256, ((n-100)/200)*256);}
    red = red.toString(16).slice(0,2);
    if(red=="0")red = "00";
    if(n<175)var blue = 0;
    else{var blue = ((n-100)/200)*256;}
    blue = blue.toString(16).slice(0,2);
    if(blue=="0")blue = "00";
    var ans = "#"+red+"00"+blue;
    return ans;
  }

  document.getElementById("start").addEventListener("mousedown", function(event){
    stop();
    restart = true;
    var numPoints = document.getElementById("points").value;
    var magic = document.getElementById("magic").value;
    points = [];
    for(var i=0;i<numPoints;i++){
      points.push(new Point(X_CENTER, Y_CENTER, i*Math.PI/numPoints, i*magic/numPoints)); //Legit last one is a magic number. Now clue why it is what it is
    }
    restart = false;
    start();
  });

  var p = setInterval(function(){
    document.getElementById("selected").innerHTML = document.getElementById("points").value;
  }, 500);

  var l = setInterval(function(){
    if(document.getElementById("lines").checked)drawLines = true;
    else{drawLines = false;}
  }, 500);

  var t = setInterval(function(){
    if(document.getElementById("track").checked)drawTracks = true;
    else{drawTracks = false;}
  }, 500);

  var m = setInterval(function(){
    document.getElementById("dispMagic").innerHTML = document.getElementById("magic").value;
  }, 500);

  document.getElementById("stop").addEventListener("mousedown", function(event){
    stop();
    restart = true;
  });

}
