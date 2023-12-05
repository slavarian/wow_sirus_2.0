var dropdownContent = document.getElementById("dropdownContent");
  var dropdownTimer;

  document.getElementById("db").addEventListener("mouseenter", function() {
    clearTimeout(dropdownTimer); 
    dropdownContent.style.display = "block";
  });

  document.getElementById("db").addEventListener("mouseleave", function() {
    dropdownTimer = setTimeout(function() {
      dropdownContent.style.display = "none";
    }, 100); 
  });