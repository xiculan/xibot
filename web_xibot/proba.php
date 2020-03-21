<html>
<script type="text/javascript">
//https://raspberrypi.stackexchange.com/questions/28689/is-it-possible-to-make-javascript-interact-with-the-gpio-pins
function addLoadEvent(func) 
{ //1
    var oldonload = window.onload;
    if (typeof window.onload != 'function')
    { //1.1
        window.onload = func;
    } //1.1
    else
    { //1.2
        window.onload = function()
        { //1.2.1
            if (oldonload)
            {  //1.2.1.1
                oldonload();
            } //1.2.1.1
        func();
        } //1.2.1
    } //1.2
} //1
addLoadEvent(function() {
       document.getElementById('lbltipAddedComment').innerHTML = 'your tip has been submitted!';
});
  function mensaje() {
    setTimeout(function() {console.log("hola desde javascript");},5000);
  }
function myFunction() {
  document.getElementsByTagName("BODY")[0].style.backgroundColor = "yellow";
}
  function hola() {
//    setTimeout(function() {console.log("hola que tal");},1);
//    document.write("Text to display.");
       document.getElementById('lbltipAddedComment').innerHTML = 'hola';
  }
  function adeu() {
       document.getElementById('lbltipAddedComment').innerHTML = 'adeu';
  }
  function avan_xibot() {
       document.getElementById('xibot').innerHTML = 'avanza';
  }
  function para_xibot() {
       document.getElementById('xibot').innerHTML = 'para';
  }
  function alerta() {
    alert("hola");
  }
</script>

<body>
<input type="button" value="asincrono" onclick="mensaje()"/>
<input type="button" value="hola"  onmouseup="adeu()" onmousedown="hola()" />
<input type="button" value="avanzar"  onmouseup="avan_xibot()" onmousedown="para_xibot()" />
<input type="button" value="alerta" onclick="alerta()"/>
<label id="lbltipAddedComment">test</label>
<label id="xibot">xibot</label>

</body>
</html>
