function onSignIn(googleUser) {
    let id_token = googleUser.getAuthResponse().id_token;
    console.log("Signed in.");
    $.post("/google/token_signin", {token: id_token}, function(data, status){
        console.log(data + " " + status)
    });
}

function googleSignOut(){
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function(){
        console.log("User signed out.");
    });
}