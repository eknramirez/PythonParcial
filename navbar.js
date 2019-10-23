var botones =document.querySelectorAll('.botones');

botones.forEach(boton =>{
	boton.addEventListener('click', e=>{
		switch(e.currentTarget.id){

			case 'boton_datos':
			fetch('/datos')
                    .then(res => res.text())
                    .then(data => {
                        document.querySelector('#main').innerHTML = data;
                        var script = document.createElement('script');
                        script.setAttribute('src', '../static/js/cargar_datos.js');

                        document.querySelector('#scripts').appendChild(script);                       
                    })
			break;

			case 'boton_limpieza':
			break;

			case 'boton_graficas':

			fetch('/graficos')
                    .then(res => res.text())
                    .then(data => {
                        document.querySelector('#main').innerHTML = data;
                        var script = document.createElement('script');
                        script.setAttribute('src', '../static/js/graficas.js');

                        document.querySelector('#script').appendChild(script);
                        
                    })


			break;

			case 'boton_Consultas':
			fetch('/consultar')
                    .then(res => res.text())
                    .then(data => {
                        document.querySelector('#main').innerHTML = data;
                        var script = document.createElement('script');
                        script.setAttribute('src', '../static/js/consultas.js');

                        document.querySelector('#script').appendChild(script);
                        
                    })

			break;

			case 'boton_Exportar':
			break;
			
			case 'boton_consulta':
			break;
		}
	});
});

function peticion(ruta){

	fetch(ruta)
	.then(response=> response.text())
	.then(data=>{
		document.querySelector('#main').innerHTML = data;
	})
}