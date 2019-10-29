let identify = (l,w)=>{
  $.ajax({
    type:'POST',
    url:'/',
    data:JSON.stringify({width:w,length:l}),
    contentType: 'application/json',
    success: response=>{
      if (+response) {
        fill(255,87,34)
        ellipse(l,height-w,15,15)
      }
      else{
        fill(33,150,243)
         ellipse(l,height-w,15,15)
      }
    }
  })
}

function setup() { 
   let navheight = $("nav")[0].offsetHeight
   createCanvas(innerWidth,innerHeight-navheight) 
    background(51)
    translate(0,height) 
}

function draw() {

}
 
function mouseDragged() { 
  fill(255)
  if (mouseX>=0&&mouseX<=width&&mouseY>=0&&mouseY<=height) {
   ellipse(mouseX,mouseY,15,15) 
   console.log(mouseX,height - mouseY)
   identify(mouseX, height - mouseY)
}
}