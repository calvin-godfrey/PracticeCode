window.onload = function(){
  var canvas = document.getElementById("canvas");
  canvas.width = screen.width;
  canvas.height = screen.height;
  var height = canvas.height;
  var width = canvas.width;
  var ctx = canvas.getContext("2d");

  function Vector(x, y){
    this.x = x;
    this.y = y;
  }

  Vector.prototype.magnitude = function(){
    return Math.pow(Math.pow(this.x, 2)+Math.pow(this.y, 2), 0.5);
  }

  function Boid(x, y, a, v, id){
    this.id = id;
    this.x = x;
    this.y = y;
    this.angle = a*Math.PI/180;
    this.velocity = new Vector(v*Math.cos(this.angle), v*Math.sin(this.angle));
    this.radius = 250;
    this.maxSpeed = 5;
  }

  Boid.prototype.draw = function(){
    ctx.save();
    ctx.translate(this.x, this.y);
    ctx.rotate(this.angle+Math.PI/2);
    ctx.strokeStyle = "#000";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(-7, 7);
    ctx.lineTo(7, 7);
    ctx.lineTo(0, -14);
    ctx.lineTo(-7, 7);
    ctx.stroke();
    ctx.restore();
  }

  Boid.prototype.step = function(){
    this.x += this.velocity.x;
    this.y += this.velocity.y;
    this.checkLocation();
  }

  Boid.prototype.checkLocation = function(){
    if(this.x<0)this.x=width;
    if(this.x>width)this.x=0;
    if(this.y<0)this.y=height;
    if(this.y>height)this.y=0;
    /*if(this.x<0||this.x>width||this.y<0||this.y>height){
      this.x = Math.random()*width;
      this.y = Math.random()*height;
    }*/
    if(this.velocity.magnitude()>this.maxSpeed){
      this.velocity = new Vector(this.velocity.magnitude()/this.maxSpeed*Math.cos(this.angle), this.velocity.magnitude()/this.maxSpeed*Math.sin(this.angle));
    }
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
        var deltaX = (this.x-arr[i].x);
        var deltaY = (this.y-arr[i].y);
        var angle = -Math.atan2(deltaX, deltaY);
        var force = 30/distance;
        addX += force*Math.cos(angle);
        addY += force*Math.sin(angle);
      }
    }
    return new Vector(addX, addY);
    //this.velocity.x += addX;
    //this.velocity.y += addY;
    //this.angle = -Math.atan2(this.velocity.x, this.velocity.y)+Math.PI/2;
  }

  Boid.prototype.alignment = function(){
    var avgX = 0;
    var avgY = 0;
    var count = 0;
    for(var i=0;i<arr.length;i++){
      if(arr[i].id==this.id)continue;
      if(this.getDistance(arr[i])<this.radius){
        avgX += arr[i].velocity.x;
        avgY += arr[i].velocity.y;
        count++;
      }
    }
    avgX /= count;
    avgY /= count;
    return mult(new Vector(avgX, avgY), 0.05);
    //this.velocity = add(this.velocity, mult(new Vector(avgX, avgY), 0.1));
    //this.angle = -Math.atan2(this.velocity.x, this.velocity.y)+Math.PI/2;
  }

  Boid.prototype.cohesion = function(){
    var posX = 0;
    var posY = 0;
    var count = 0;
    for(var i=0;i<arr.length;i++){
      if(arr[i].id==this.id)continue;
      if(this.getDistance(arr[i])<this.radius){
        posX += arr[i].x;
        posY += arr[i].y;
        count++;
      }
    }
    posX /= count;
    posY /= count;
    return this.seek(new Vector(posX, posY));
    //this.seek(new Vector(posX, posY));
  }

  Boid.prototype.seek = function(target){
    var posVector = new Vector(this.x, this.y);
    var des = mult(normalize(subtract(posVector, target)), this.maxSpeed);
    return mult(des, -0.02);
    //this.velocity = subtract(this.velocity, mult(des, 0.01));
    //this.angle = -Math.atan2(this.velocity.x, this.velocity.y)+Math.PI/2;
  }

  Boid.prototype.move = function(){
    var moveTo = new Vector(0,0);
    moveTo = add(moveTo, this.cohesion());
    moveTo = add(moveTo, this.separate());
    moveTo = add(moveTo, this.alignment());
    this.velocity = add(this.velocity, moveTo);
    this.angle = -Math.atan2(this.velocity.x, this.velocity.y)+Math.PI/2;
  }

  function drawBackground(){
    ctx.fillStyle = "#FFF";
    ctx.fillRect(0,0,canvas.width,canvas.height);
  }

  function normalize(vector){
    return new Vector(vector.x/vector.magnitude(),vector.y/vector.magnitude());
  }

  function subtract(vect1, vect2){
    return new Vector(vect1.x-vect2.x, vect1.y-vect2.y);
  }

  function mult(vect1, scalar){
    return new Vector(vect1.x*scalar, vect1.y*scalar);
  }

  function add(vect1, vect2){
    return new Vector(vect1.x+vect2.x, vect1.y+vect2.y);
  }

  var arr = [];
  for(var i=0;i<500;i++){
    arr.push(new Boid(Math.random()*width, Math.random()*height, Math.random()*360, Math.random()*2, i));
  }
  //arr.push(new Boid(0,height/2, 0, 5, 0));
  //arr.push(new Boid(width, height/2, 180, 5, 1));

  function main(){
    drawBackground();
    for(var i=0;i<arr.length;i++){
      arr[i].draw();
      arr[i].step();
      arr[i].move();
    }
    requestAnimationFrame(main);
  }

  requestAnimationFrame(main);
};
