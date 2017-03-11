window.onload = function(){
    var canvas = document.getElementById("canvas");
    var gravity = document.getElementById("gravity");
    var useGravity;
    var GRAVITY = 4;
    var checkGravity = setInterval(function(){
      useGravity = gravity.checked;
    }, 5);
    canvas.width = screen.width;
    canvas.height = screen.height;
    var width = canvas.width;
    var height = canvas.height;
    var ctx = canvas.getContext("2d");
    var startClickLocation, endClickLocation, tempEndLocation, tempPrevEndLocation, isMouseDown;
    var ballArray = [];

    var FACTOR = 0.10;

    var Vector = function(x, y){
        this.x = x;
        this.y = y;
        this.magnitude = Math.pow(Math.pow(x,2)+Math.pow(y,2),0.5);
    }

    var Ball = function(x, y){
      this.x = x;
      this.y = y;
      this.prevX = x;
      this.prevY = y;
      this.isDone = false;
      this.color = "#FFF";
      this.radius = 8;
    }

    Ball.prototype.draw = function(){
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI*2);
      ctx.lineWidth = 4;
      ctx.strokeStyle = "#000";
      ctx.stroke();
      ctx.fillStyle = this.color;
      ctx.fill();
      this.life-=1;
    }

    Ball.prototype.setup = function(endX, endY){
      this.velocity = new Vector((this.x-endX)*FACTOR, (this.y-endY)*FACTOR);
      this.isDone = true;
      this.life=100000;
    }

    Ball.prototype.step = function(){
        this.x += this.velocity.x;
        this.y += this.velocity.y;
        if(useGravity)this.velocity.y += GRAVITY;
        this.checkLocation();
    }

    Ball.prototype.checkLocation = function(){
        var epsilon = this.radius;
        var distance = Math.pow(Math.pow(this.x-width/2, 2)+Math.pow(this.y-height/2, 2), 0.5);
        if(distance>200-epsilon&&distance<200+epsilon){
            var slope = -(this.x-width/2)/(this.y-height/2); //Implicit differentiation!
            var normalAngle = Math.atan2(this.x-width/2, this.y-height/2);
            var normal = new Vector(Math.cos(normalAngle), Math.sin(normalAngle));
            var velocitySlope = this.velocity.magnitude;
            var angle = Math.atan(Math.abs((slope-velocitySlope)/(1+slope*velocitySlope)));
            var perpAngle = Math.PI/2-angle;
            var u = new Vector((dotProduct(this.velocity, normal, perpAngle))*normal.x, (dotProduct(this.velocity, normal, perpAngle))*normal.y);
            var w = new Vector(this.velocity.x-u.x, this.velocity.y-u.y);
            this.velocity = new Vector(w.x-u.x, w.y-u.y);
        }
    }


    function drawTrajectory(start, end, color){
      ctx.beginPath();
      ctx.moveTo(start.x, start.y);
      ctx.lineTo(end.x, end.y);
      ctx.strokeStyle = color;
      if(color=="#FFF"){
        ctx.lineWidth = 4;
      }
      else{
        ctx.lineWidth = 1;
      }
      ctx.stroke();
    }

    function dotProduct(v1, v2, angle){
        return v1.magnitude*v2.magnitude*Math.cos(angle);
    }

    function getMousePos(canvas, evt){
      var rect = canvas.getBoundingClientRect();
      return {x: (evt.clientX-rect.left)/(rect.right-rect.left)*canvas.width,
        y: (evt.clientY-rect.top)/(rect.bottom-rect.top)*canvas.height};
    }

    function main(){
        ctx.fillStyle = "#fff";
        ctx.fillRect(0,0,width,height);
        ctx.beginPath();
        ctx.lineWidth = 1;
        ctx.arc(width/2, height/2, 200, 0, Math.PI*2);
        ctx.stroke();
        for(var i=0;i<ballArray.length;i++){
            ballArray[i].draw();
            if(ballArray[i].isDone)ballArray[i].step();
        }
        requestAnimationFrame(main);
    }

    requestAnimationFrame(main);

    canvas.addEventListener("mousedown", function(event){
      startClickLocation = getMousePos(canvas, event);
      tempEndLocation = new Object();
      tempPrevEndLocation = new Object();
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
}
