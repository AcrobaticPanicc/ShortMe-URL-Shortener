function copyToClipboard() {
    let copyText = document.getElementById("copy-able");
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/
    document.execCommand("copy");
}


$("#copy-btn").click(function () {
    $("div.success").fadeIn(300).delay(1500).fadeOut(900);
});

function checkUrl(event) {
    let value = document.getElementById('url-input').value;
    if (value.length < 5) {
        $("div.alert-warning").fadeIn(300).delay(1500).fadeOut(900);
        event.preventDefault();
        return false;
    }
}


function checkEmail(event) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    let email = document.getElementById('email_input').value;
    let isEmailValid = re.test(String(email).toLowerCase());

    if (email.length < 1) {
        $("div#cant-be-empty").fadeIn(300).delay(1500).fadeOut(900);
        event.preventDefault();
        return false;

    } else if (isEmailValid === false) {
        $("div#invalid-email").fadeIn(300).delay(1500).fadeOut(900);
        event.preventDefault();
        return false;
    }
}

function callGetToken() {
    let xhttp = new XMLHttpRequest();
    let hostUrl = document.getElementById('host-url').getAttribute('value');
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            document.getElementById("token").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", `${hostUrl}/api/get_token`, true);
    xhttp.send();
}

$('#verification').on('keyup', function () {
    var foo = $(this).val().split(" ").join("");
    if (foo.length > 0) {
        foo = foo.match(new RegExp('.{1,3}', 'g')).join(" ");
    }
    $(this).val(foo);
});