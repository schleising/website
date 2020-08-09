function response() {

    responseField = document.getElementById("response_field")
    r_number_var = document.getElementById("r_number").value

    if (r_number_var > 1.5) {
        responseField.textContent = "Seems unlikely"
        responseField.classList.remove("text-success")
        responseField.classList.add("text-danger")
    }
    else if (r_number_var < 0.5) {
        responseField.textContent = "Seems unlikely"
        responseField.classList.remove("text-success")
        responseField.classList.add("text-danger")
    }
    else {
        responseField.textContent = "Possible"
        responseField.classList.remove("text-danger")
        responseField.classList.add("text-success")
    }
}
