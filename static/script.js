$(document).ready(function () {
    numFams = 1;
    numPeople = 1;
    $("#addFam").click(function () {
        numFams++;
        numPeople++;
        $("#inputarea").append('<div class="fam1"><div class="famarea"><p>Email <input type = "text" name = "email'.concat(numFams.toString()).concat('" /></p><div class="deleteEmail"><a class="btn" href="#">Remove email</a></div><div class="nameOuter"><p>Name <input style="display: inline" type = "text" name = "name').concat(numPeople.toString()).concat('" /><a class="btn" href="#"><div class="deleteName"> Remove name</div></a></p></div></div><a class="btn" href="#"><div class="addName">Add Name</div></a></div>'));
    })
    $("#inputarea").on("click", ".addName", function () {
        console.log("registered click");
        numPeople++;
        $(this).parent().parent().children(".famarea").append('<div class="nameOuter"><p>Name <input style="display: inline" type = "text" name = "name'.concat(numPeople.toString().concat('" /><a class="btn" href="#"><div class="deleteName">Remove name</div></a></p></div>')));
    })
    $("#inputarea").on("click", ".deleteName", function () {
        console.log("tryna delete this name");
        numPeople--;
        $(this).parent().remove();
    })
    $("#inputarea").on("click", ".deleteEmail", function () {
        console.log("tryna delete this name");
        numPeople--;
        $(this).parent().parent().remove();
    })
})