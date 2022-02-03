const headingOne = document.getElementsByTagName('h1')[0];
console.log(headingOne.innerHTML);
var text = "<h1>" + headingOne.innerText + " ---> This text is printed using javascript check console too" + "</h1>";
document.write(text); 