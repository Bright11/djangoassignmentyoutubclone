
const searchul=document.getElementById("centernav")



function shownavmobile(){
    searchul.classList.toggle("mobileshowsearch")
}


const golive=document.querySelector(".createul");

function golivedrop(){
   //e.preventDefault()
golive.classList.toggle("openlive")
}



function hidesidebarname(){
    const sidebarname= document.querySelectorAll(".sidebarname")// Select all <p> elements
    for (var i = 0; i < sidebarname.length; i++) {
      sidebarname[i].classList.toggle("hidden"); // Add the "hidden" class to hide paragraphs
    }
  
    
}

const register=document.querySelector(".registerform")

const loginform=document.querySelector(".loginform")

function loginuser(){
register.classList.toggle("hideregister")

loginform.classList.toggle("showlogin")

}
// logout dropdown

const hideshowdropdwon=document.querySelector(".logoutdive")
function showlogout(){
  hideshowdropdwon.classList.toggle("dropdownlogout")
}


