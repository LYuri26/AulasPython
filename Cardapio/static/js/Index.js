document.addEventListener('DOMContentLoaded', function () {
    // Função para fazer as imagens pulsarem automaticamente
    function fazerImagensPulsarem() {
        const itensCardapio = document.querySelectorAll('.item-cardapio img');

        itensCardapio.forEach((imagem) => {
            setInterval(() => {
                imagem.classList.toggle('pulso');
            }, 1000); // Pulsar a cada 1 segundo (1000 milissegundos)
        });
    }

    // Iniciar a pulsação das imagens ao carregar a página
    fazerImagensPulsarem();

    // Função para calcular a soma dos valores dos produtos
    function calcularTotalPedido() {
        const checkboxes = document.querySelectorAll('input[name="pedido"]');
        let total = 0;

        checkboxes.forEach((checkbox) => {
            if (checkbox.checked) {
                total += parseFloat(checkbox.value);
            }
        });

        // Atualizar o total na página
        document.getElementById('total').textContent = `Total: R$ ${total.toFixed(2)}`;
    }

    // Adicionar eventos de clique aos checkboxes para recalcular o total
    const checkboxes = document.querySelectorAll('input[name="pedido"]');
    checkboxes.forEach((checkbox) => {
        checkbox.addEventListener('click', calcularTotalPedido);
    });

    // Função para enviar o pedido com confirmação
    function enviarPedido() {
        const confirmacao = confirm('Deseja enviar o pedido?');

        if (confirmacao) {
            alert('Pedido enviado com sucesso!');
            // Aqui você pode adicionar lógica adicional, como enviar os dados para um servidor, etc.
        }
    }

    // Adicionar evento de clique ao botão "Enviar Pedido"
    const botaoEnviarPedido = document.querySelector('button');
    botaoEnviarPedido.addEventListener('click', enviarPedido);
});
