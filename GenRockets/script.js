//Idea for this program from Daniel Shiffman, code is my own
window.onload = function(){
  var canvas = document.getElementById("canvas");
  canvas.width = screen.width;
  canvas.height = screen.height;
  var width = canvas.width;
  var height = canvas.height;
  var ctx = canvas.getContext("2d");
  var life = 0;
  var target = new Object();
  target.x = width/2;
  target.y = 50;
  var gen = 0;

  function Rocket(randForce, force){
    this.x = width/2;
    this.y = height;
    this.width = 80;
    this.height = 10;
    this.angle = 0;
    this.xVelocity = 0;
    this.yVelocity = 0;
    this.forces = [];
    this.stuckTime = -1;
    this.isStuck = false;
    if(randForce){
      for(var i=0;i<200;i++){
        this.forces.push([Math.random()*-2 + 1, Math.random()*-2 + 1]);
      }
    }
    else{
      this.forces = force;
    }
  }

  Rocket.prototype.draw = function(){
    ctx.save();
    this.addForce();
    ctx.translate(this.x, this.y);
    ctx.rotate(this.angle);
    ctx.fillStyle = "#CCC";
    ctx.fillRect(-this.width/2, -this.height/2, this.width, this.height);
    ctx.restore();
  }

  Rocket.prototype.addForce = function(){
    if(!this.isStuck){
      this.xVelocity += this.forces[life][0];
      if(this.xVelocity>15)this.xVelocity=15;
      if(this.xVelocity<-15)this.xVelocity=-15;
      if(this.yVelocity>15)this.yVelocity=15;
      if(this.yVelocity<-15)this.yVelocity=-15;
      this.yVelocity += this.forces[life][1];
      this.angle = Math.atan(this.yVelocity/this.xVelocity);
      this.x += this.xVelocity;
      this.y += this.yVelocity;
      if(1/(this.calcHealth()) < 25){ //basically distance
        this.stuckTime = life;
        this.isStuck = true;
      }
    }
  }

  Rocket.prototype.calcHealth = function(){
    var deltaX = this.x-target.x; //x of target
    var deltaY = this.y - target.y; //y of target
    var temp = 1/(Math.pow(Math.pow(deltaX, 2) + Math.pow(deltaY, 2), 0.5)); //Since smaller is better, we to invert this
    if(this.isStuck)temp += 1/this.stuckTime;
    return temp
  }

  function drawBackground(){
    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, width, height);
    ctx.beginPath();
    ctx.arc(target.x, target.y, 25, 0, Math.PI*2);
    ctx.strokeStyle = "#FFF";
    ctx.fillStyle = "#FFF";
    ctx.fill();
    ctx.stroke();
  }

  function crossover(mates, weighted){
    var mate1, mate2;
    var ans = [];
    var arr;
    for(var j=0;j<25;j++){
      arr = [];
      var num = Math.floor(Math.random() * mates.length);
      mate1 = mates[num];
      mate2 = mates[Math.floor(Math.random() * mates.length)];
      for(var i=0;i<200;i++){
        if(!weighted)arr.push([(mate1.forces[i][0]+mate2.forces[i][0])/2 - 0.5*Math.random()+0.25, (mate1.forces[i][1]+mate2.forces[i][1])/2 - 0.5*Math.random()+0.25]);
        else{ //More than just frame-to-frame "learning"
          var newX = 0;
          var newY = 0;
          for(k=Math.max(0, i-5);k<Math.min(i+5, 200);k++){
            //console.log(mate1);
            newX += (mate1.forces[k][0]+mate2.forces[k][0])/Math.pow(3, Math.abs(i-k)+1); //Denominator should theoretically add to 1
            newY += (mate1.forces[k][1]+mate2.forces[k][1])/Math.pow(3, Math.abs(i-k)+1); //So that it doesn't get way faster
          }
          newX += -0.5*Math.random() + 0.25;
          newY += -0.5*Math.random() + 0.25;
          arr.push([newX, newY]);
        }
      }
      ans.push(new Rocket(false, arr));
    }
    return ans;
  }

  var rockets = [];
  for(var i=0;i<25;i++){
    rockets.push(new Rocket(true, []));
  }

  function animate(){
    drawBackground();
    document.getElementById("gen").innerHTML = "generation: " + gen;
    for(var i=0;i<rockets.length;i++){
      rockets[i].draw();
    }
    life += 1;
    if(life==200){ //End of generation
      for(var i=0;i<rockets.length;i++){
        rockets[i].health = rockets[i].calcHealth();
      }
      gen += 1;
      var mate1, mate2, mate3;
      var max1 = -10;
      var max2 = -10;
      var max3 = -10;
      for(var i=0;i<rockets.length;i++){
        if(rockets[i].health > max1){
          mate1 = rockets[i];
          max1 = rockets[i].health;
          continue;
        }
        if(rockets[i].health > max2){
          mate2 = rockets[i];
          max2 = rockets[i].health;
          continue;
        }
        if(rockets[i].health > max3){
          mate3 = rockets[i];
          max3 = rockets[i].health;
          continue;
        }
      }
      life = 0;
      rockets = crossover([mate1, mate2, mate3], false);
    }
    requestAnimationFrame(animate);
  }

  requestAnimationFrame(animate);

};
