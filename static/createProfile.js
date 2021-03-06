let massUniversity = ["Boston University","Benjamin Franklin Institute of Technology","Eastern Nazarene College"
,"Franklin W. Olin College of Engineering", "Harvard University", "Massachusetts Institute of Technology",
"Massachusetts Maritime Academy","Northeastern University", "Smith College","Tufts University",
"University of Massachusetts Amherst", "University of Massachusetts Boston", "University of Massachusetts Dartmouth"
,"University of Massachusetts Lowell", "Wentworth Institute of Technology", "Western New England University","Worcester Polytechnic Institute"];

let state = ["Alaska", "Alabama", "Arkansas", "American Samoa",
"Arizona", "California", "Colorado", "Connecticut", "District of Columbia",
"Delaware", "Florida", "Georgia","Hawaii", "Iowa",
"Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts",
"Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi",
"Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire",
"New Jersey", "New Mexico", "Nevada", "New York", "Ohio",
"Oklahoma", "Oregon", "Pennsylvania","Rhode Island",
"South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
"Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin",
"West Virginia", "Wyoming"];

let majors = ['Accounting','Actuarial Science',"Advertising","Agriculture","Agricultural and Biological Engineering",
"Agricultural Business Management","Agriculture Economics","Animal Bioscience","Animal Sciences","Anthropology",
"Applied Mathematics","Archaeology","Architectural Engineering","Architecture","Art History","Studio Art",
"Art Education","Biobehavioral Health","Biochemistry","Bioengineering","Biology","Biophysics","Biotechnology",
"Business Administration and Management","Business Logistics","Chemical Engineering","Chemistry","Children",
"Civil Engineering","Computer Engineering","Computer Science","Crime, Law, and Justice","Dance","Earth Sciences",
"Economics","Electrical Engineering","Elementary and Kindergarten Education","Engineering Science","English",
"Environmental Systems Engineering","Environmental Sciences","Environmental Resource Management","Film and Video",
"Finance","Food Science","Forest Science","Forest Technology","General Science","Geography","Geosciences",
"Graphic Design and Photography","Health and Physical Education","Health Policy and Administration",'History',
"Horticulture","Hotel, Restaurant, and Institutional Management","Human Development and Family Studies",
"Individual and Family Studies","Industrial Engineering","Information Sciences and Technology","Journalism","Kinesiology","Landscape Architecture",
"Law Enforcement and Correction","Marine Biology","Marketing","Mathematics","Mechanical Engineering","Media Studies",
"Meteorology","Microbiology","Mineral Economics","Modern Languages","Music Education","Nuclear Engineering",
"Nursing","Nutrition","Philosophy","Physics","Physiology","Political Science","Pre-medicine","Psychology",
"Public Relations","Real Estate","Recreation and Parks","Rehabilitation Services","Religious Studies","Secondary Education",
"Sociology","Social Work","Special Education","Speech Communication","Speech Pathology and Audiology/Communication Disorder"
,"Statistics","Telecommunications","Theater","Wildlife and Fishery Science","Wildlife Technology","Womens Studies"
];

function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
              b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
      x[i].parentNode.removeChild(x[i]);
    }
  }
}
/*execute a function when someone clicks in the document:*/
document.addEventListener("click", function (e) {
    closeAllLists(e.target);
});
}
x = 2;
y = 2;
function addRow(){
  var str = document.getElementById('div');
  if(x == 2){
    str.innerHTML += "<br > <input type='text' id='strengths"+ x +"' name='strengths" + x + "'><br >";
  }
  else{
     str.innerHTML += "<input type='text' id='strengths"+ x +"' name='strengths" + x + "'><br >";
   }
   x++
}
function add2Row(){
  var weak = document.getElementById('div2');
  if(y == 2){
    weak.innerHTML += "<br > <input type='text' id='AreasNeedingHelp" + y + "' name='Areas_needing_help" + y + "'><br >";
  }
  else{
     weak.innerHTML += "<input type='text' id='AreasNeedingHelp" + y + "' name='Areas_needing_help" + y + "'><br >";
   }
   y++;
 }

let massuni = document.querySelector('#college');
let UsState = document.querySelector('#state');
let major = document.querySelector('#major');
autocomplete(massuni, massUniversity);
autocomplete(UsState, state);
autocomplete(major, majors);
