window.onload = function(){
  var canvas = document.getElementById("canvas");
  canvas.width = screen.width;
  canvas.height = screen.height;
  var height = canvas.height;
  var width = canvas.width;
  var ctx = canvas.getContext("2d");

  function Boid(x, y, a, v, id){
    this.id = id;
    this.x = x;
    this.y = y;
    this.angle = a*Math.PI/180;
    this.velocity = v;
    this.velocityX = v*Math.cos(this.angle);
    this.velocityY = v*Math.sin(this.angle);
    this.radius = 250;
  }

  Boid.prototype.draw = function(){
    ctx.save();
    ctx.translate(this.x, this.y);
    ctx.rotate(this.angle+Math.PI/2);
    ctx.strokeStyle = "#000";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(-20, 20);
    ctx.lineTo(20, 20);
    ctx.lineTo(0, -40);
    ctx.lineTo(-20, 20);
    ctx.stroke();
    ctx.restore();
  }

  Boid.prototype.step = function(){
    this.x += this.velocityX;
    this.y += this.velocityY;
  }

  Boid.prototype.update = function(){
    this.velocity = Math.pow(Math.pow(this.velocityX, 2)+Math.pow(this.velocityY, 2), 0.5);
    this.angle = Math.asin(this.velocityY/this.velocity);
  }

  Boid.prototype.getDistance = function(other){
    return Math.pow(Math.pow(this.x-other.x, 2)+Math.pow(this.y-other.y, 2), 0.5);
  }

  Boid.prototype.separate = function(){
    var addX = 0;
    var addY = 0;
    for(var i=0;i<arr.length;i++){
      if(arr[i].id==this.id)continue;
      var distance = this.getDistance(arr[i]);
      if(distance<this.radius){
        var deltaX = (arr[i].x-this.x);
        var deltaY = (arr[i].y-this.y);
        var angle = Math.atan2(deltaX, deltaY);
        var force = 50/(Math.pow(distance, 2)); //Based off force of gravity, numberator is some constant
        addX += force*Math.cos(angle);
        addY += force*Math.sin(angle);
      }
    }
    this.velocityX += addX;
    this.velocityY += addY;
    this.update();
  }

  function drawBackground(){
    ctx.fillStyle = "#F00";
    ctx.fillRect(0,0,canvas.width,canvas.height);
  }

  var arr = [];
  for(var i=0;i<50;i++){
    arr.push(new Boid(Math.random()*width, Math.random()*height, Math.random()*360, Math.random()*2, i));
  }

  function main(){
    drawBackground();
    for(var i=0;i<arr.length;i++){
      arr[i].draw();
      arr[i].step();
      arr[i].separate();
    }
    requestAnimationFrame(main);
  }

  requestAnimationFrame(main);
};
