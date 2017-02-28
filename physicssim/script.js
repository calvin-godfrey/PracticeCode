window.onload = function(){
  var canvas = document.getElementById("canvas");
  var collision = document.getElementById("collision");
  var useCollision;
  var checkCollision = setInterval(function(){
    useCollision = collision.checked;
  }, 1000);
  canvas.width = screen.width;
  canvas.height = screen.height;
  var width = canvas.width;
  var height = canvas.height;
  var ctx = canvas.getContext("2d");
  var ballArray = [];
  var startClickLocation, endClickLocation, tempEndLocation, tempPrevEndLocation;
  var FACTOR = 0.08;
  var GRAVITY = 0.2; //Arbitrary number unrelated to 9.8 m/s^2
  var RADIUS = 20;
  var REBOUND = -0.88;
  var MASS = 5;
  tempEndLocation = {x:null, y:null};
  tempPrevEndLocation = {x:null, y:null};
  var isMouseDown = false;
  var color = ["#F00", "#000", "#0F0", "#00F", "#FF0", "#F0F", "#0FF"];
  var Ball = function(x, y){
    this.x = x;
    this.y = y;
    this.prevX = x;
    this.prevY = y;
    this.isDone = false;
    this.color = color[Math.floor(Math.random()*color.length)];
  }

  Ball.prototype.draw = function(){
    ctx.beginPath();
    ctx.arc(this.x, this.y, 16, 0, Math.PI*2);
    ctx.strokeStyle = "#000";
    ctx.stroke();
    ctx.fillStyle = this.color;
    ctx.fill();
    this.life-=1;
  }

  Ball.prototype.erase = function(){
    ctx.beginPath();
    ctx.arc(this.prevX, this.prevY, RADIUS, 0, Math.PI*2);
    ctx.strokeStyle = "#FFF";
    ctx.stroke();
    ctx.fillStyle = "#FFF";
    ctx.fill();
  }

  Ball.prototype.setup = function(endX, endY){
    this.velocityX = (this.x-endX)*FACTOR;
    this.velocityY = (this.y-endY)*FACTOR;
    this.isDone = true;
    this.life=100000;
  }

  Ball.prototype.move = function(){
    this.moveReally();
    if(useCollision){
      this.checkWallCollision();
      this.checkBallCollision();
    }
  }

  Ball.prototype.moveReally = function(){
    this.x += this.velocityX;
    this.y += this.velocityY;
    this.velocityY += GRAVITY;
    this.erase();
    this.draw();
    this.prevX = this.x;
    this.prevY = this.y;
  }

  Ball.prototype.checkWallCollision = function(){
    if(this.x-RADIUS<=0){
      this.x = RADIUS;
      this.velocityX *= REBOUND;
    }
    if(this.x+RADIUS>=width){
      this.x = width-RADIUS;
      this.velocityX *= REBOUND;
    }
    if(this.y+RADIUS>=height){
      this.y = height-RADIUS;
      this.velocityY *= REBOUND;
      this.velocityX *= 0.97;
    }
    if(this.y-RADIUS<=0){
      this.y = RADIUS;
      this.velocityY*=REBOUND;
    }
  }

  Ball.prototype.checkBallCollision = function(){
    for(var i=0;i<ballArray.length;i++){
      if(i==this.index||ballArray[i].isDone==false){
        continue;
      }
      else if(distance(this, ballArray[i])<=RADIUS*2){
        var other = ballArray[i];
        var dis = distance(this, other);
        var dx = this.x-other.x;
        var dy = this.y-other.y;
        var v1 = Math.sqrt(Math.pow(this.velocityX,2)+Math.pow(this.velocityY,2));
        var v2 = Math.sqrt(Math.pow(other.velocityX,2)+Math.pow(other.velocityY,2));
        var theta1 = Math.asin(this.velocityY/v1);
        var theta2 = Math.asin(other.velocityY/v2);
        var phi = Math.atan2(dx, dy);
        var tempV1X = (v2*Math.cos(theta2-phi))*Math.cos(phi)+v1*Math.sin(theta1-phi)*Math.cos(phi+Math.PI/2);
        var tempV1Y = (v2*Math.cos(theta2-phi))*Math.sin(phi)+v1*Math.sin(theta1-phi)*Math.sin(phi+Math.PI/2);
        var tempV2X = (v1*Math.cos(theta1-phi))*Math.cos(phi)+v2*Math.sin(theta2-phi)*Math.cos(phi+Math.PI/2);
        var tempV2Y = (v1*Math.cos(theta1-phi))*Math.sin(phi)+v2*Math.sin(theta2-phi)*Math.sin(phi+Math.PI/2);
        if(isNaN(tempV1X)||isNaN(tempV1Y)||isNaN(tempV2X)||isNaN(tempV2Y)){
          console.log(theta2);
          console.log(other.velocityY);
          console.log(v2);
          console.log(phi);
          console.log(dy);
          console.log(dis);
          console.log(theta1);
          console.log(this.velocityY);
          console.log(v1);
          console.log("\n");
        }
        this.velocityX = tempV1X;
        this.velocityY = tempV1Y;
        other.velocityX = tempV2X;
        other.velocityY = tempV2Y;
        this.moveReally();
        this.moveReally();
        this.moveReally();
        other.moveReally();
        other.moveReally();
        other.moveReally();
      }
    }
  }

  function getMousePos(canvas, event){
    var rect = canvas.getBoundingClientRect();
    return {x:event.clientX - rect.left, y:event.clientY - rect.top};
  }

  function distance(ball, other){
    return Math.sqrt(Math.pow(ball.x-other.x,2)+Math.pow(ball.y-other.y,2));
  }

  function drawTrajectory(start, end, color){
    ctx.beginPath();
    ctx.moveTo(start.x, start.y);
    ctx.lineTo(end.x, end.y);
    ctx.strokeStyle = color;
    if(color=="#FFF"){
      ctx.lineWidth = 3;
    }
    else{
      ctx.lineWidth = 1;
    }
    ctx.stroke();
  }

  canvas.addEventListener("mousedown", function(event){
    startClickLocation = getMousePos(canvas, event);
    tempEndLocation.x = startClickLocation.x;
    tempEndLocation.y = startClickLocation.y;
    tempPrevEndLocation.x = startClickLocation.x;
    tempPrevEndLocation.y = startClickLocation.y;
    isMouseDown = true;
    ballArray.push(new Ball(startClickLocation.x, startClickLocation.y));
    ballArray[ballArray.length-1].draw();
  });

  canvas.addEventListener("mouseup", function(event){
    endClickLocation = getMousePos(canvas, event);
    drawTrajectory(startClickLocation, endClickLocation, "#FFF");
    isMouseDown = false;
    ballArray[ballArray.length-1].setup(endClickLocation.x, endClickLocation.y);
    ballArray[ballArray.length-1].index = ballArray.length-1;
  });

  canvas.addEventListener("mousemove", function(event){
    if(isMouseDown){
      tempEndLocation = getMousePos(canvas, event);
      drawTrajectory(startClickLocation, tempPrevEndLocation, "#FFF");
      tempPrevEndLocation.x = tempEndLocation.x;
      tempPrevEndLocation.y = tempEndLocation.y;
      drawTrajectory(startClickLocation, tempEndLocation, "#000");
      ballArray[ballArray.length-1].draw();
    }
  });

  var animate = function(){
    for(var i=0;i<ballArray.length;i++){
      if(ballArray[i].isDone==false){
        continue;
      }
      ballArray[i].move();
      if(ballArray[i].x<-200||ballArray[i].x>width+200||ballArray[i].y>height+200||ballArray[i].life<=0){
        ballArray[i].erase();
        ballArray.splice(i,1);
      }
    }
    window.requestAnimationFrame(animate);
  }

  var loop = window.requestAnimationFrame(animate);

};
