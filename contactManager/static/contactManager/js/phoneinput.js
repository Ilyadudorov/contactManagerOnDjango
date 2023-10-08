document.addEventListener("DOMContentLoaded", function(){
    let phoneInputs = document.getElementById('phone')




    for (i=0; i<phoneInputs.length; i++){
        let input = phoneInputs[i];
        input.addEventListener('input',onPhoneInput) //Обрабатываем каждый input с id phone

    }
});