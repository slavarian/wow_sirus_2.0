document.addEventListener('DOMContentLoaded', function () {
    const tooltipTriggers = document.querySelectorAll('.tooltip-trigger');

    tooltipTriggers.forEach(function (trigger) {
        trigger.addEventListener('mouseover', function () {
            const tooltipContent = this.closest('.armor-tooltip').querySelector('.tooltip-content');
            tooltipContent.style.display = 'block';
        });

        trigger.addEventListener('mouseout', function () {
            const tooltipContent = this.closest('.armor-tooltip').querySelector('.tooltip-content');
            tooltipContent.style.display = 'none';
        });
    });

});



function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("armor-table");
    switching = true;
    dir = "asc";
    
    while (switching) {
      switching = false;
      rows = table.rows;
  
      for (i = 1; i < rows.length - 1; i++) {
        shouldSwitch = false;
  
        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];
  
        var xValue, yValue;
  
      
        if (!isNaN(x.innerHTML) && !isNaN(y.innerHTML)) {
          xValue = parseFloat(x.innerHTML);
          yValue = parseFloat(y.innerHTML);
        } else {
          xValue = x.innerHTML.toLowerCase();
          yValue = y.innerHTML.toLowerCase();
        }
  
        if (dir == "asc") {
          if (xValue > yValue) {
            shouldSwitch = true;
            break;
          }
        } else if (dir == "desc") {
          if (xValue < yValue) {
            shouldSwitch = true;
            break;
          }
        }
      }
  
      if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        switchcount++;
      } else {
        if (switchcount == 0 && dir == "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
  }