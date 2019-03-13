let bookmark_button = document.getElementsByClassName("bookmark");

function bookmark () {
    console.log("Add this Article to my bookmarks.");
}

fname = document.querySelector('#id_first_name');

if (fname) {
    fname.focus();
}

window.setTimeout(function ()
{
    document.getElementById('id_first_name').focus();
}, 0);

document.querySelector('#id_username').focus();