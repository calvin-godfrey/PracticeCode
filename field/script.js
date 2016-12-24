window.onload = function(){
  var canvas = document.getElementById("canvas");
  var s = new Image();
  s.src="sun.png";
  var m = new Image();
  m.src="moon.png";
  canvas.width = screen.width;
  canvas.height = screen.height;
  var width = canvas.width;
  var height = canvas.height;
  var ctx = canvas.getContext("2d");
  var GREEN = "#20b705";
  var  BLUE = "#00F";
  var   RED = "#F00";
  var  CYAN = "#4AF";
  var SUNSET = ["#49F", "#48F", "#47F", "#46F", "#45F", "#44F"];
  for(var i=45;i<75;i++){
    SUNSET.push("#" + i + "44FF");
  }
  SUNSET.push("#7330DD", "#682DC6", "#632FB7", "#5E2DAD", "#55299B", "#4A2487", "#421F7A", "#3C1C70", "#361963", "#2f1659", "#2b1451", "#210f3f", "#1c0c35", "#170a2b");

  SUNSET.push("#000");
  var FRAMES = SUNSET.length;
  var STEP = height*0.5/FRAMES;

  var Planet = function(image, angle){ //Yes I know neither of them are planets
    this.angle = angle;
    this.xCenter = width/2;
    this.yCenter = height*1.1;
    this.radius = width/1.8;
    this.x = this.xCenter+this.radius*Math.cos(this.angle);
    this.y = this.yCenter+this.radius*Math.sin(this.angle);
    this.image = image;
    this.width = 55;
    this.height = 55;
  }

  Planet.prototype.draw = function(){
    if(this.y < height*1.1)ctx.drawImage(this.image, this.x-(this.width/2), this.y-(this.height/2), this.width, this.height);
  }

  Planet.prototype.shift = function(){
    this.angle += Math.PI/128;
    this.x = this.xCenter+this.radius*Math.cos(this.angle);
    this.y = this.yCenter+this.radius*Math.sin(this.angle);
  }

  function drawBackground(sky){
    ctx.fillStyle = sky;
    ctx.fillRect(0,0,width,height);
    ctx.strokeStyle = GREEN;
    ctx.arc(width/2, height*5, width*2.05, 0, Math.PI*2);
    ctx.stroke();
    ctx.fillStyle = GREEN;
    ctx.fill();
  }

  var sun = new Planet(s, -Math.PI/2);
  var moon = new Planet(m, Math.PI/2);
  var planets = [sun, moon];
  function animate(){
    var color = CYAN;
    for(var i=0;i<FRAMES;i++){
      if(sun.y > height*0.75 + (STEP*i))color = SUNSET[i];
    }
    drawBackground(color);
    for(var i=0;i<planets.length;i++){
      planets[i].draw();
      planets[i].shift();
    }
    requestAnimationFrame(animate);
  }
  requestAnimationFrame(animate);

};
