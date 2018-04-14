//edit subscription model

// Get the button that opens the modal
var btn_editsub = document.getElementById("myBtn");

// Get the modal
var modal_editsub = document.getElementById('myModal');

// Get the <span> element that closes the modal
var span_editsub = document.getElementsByClassName("close_editsub")[0];

// When the user clicks the button, open the modal 
btn_editsub.onclick = function() {
    modal_editsub.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span_editsub.onclick = function() {
    modal_editsub.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
/*window.onclick = function(event1) {
    if (event1.target == modal_editsub) {
        modal_editsub.style.display = "none";
    }
}*/


//edit info modal

// Get the button that opens the modal
var btn_editinfo = document.getElementById("editinfoBtn");

// Get the modal
var modal_editinfo = document.getElementById('editinfoModal');

// Get the <span> element that closes the modal
var span_editinfo = document.getElementsByClassName("close_editinfo")[0];

// When the user clicks the button, open the modal 
btn_editinfo.onclick = function() {
    modal_editinfo.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span_editinfo.onclick = function() {
    modal_editinfo.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
/*window.onclick = function(event) {
    if (event.target == modal_editinfo) {
        modal_editinfo.style.display = "none";
    }
}*/