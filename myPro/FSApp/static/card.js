let cardsImgs = Array.from(document.querySelectorAll(".card-img"))

let backCard=Array.from(document.getElementsByClassName("backCard"))
let cards=Array.from(document.getElementsByClassName("card"))

// let ack=document.querySelector(".tail span a").value
let f=1
i=0

// for the navbar

let menuList=document.getElementById("menuList")
menuList.style.maxHeight='0px'

function togglemenu(){
    if(menuList.style.maxHeight=='0px'){
        menuList.style.maxHeight='130px'
    }
    else{
        menuList.style.maxHeight='0px'
    }
}




// let cardsAlt=Array.from(document.querySelectorAll('.container-mine card'))

// cardsAlt.forEach()
cards.forEach(
    (ele)=>{
        ele.addEventListener("click",Click)
        console.log(ele)
    }
)

function Click(){

    if(f){
        console.log('clicked')
        this.getElementsByTagName("div")[0].classList.add("FocusBack")
        this.getElementsByTagName("div")[1].classList.remove("deactive")
        f=0
    }
    else{
        console.log('clicked')
        this.getElementsByTagName("div")[0].classList.remove("FocusBack")
        this.getElementsByTagName("div")[1].classList.add("deactive")
        f=1  
    }
}

function Done(){
    // let ack=document.querySelector(".tail span a").value
    // if(ack){
        Swal.fire({
            position: 'top-end',
            icon: 'success',
            title: 'Your work has been saved',
            showConfirmButton: false,
            timer: 1500
          })
    }

// }
function sa_check(){
    var m = "{{ message }}";
Swal.fire({
  icon: 'success',
  iconHtml: '<i class="fa fa-check"></i>',
  text: m,
  confirmButtonColor: '#fff',
  color: '#000',
  background: 'rgba(0, 0, 0, 0.7)',
  allowEscapeKey: false,
  showClass: {
    popup: 'my-icon'                     // disable popup animation css
  },
});
}

