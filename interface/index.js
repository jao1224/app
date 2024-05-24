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