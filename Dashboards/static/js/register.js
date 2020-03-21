var user_type_0 = document.getElementById("id_user_type_0");
user_type_0.setAttribute("onclick", "displayHiddenBlock(this.id)");
var user_type_1 = document.getElementById("id_user_type_1");
user_type_1.setAttribute("onclick", "displayHiddenBlock(this.id)");
var user_type_2 = document.getElementById("id_user_type_2");
user_type_2.setAttribute("onclick", "displayHiddenBlock(this.id)");

function displayHiddenBlock(id) {
    var patient_username = document.getElementById("patient_username")
    if (id === "id_user_type_2") {
        patient_username.style.display = "";
    } else {
        patient_username.style.display = "none";
    }
}