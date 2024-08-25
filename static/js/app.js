// Responsive nav
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
  // Automatically fade out alerts after 5 seconds
  setTimeout(function() {
    var alerts = document.getElementsByClassName('alert');
    for (var i = 0; i < alerts.length; i++) {
      alerts[i].style.opacity = '0';
      setTimeout(function(alert) {
        alert.style.display = 'none';
      }, 600, alerts[i]); // Wait for the fade out transition
    }
  }, 5000);

  // Close the alert when the close button is clicked
  var closeButtons = document.getElementsByClassName('alert-close');
  for (var i = 0; i < closeButtons.length; i++) {
    closeButtons[i].onclick = function() {
      var div = this.parentElement;
      div.style.opacity = '0';
      setTimeout(function() {
        div.style.display = 'none';
      }, 600);
    };
  }
  function showReplyForm(id) {
    var form = document.getElementById('reply-form-' + id);
    if (form.style.display === 'none' || form.style.display === '') {
      form.style.display = 'block';
    } else {
      form.style.display = 'none';
    }
  }