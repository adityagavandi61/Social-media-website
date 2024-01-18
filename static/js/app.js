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
  homesec();
}

search.addEventListener("click", () => {
  searchselected = true;
  search.classList.add("imgeselected");
  search.classList.remove("imge");
  home.classList.add("imge");
  home.classList.remove("imgeselected");
  search.innerHTML = `<img src="/static/assets/svg/searchselected.svg" alt="" srcset="" /><li>Search</li>`;
  home.innerHTML = `<img src="/static/assets/svg/home.svg" alt="" srcset="" /><li>Home</li>`;
  searchsec();
  homeselected = false;
});

home.addEventListener("click", () => {
  homeselected = true;
  home.classList.add("imgeselected");
  search.classList.remove("imgeselected");
  search.classList.add("imge");
  home.classList.remove("imge");
  home.innerHTML = `<img src="/static/assets/svg/homeselected.svg" alt="" srcset="" /><li>Home</li>`;
  search.innerHTML = `<img src="/static/assets/svg/search.svg" alt="" srcset="" /><li>Search</li>`;
  homesec();
  searchselected = false;
});

let follow = document.querySelectorAll("#follow");
let like = document.querySelectorAll("#like");

like.forEach((like) => {
  let likecount = 0;
  let liked = true;
  like.addEventListener("click", () => {
    if (liked) {
      likecount++;
      like.innerHTML = `<img src="/static/assets/svg/liked.svg" alt="" srcset="" />${likecount}`;
      liked = false;
    } else {
      likecount--;
      like.innerHTML = `<img src="/static/assets/svg/like.svg" alt="" srcset="" />${
        likecount - 0
      }`;
      liked = true;
    }
  });
});

follow.forEach((follow) => {
  let btn = true;
  follow.addEventListener("click", () => {
    if (btn) {
      follow.classList.add("following1");
      follow.classList.remove("btn-follow");
      follow.innerHTML = `<img src="/static/assets/svg/followed.svg" alt="" srcset="" />Following`;
      btn = false;
    } else {
      follow.innerHTML = `<img src="/static/assets/svg/follow.svg" alt="" srcset="" />Follow`;
      follow.classList.add("btn-follow");
      follow.classList.remove("following1");
      btn = true;
    }
  });
});

function homesec() {
  container.innerHTML = `<div class="postcard">
  <div class="userinfo">
    <a href="#"><img
      class="userprofilepic"
      src="/static/assets/img/pp.webp"
      alt=""
      srcset=""
    />
    <span class="userprofile"
      ><h4 id="username">UserName</h4>
      <p id="date">Date:</p></span>
    </a>
    <button class="btn-follow" id="follow">
      <img src="/static/assets/svg/follow.svg" alt="" srcset="" />
      Follow
    </button>
  </div>
  <div id="post"><img
    src="/static/assets/img/peakpx (11).jpg"
    alt=""
    srcset=""
  /></div>
  <div class="btn">
    <button class="button" id="like">
      <img src="/static/assets/svg/like.svg" alt="" srcset="" />
    </button>
    <button class="button" id="comment">
      <img src="/static/assets/svg/comment.svg" alt="" srcset="" />
    </button>
    <button class="button" id="share">
      <img src="/static/assets/svg/share.svg" alt="" srcset="" />
    </button>
  </div>
  <div class="line"></div>
  <div class="commentbox">
    <a href="#"><img
      class="viewerprofilepic"
      src="/static/assets/img/pp.webp"
      alt=""
      srcset=""
    />
    <h4 class="viewername">@viewername</h4></a>
    <p class="ctext">Hi Hello how are you</p>
  </div>
</div>
<div class="brake"></div>`;
}

function searchsec() {
  container.innerHTML = ` <div class="search">
  <div class="searchbar">
  <input class="inputsearch" id="searchtext" type="text" placeholder="Search...">
  <button class="btn-cancel" id="cancel"><img src="/static/assets/svg/cancel.svg" alt="" srcset=""></button>
  </div>
  <div class="line"></div>
  <div class="searchoutput">
    <div class="accountbox"><a href="#"><img
      class="userprofilepic"
      src="/static/assets/img/pp.webp"
      alt=""
      srcset=""
    />
    <span class="userprofile"
      ><h4 id="username">UserName</h4>
    </a></div>
    <div class="accountbox"><a href="#"><img
      class="userprofilepic"
      src="/static/assets/img/pp.webp"
      alt=""
      srcset=""
    />
    <span class="userprofile"
      ><h4 id="username">UserName</h4>
    </a></div>
    <div class="accountbox"><a href="#"><img
      class="userprofilepic"
      src="/static/assets/img/pp.webp"
      alt=""
      srcset=""
    />
    <span class="userprofile"
      ><h4 id="username">UserName</h4>
    </a>
</div>
</div></div>`;
}
