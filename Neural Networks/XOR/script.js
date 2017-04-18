window.onload = function(){
  var inputData = [[0, 0], [0, 1], [1, 0], [1, 1]];
  var outputData = [0, 1, 1, 0];

  function activation(n){
    return 1/(1+Math.exp(-n)); //Standard sigmoid
  }

  var Neuron = function(isInput, isOutput){
    this.isInput = isInput;
    this.isOutput = isOutput;
    if(this.isInput&&this.isOutput)throw "Neuron cannot be input and output";
  }

  Neuron.prototype.initialize = function(n){ //where n is the number of neurons in the previous layer, this is only done for the initial generation
    this.weights = [];
    for(var i=0;i<n;i++){
      this.weights.push(Math.floor(-10*Math.random() + 5));
    }
    if(this.isInput)return; //input neuron does not need bias
    this.bias = Math.floor(-10*Math.random() + 5); //Random bias value
  }

  Neuron.prototype.setValues = function(weights, bias){ //This is done for all generations after the first
    this.weights = weights;
    if(this.isInput)return;
    this.bias = bias;
  }

  Neuron.prototype.feedForward = function(input){ //This is an array where the nth element is the output of the nth neuron in previous layer
    if(!this.weights)throw "Weights must be initialized first";
    var output = 0;
    for(var i=0;i<input.length;i++){
      output += input[i]*this.weights[i];
    }
    if(!this.isInput)output += this.bias;
    return activation(output);
  }

  var Network = function(size, isInitial){ //Size is an array where the nth element is the number of neurons in the nth layer
    this.layers = [];
    this.isInitial = isInitial;
    this.ready = false;
    for(var i=0;i<size.length;i++){
      this.layers.push([]);
      for(var j=0;j<size[i];j++){
        if(i == 0){
          this.layers[i].push(new Neuron(true, false));
        }
        if(i == size.length-1){
          this.layers[i].push(new Neuron(false, true));
        }
        if(i != 0 && i != size.length-1){
          this.layers[i].push(new Neuron(false, false));
        }
      }
    }
    if(isInitial){
      this.ready = true;
      for(var j=0;j<layers[0].length;i++){
        this.layers[0][j].initialize(1); //only one weight from the input
      }
      for(var i=1;i<layers.length;i++){ //Skip the input layer
        for(var j=0;j<layers[i].length;j++){ //jagged array
          this.layers[i][j].initialize(layers[i-1].length); //random weight array and values
        }
      }
    }
  }

  Network.prototype.setValues = function(values){ //Values is 3-dimensional array, first is layers, second is neurons, then two values: weights and bias
    if(this.ready||this.isInitial)return;
    this.ready = true;
    for(var j=0;j<this.layers[0].length;j++){
      this.layers[0][j].setValues(values[0][j]); //first layer has no bias
    }
    for(var i=1;i<this.layers.length;i++){
      for(var j=0;j<this.layers[i].length;j++){
        this.layers[i][j].setValues(values[i][j][0], values[i][j][1]);
      }
    }
  }

  Network.prototype.process = function(input){
    for(var i=0;i<input.length;i++){
      input[i] *= this.layers[0][i].weights[0]; //Multiplies input by the weight of each input neuron
    }
    for(var i=1;i<this.layers.length;i++){
      var out = [];
      for(var j=0;j<this.layers[i].length;j++){
        out.push(this.layers[i][j].feedForward(input));
      }
      input = out;
    }
    return input;
  }

  function main(){
    var network = new Network([2, 1, 1], false); //Two input neurons, one hidden neuron, one output neuron

    network.setValues([[[2], [2]], [[[2, 1], 1]], [[[2], 1]]]);
    console.log(network.process([1, 1]));
  }

  document.getElementById("start").addEventListener("mousedown", function(event){
    main();
  });
}
