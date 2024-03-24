let home = document.querySelector("#home");
let search = document.querySelector("#search");
let account = document.querySelector("#account");
let setting = document.querySelector("#setting");
let postcard = document.querySelector(".postcard");
let container = document.querySelector(".container");


// ----pop-up window----


function openPopupimg() {
    document.getElementById('pop').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
  }
  function openPopupvideo() {
    document.getElementById('pop1').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
  }
  
  
  function closePopupimg() {
    document.getElementById('pop').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
  }
  function closePopupvideo() {
    document.getElementById('pop1').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
  }

  function openPopupfollow() {
    document.getElementById('pop2').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
  }
  function closePopupfollow() {
    document.getElementById('pop2').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
  }

  document.addEventListener("DOMContentLoaded", startLoading);
  window.addEventListener("load", finishLoading);

  function startLoading() {
     document.getElementById("loading-bar").style.display = "block";
  }

  function finishLoading() {
     document.getElementById("loading-bar").style.display = "none";
  }


