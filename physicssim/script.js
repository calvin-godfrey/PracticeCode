window.onload = function(){
  var canvas = document.getElementById("canvas");
  canvas.width = screen.width;
  canvas.height = screen.height;
  var width = canvas.width;
  var height = canvas.height;
  var ctx = canvas.getContext("2d");
  var ballArray = [];
  var startClickLocation, endClickLocation, tempEndLocation, tempPrevEndLocation;
  var FACTOR = 0.04;
  var GRAVITY = 0.18; //Arbitrary number unrelated to 9.8 m/s^2
  tempEndLocation = {x:null, y:null};
  tempPrevEndLocation = {x:null, y:null};
  var isMouseDown = false;

  var Ball = function(x, y){
    this.x = x;
    this.y = y;
    this.prevX = x;
    this.prevY = y;
    this.isDone = false;
  }

  Ball.prototype.draw = function(){
    ctx.beginPath();
    ctx.arc(this.x, this.y, 16, 0, Math.PI*2);
    ctx.strokeStyle = "#000";
    ctx.stroke();
    ctx.fillStyle = "#000";
    ctx.fill();
  }

  Ball.prototype.erase = function(){
    ctx.beginPath();
    ctx.arc(this.prevX, this.prevY, 20, 0, Math.PI*2);
    ctx.strokeStyle = "#FFF";
    ctx.stroke();
    ctx.fillStyle = "#FFF";
    ctx.fill();
  }

  Ball.prototype.setup = function(endX, endY){
    this.velocityX = (this.x-endX)*FACTOR;
    this.velocityY = (this.y-endY)*FACTOR;
    this.isDone = true;
  }

  Ball.prototype.move = function(){
    this.x += this.velocityX;
    this.y += this.velocityY;
    this.velocityY += GRAVITY;
    this.erase();
    this.draw();
    this.prevX = this.x;
    this.prevY = this.y;
  }

  function getMousePos(canvas, event){
    var rect = canvas.getBoundingClientRect();
    return {x:event.clientX - rect.left, y:event.clientY - rect.top};
  }

  function drawTrajectory(start, end, color){
    ctx.beginPath();
    ctx.moveTo(start.x, start.y);
    ctx.lineTo(end.x, end.y);
    ctx.strokeStyle = color;
    if(color=="#FFF"){
      ctx.lineWidth = 2.6;
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

  var animate = setInterval(function(){
    for(var i=0;i<ballArray.length;i++){
      if(ballArray[i].isDone==false){
        continue;
      }
      ballArray[i].move();
      if(ballArray[i].x<-20||ballArray[i].x>width+30||ballArray[i].y>height+40){
        ballArray.splice(i,1);
      }
    }
  }, 17);

};
