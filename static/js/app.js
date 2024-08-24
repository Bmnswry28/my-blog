function toggleMenu() {
    var x = document.querySelector(".nav");
    if (x.className === "nav") {
        x.className += " responsive";
    } else {
        x.className = "nav";
    }
}
function showReplyForm(id) {
    var replyForm = document.getElementById('reply-form-' + id);
    if (replyForm.style.display === 'none') {
      replyForm.style.display = 'block';
    } else {
      replyForm.style.display = 'none';
    }
  }

  function toggleMenu() {
    var x = document.querySelector(".nav");
    if (x.className === "nav") {
      x.className += " responsive";
    } else {
      x.className = "nav";
    }
  }