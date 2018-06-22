function onSignIn(googleUser) {
    let id_token = googleUser.getAuthResponse().id_token;
    console.log("Signed in.");
}

function googleSignOut(){
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function(){
        console.log("User signed out.");
    });
}