function toggleArmorList(dropdownId) {
    var dropdown = document.getElementById(dropdownId);
    dropdown.classList.toggle('show');
}

function showTooltip(tooltipId) {
    document.getElementById(tooltipId).style.display = 'block';
}

function hideTooltip(tooltipId) {
    document.getElementById(tooltipId).style.display = 'none';
}

function changeBodyArmor() {
    var selectedBodyArmorId = document.getElementById('bodyArmorList').value;

    $.ajax({
        type: "POST",
        url: "{% url 'equip_gear' %}",
        data: {
            'character_id': {{ character.id }},
            'gear_type': 'bodyArmor',
            'selected_item': selectedBodyArmorId,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function (data) {
            location.reload();
        },
        error: function (xhr, errmsg, err) {
            console.log("Error: " + xhr.status + ": " + xhr.responseText);
        }
    });
}

function changeHeadArmor() {
    var selectedHeadArmorId = document.getElementById('headArmorList').value;

    $.ajax({
        type: "POST",
        url: "{% url 'equip_gear' %}",
        data: {
            'character_id': {{ character.id }},
            'gear_type': 'headArmor',
            'selected_item': selectedHeadArmorId,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function (data) {
            location.reload();
        },
        error: function (xhr, errmsg, err) {
            console.log("Error: " + xhr.status + ": " + xhr.responseText);
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    const selectedBodyArmor = document.getElementById('selectedBodyArmor');
    const bodyArmorOptions = document.getElementById('bodyArmorOptions');
    const bodyArmorInput = document.getElementById('bodyArmor');

    bodyArmorOptions.addEventListener('click', function (event) {
        if (event.target.tagName === 'img') {
            selectedBodyArmor.textContent = event.target.textContent;
            bodyArmorInput.value = event.target.dataset.value;
        }
    });

    document.addEventListener('click', function (event) {
        if (!bodyArmorOptions.contains(event.target) && event.target !== selectedBodyArmor) {
            bodyArmorOptions.classList.remove('show');
        }
    });

    selectedBodyArmor.addEventListener('click', function () {
        bodyArmorOptions.classList.toggle('show');
    });

    const selectedHeadArmor = document.getElementById('selectedHeadArmor');
    const headArmorOptions = document.getElementById('headArmorOptions');
    const headArmorInput = document.getElementById('headArmor');

    headArmorOptions.addEventListener('click', function (event) {
        if (event.target.tagName === 'img') {
            selectedHeadArmor.textContent = event.target.textContent;
            headArmorInput.value = event.target.dataset.value;
        }
    });

    document.addEventListener('click', function (event) {
        if (!headArmorOptions.contains(event.target) && event.target !== selectedHeadArmor) {
            headArmorOptions.classList.remove('show');
        }
    });

    selectedHeadArmor.addEventListener('click', function () {
        headArmorOptions.classList.toggle('show');
    });
});