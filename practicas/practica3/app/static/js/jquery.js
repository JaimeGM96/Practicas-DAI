$(document).on("click", "#btn-add", function(){
    //declarar variables
    $.post("/aniade-pokemon/nuevo", function(data){
        let fila = 
        console.log("Añadido correctamente")
    });
});

$(document).on("click", "#btn-update", function(){
    let id = $("")
    $.put("/actualiza-pokemon", function(data){
        console.log("Modificado correctamente")
    });
});

$(document).on("click", "#btn-delete", function(){
    //declarar variables
    $.delete("/add_pokemon", function(data){
        console.log("Eliminado correctamente")
    });
});

// $(function () {
//     $("#btn-add").click(function () {
//       $.ajax({
//         url: '/aniade-pokemon/nuevo',
//         type: 'POST',
//         dataType: 'json',
//         success: function (data) {
//             console.log("Añadido correctamente")
//         }
//       });
//     });
// });

// $(function () {
//     $("#btn-update").click(function () {
//         let id = $(this).val();
//         $.ajax({
//             url: '/actualiza-pokemon',
//             type: 'PUT',
//             data: {id: id},
//             success: function (data) {
//                 console.log("Modificado correctamente")
//             }
//         });
//     });
// });

// $(function () {
//     $("#btn-delete").click(function () {
//         let id = $(this).val();
//         $.ajax({
//             url: '/borrar-pokemon',
//             type: 'DELETE',
//             data: {id: id},
//             success: function (data) {
//                 console.log("Eliminado correctamente")
//             }
//         });
//     });
// });