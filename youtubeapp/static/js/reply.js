const toggleButtons = document.querySelectorAll('.showbtn');

// Add a click event listener to each toggle button
toggleButtons.forEach(button => {
  button.addEventListener('click', function () {
    // Find the parent comment element
    const comment = this.parentElement;

    // Find the reply element within the comment
    const reply = comment.querySelector('.reply');

    // Toggle the visibility of the reply
    if (reply.style.display === 'none' || reply.style.display === '') {
      reply.style.display = 'block';
      this.textContent = 'Hide Reply';
    } else {
      reply.style.display = 'none';
      this.textContent = 'Show Reply';
    }
  });
});





