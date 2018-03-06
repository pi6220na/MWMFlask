function showModal(id) {
    // alert(id);
    var modal = document.getElementById(id);
    modal.style.display = "block";
}

function closeModal(obj) {
    var element = obj;
    while (element.className !== 'modal') {
        element = element.parentNode
    }
    element.style.display = "none";
}
