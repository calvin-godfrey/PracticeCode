window.onload = function(){
    var canvas = document.getElementById("canvas");
    var width = canvas.width;
    var height = canvas.height;
    console.log(canvas.height);
    var ctx = canvas.getContext("2d");

    function numToHex(n){
        var hexString = n.toString(16);
        while(hexString.length<6){
            hexString = "0"+hexString;
        }
        return "#"+hexString;
    }

    function setBackground(color){
        color = color.slice(1, 7);
        var r1 = color.slice(0, 2);
        var g = color.slice(2, 4);
        var b = color.slice(4, 6);
        console.log(parseInt(r1, 16)+"\t" + parseInt(g, 16)+"\t" + parseInt(b, 16));
        ctx.fillStyle = color;
        //ctx.fillRect(0,0,width,height);
        for(var r=0;r<height;r++){
            for(var c=0;c<width;c++){
                var id = ctx.createImageData(1,1);
                var d = id.data;
                d[0] = parseInt(r1, 16);
                d[1] = parseInt(g, 16);
                d[2] = parseInt(b, 16);
                d[3] = 255; //Completely opque
                ctx.putImageData(id, c, r);
            }
        }
    }

    var time=0;
    function main(){
        setBackground(numToHex(time));
        time+=100;
        requestAnimationFrame(main);
    }
    requestAnimationFrame(main);
}
