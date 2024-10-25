// const body = document.querySelector("body"),
//       sidebar = body.querySelector(".sidebar"),
//       toggle = body.querySelector(".toggle"),
//       searchBtn = body.querySelector(".search-box"),
//       modeSwitch = body.querySelector(".toggle-switch"),
//       modeText = body.querySelector(".mode-text");

//       toggle.addEventListener("click", () =>{
//         sidebar.classList.toggle("close");

//       });

//       searchBtn.addEventListener("click", () =>{
//         sidebar.classList.remove("close");

//       });

//       modeSwitch.addEventListener("click", () =>{
//         body.classList.toggle("dark");

//         if(body.classList.contains("dark")){
//             modeText.innerText = "Light Mode"
//         }else{
//             modeText.innerText = "Dark Mode"
//         }

//       });

const body = document.querySelector("body"),
      navBar =  body.querySelector(".nav-bar"),
      sidebar = body.querySelector(".sidebar"),
      toggle = body.querySelector(".toggle"),
      searchBtn = body.querySelector(".search-box"),
      modeSwitch = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");

// Check local storage for the user's theme preference
let darkMode = localStorage.getItem("darkMode");

// Apply the saved preference
if (darkMode === "enabled") {
    body.classList.add("dark");
    modeText.innerText = "Light Mode";
}

// Toggle sidebar
toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
});

// Search button functionality
searchBtn.addEventListener("click", () => {
    sidebar.classList.remove("close");
});

// Toggle dark mode
modeSwitch.addEventListener("click", () => {
    body.classList.toggle("dark");

    if (body.classList.contains("dark")) {
        modeText.innerText = "Light Mode";
        localStorage.setItem("darkMode", "enabled");  // Save preference
    } else {
        modeText.innerText = "Dark Mode";
        localStorage.setItem("darkMode", "disabled");  // Save preference
    }
});
