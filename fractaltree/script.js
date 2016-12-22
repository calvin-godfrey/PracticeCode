window.onload = function(){
  var c = document.getElementById("canvas");
  var ANGLE;
  c.width = screen.width*0.9;
  c.height = screen.height*0.9;
  var width = c.width;
  var height = c.height;
  var branchArray;
  var ctx = c.getContext("2d");
  var getAngle = setInterval(function(){
    ANGLE = document.getElementById("angle").value;
    ANGLE = ANGLE*Math.PI/180;
  }, 100);

  var Base = function(){
    this.x = width/2;
    this.y = height;
    this.angle = -Math.PI/2;
    this.length = 300;
    this.toX = this.x + this.length*Math.cos(this.angle);
    this.toY = this.y + this.length*Math.sin(this.angle);
  }

  Base.prototype.draw = function(){
    draw(this, "#000", 1);
  }

  Base.prototype.updateTo = function(){
    return;
  }

  var Branch = function(parent, angle, side){
    this.parent = parent;
    this.x = parent.toX;
    this.y = parent.toY;
    this.length = parent.length*0.7;
    this.side = side;
    this.angle = this.parent.angle + angle;
    if(this.side==0)this.angle = Math.PI-this.angle;
    this.toX = this.x+this.length*Math.cos(this.angle);
    this.toY = this.y+this.length*Math.sin(this.angle);
  };

  Branch.prototype.draw = function(){
    if(this.angle==ANGLE && this.side==1){
      return true;
    }
    else if(this.angle==Math.PI-ANGLE && this.side==0){
      return true;
    }
    else{
      draw(this, "#FFF", 3);
      if(this.side==1){
        this.angle = this.parent.angle + ANGLE;
      }
      else{
        this.angle = this.parent.angle - ANGLE;
      }
      this.updateTo();
      draw(this, "#000", 1);
    }
  }

  Branch.prototype.updateTo = function(){
    this.parent.updateTo();
    this.y = this.parent.toY;
    this.x = this.parent.toX;
    this.toX = this.x+this.length*Math.cos(this.angle);
    this.toY = this.y+this.length*Math.sin(this.angle);
  }

  function draw(branch, color, width){
    ctx.beginPath();
    ctx.moveTo(branch.x, branch.y);
    ctx.strokeStyle=color;
    ctx.lineTo(branch.toX, branch.toY);
    ctx.lineWidth = width;
    ctx.stroke();
  }


  var base = new Base();
  var branchArray = [base];
  var isParent = [false];
  function addToArray(index){
    if(isParent[i]==true){
      return;
    }
    else{
      branchArray.push(new Branch(branchArray[i], ANGLE, 0));
      branchArray.push(new Branch(branchArray[i], ANGLE, 1));
      isParent.push(false);
      isParent.push(false);
      isParent[i] = true;
    }
  }
  for(var i=0;i<8191;i++){
    var len = branchArray.length;
    for(var j=0;j<len;j++){
      addToArray(j);
    }
  }

  var keepDraw = setInterval(function(){
    for(var i=0;i<branchArray.length;i++){
      branchArray[i].draw();
    }
  }, 100);

};
