let button = document.querySelector("#hide");
let displaynone = document.querySelector("#otp-send");

let btn = true;
button.addEventListener("click", () => {
  if (btn) {
    document.getElementById("password").type = "text";
    document.getElementById("password1").type = "text";
    button.innerHTML = `<img src="/static/assets/svg/showpassword.svg" alt="" srcset="" />`;
    btn = false;
  } else {
    document.getElementById("password").type = "password";
    document.getElementById("password1").type = "password";
    button.innerHTML = `<img src="/static/assets/svg/hidepassword.svg" alt="" srcset="" />`;
    btn = true;
  }
});


