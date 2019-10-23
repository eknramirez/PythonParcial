M.AutoInit();

document.querySelector('#form_graficos').addEventListener('submit', e => {
    e.preventDefault();
    var valor1 = document.querySelector('#consulta').value;
    var formdata = new FormData(document.querySelector('#form_graficos'));
    var valor2 = formdata.getAll('valor2[]');
    console.log(valor2);

    fetch('/consultas', {
        method: 'POST',
        body: new URLSearchParams('valor1='+valor1+'&valor2='+valor2)
    })
        .then(response => response.text())
        .then(data => {
            document.querySelector('#img').setAttribute('src', data);
        })
});