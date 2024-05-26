document.getElementById('meuFormulario').addEventListener('submit', function(event){
    event.preventDefault();
    var nome = document.getElementById('nome').value;
    var data_lancamento = document.getElementById('data_lancamento').value;
    var destino = document.getElementById('destino').value;
    var estado = document.getElementById('estado').value;
    var tripulacao = document.getElementById('tripulacao').value;
    var carga_util = document.getElementById('carga_util').value;
    var duracao = document.getElementById('duracao').value;
    var custo = document.getElementById('custo').value;
    var status = document.getElementById('status').value;
    
    var dados = {
      
        nome: nome,
        data_lancamento: data_lancamento,
        destino: destino,
        estado: estado,
        tripulacao: tripulacao,
        carga_util: carga_util,
        duracao: duracao,
        custo: custo,
        status: status
    };
    console.log(dados)
    // realizar requisição AJAX para a API
    fetch('http://127.0.0.1:9000/Create',{
        method:'post',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })
});

    



document.getElementById('deletar').addEventListener('submit', function(event){
    event.preventDefault();
        
    var id = document.getElementById('id').value;
        
    var dadosdelet = {
        id: id
    };
        
    console.log(dadosdelet)
        
    // realizar requisição AJAX para a API
    fetch('http://127.0.0.1:9000/Delete',{
        method:'delete',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dadosdelet)
    })
});


document.getElementById('searchForm').addEventListener('submit', function(event){
    event.preventDefault();
    
    var id = document.getElementById('id').value;
         
    var dadospesq = {
        id: id
    };
    fetch('http://127.0.0.1:9000/id', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({id: id})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = JSON.stringify(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});