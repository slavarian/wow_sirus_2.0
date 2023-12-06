

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

    document.addEventListener('DOMContentLoaded', function () {
        const selectedBodyArmor = document.getElementById('selectedBodyArmor');
        const bodyArmorOptions = document.getElementById('bodyArmorOptions');
        const bodyArmorInput = document.getElementById('bodyArmor');
    
        bodyArmorOptions.addEventListener('click', function (event) {
            if (event.target.tagName === 'DIV') {
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
            if (event.target.tagName === 'DIV') {
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

        
        const selectedAmulet = document.getElementById('selectedAmulet');
        const amuletOptions = document.getElementById('amuletOptions');
        const amuletInput = document.getElementById('amulet');
    
        amuletOptions.addEventListener('click', function (event) {
            if (event.target.tagName === 'DIV') {
                selectedAmulet.textContent = event.target.textContent;
                amuletInput.value = event.target.dataset.value;
            }
        });
    
        document.addEventListener('click', function (event) {
            if (!amuletOptions.contains(event.target) && event.target !== selectedAmulet) {
                amuletOptions.classList.remove('show');
            }
        });
    
        selectedAmulet.addEventListener('click', function () {
            amuletOptions.classList.toggle('show');
        });

        const selectedShoulderArmor = document.getElementById('selectedShoulderArmor');
        const shoulderArmorOptions = document.getElementById('ShoulderArmorOptions');
        const shoulderArmorInput = document.getElementById('shoulderArmor');
    
        shoulderArmorOptions.addEventListener('click', function (event) {
            if (event.target.tagName === 'DIV') {
                selectedShoulderArmor.textContent = event.target.textContent;
                shoulderArmorInput.value = event.target.dataset.value;
            }
        });
    
        document.addEventListener('click', function (event) {
            if (!shoulderArmorOptions.contains(event.target) && event.target !== selectedShoulderArmor) {
                shoulderArmorOptions.classList.remove('show');
            }
        });
    
        selectedShoulderArmor.addEventListener('click', function () {
            shoulderArmorOptions.classList.toggle('show');
        });

        const selectedBackArmor = document.getElementById('selectedBackArmor');
        const backArmorOptions = document.getElementById('backArmorOptions');
        const backArmorInput = document.getElementById('backArmorInput');
    
        backArmorOptions.addEventListener('click', function (event) {
            if (event.target.tagName === 'DIV') {
                selectedBackArmor.textContent = event.target.textContent;
                backArmorInput.value = event.target.dataset.value;
            }
        });
    
        document.addEventListener('click', function (event) {
            if (!backArmorOptions.contains(event.target) && event.target !== selectedBackArmor) {
                backArmorOptions.classList.remove('show');
            }
        });
    
        selectedBackArmor.addEventListener('click', function () {
            backArmorOptions.classList.toggle('show');
        });

        
        const selectedWristArmor = document.getElementById('selectedWristArmor');
        const wristArmorOptions = document.getElementById('wristArmorOptions');
        const wristArmorInput = document.getElementById('wristArmorInput');
    
        wristArmorOptions.addEventListener('click', function (event) {
            if (event.target.tagName === 'DIV') {
                selectedWristArmor.textContent = event.target.textContent;
                wristArmorInput.value = event.target.dataset.value;
            }
        });
    
        document.addEventListener('click', function (event) {
            if (!wristArmorOptions.contains(event.target) && event.target !== selectedWristArmor) {
                wristArmorOptions.classList.remove('show');
            }
        });
    
        selectedWristArmor.addEventListener('click', function () {
            wristArmorOptions.classList.toggle('show');
        });

        const selectedGlovesArmor = document.getElementById('selectedGlovesArmor');
        const glovesArmorOptions = document.getElementById('glovesArmorOptions');
        const glovesArmorInput = document.getElementById('glovesArmorInput');
    
        glovesArmorOptions.addEventListener('click', function (event) {
            if (event.target.tagName === 'DIV') {
                selectedGlovesArmor.textContent = event.target.textContent;
                glovesArmorInput.value = event.target.dataset.value;
            }
        });
    
        document.addEventListener('click', function (event) {
            if (!glovesArmorOptions.contains(event.target) && event.target !== selectedGlovesArmor) {
                glovesArmorOptions.classList.remove('show');
            }
        });
    
        selectedGlovesArmor.addEventListener('click', function () {
            glovesArmorOptions.classList.toggle('show');
        });

        

    });

