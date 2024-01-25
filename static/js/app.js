let home = document.querySelector("#home");
let search = document.querySelector("#search");
let account = document.querySelector("#account");
let setting = document.querySelector("#setting");
let postcard = document.querySelector(".postcard");
let container = document.querySelector(".container");

main();
function main() {
  home.classList.add("imgeselected");
  home.classList.remove("imge");
  home.innerHTML = `<img src="/static/assets/svg/homeselected.svg" alt="" srcset="" /><li>Home</li>`;
}

search.addEventListener("click", () => {
  searchselected = true;
  search.classList.add("imgeselected");
  search.classList.remove("imge");
  home.classList.add("imge");
  home.classList.remove("imgeselected");
  account.classList.remove("imgeselected");
  account.classList.add("imge");
  search.innerHTML = `<img src="/static/assets/svg/searchselected.svg" alt="" srcset="" /><li>Search</li>`;
  home.innerHTML = `<img src="/static/assets/svg/home.svg" alt="" srcset="" /><li>Home</li>`;
  account.innerHTML = `<img src="/static/assets/svg/profile.svg" alt="" srcset="" /><li>My Account</li>`;
  homeselected = false;
});

home.addEventListener("click", () => {
  homeselected = true;
  home.classList.add("imgeselected");
  search.classList.remove("imgeselected");
  search.classList.add("imge");
  home.classList.remove("imge");
  account.classList.remove("imgeselected");
  account.classList.add("imge");
  home.innerHTML = `<img src="/static/assets/svg/homeselected.svg" alt="" srcset="" /><li>Home</li>`;
  search.innerHTML = `<img src="/static/assets/svg/search.svg" alt="" srcset="" /><li>Search</li>`;
  account.innerHTML = `<img src="/static/assets/svg/profile.svg" alt="" srcset="" /><li>My Account</li>`;
  searchselected = false;
});
account.addEventListener("click", () => {
  accountselected = true;
  account.classList.add("imgeselected");
  search.classList.remove("imgeselected");
  search.classList.add("imge");
  account.classList.remove("imge");
  home.classList.add("imge");
  home.classList.remove("imgeselected");
  account.innerHTML = `<img src="/static/assets/svg/profileselected.svg" alt="" srcset="" /><li>My Account</li>`;
  search.innerHTML = `<img src="/static/assets/svg/search.svg" alt="" srcset="" /><li>Search</li>`;
  home.innerHTML = `<img src="/static/assets/svg/home.svg" alt="" srcset="" /><li>Home</li>`;
  accountselected = false;
});






// let follow = document.querySelectorAll("#follow");
// let like = document.querySelectorAll("#like");

// like.forEach((like) => {
//   let likecount = 0;
//   let liked = true;
//   like.addEventListener("click", () => {
//     if (liked) {
//       likecount++;
//       like.innerHTML = `<img src="/static/assets/svg/liked.svg" alt="" srcset="" />${likecount}`;
//       liked = false;
//     } else {
//       likecount--;
//       like.innerHTML = `<img src="/static/assets/svg/like.svg" alt="" srcset="" />${
//         likecount - 0
//       }`;
//       liked = true;
//     }
//   });
// });

// follow.forEach((follow) => {
//   let btn = true;
//   follow.addEventListener("click", () => {
//     if (btn) {
//       follow.classList.add("following1");
//       follow.classList.remove("btn-follow");
//       follow.innerHTML = `<img src="/static/assets/svg/followed.svg" alt="" srcset="" />Following`;
//       btn = false;
//     } else {
//       follow.innerHTML = `<img src="/static/assets/svg/follow.svg" alt="" srcset="" />Follow`;
//       follow.classList.add("btn-follow");
//       follow.classList.remove("following1");
//       btn = true;
//     }
//   });
// });

