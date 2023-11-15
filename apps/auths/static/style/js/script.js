function showTooltip(tooltipId) {
    var tooltip = document.getElementById(tooltipId);
    if (tooltip) {
        tooltip.querySelector('.tooltip-content').style.display = 'block';
    }
}

function hideTooltip(tooltipId) {
    var tooltip = document.getElementById(tooltipId);
    if (tooltip) {
        tooltip.querySelector('.tooltip-content').style.display = 'none';
    }
}

