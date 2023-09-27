document.addEventListener('DOMContentLoaded', function() {
    const submitButton = document.getElementById('submit-button');
    if (submitButton) {
        submitButton.addEventListener('click', function(event) {
            event.preventDefault(); // Evita o envio padrão do formulário
            
            // Aqui você pode adicionar a lógica para verificar se o formulário é válido
            const nome = document.querySelector('input[name="nome"]').value;
            const preco = document.querySelector('input[name="preco"]').value;
            const categoria = document.querySelector('select[name="categoria"]').value;

            if (nome && preco && categoria) {
                // Formulário válido, envie-o
                alert('O formulário foi enviado!');
                document.querySelector('form').submit(); // Envie o formulário
            } else {
                // Exibe uma mensagem de erro
                alert('Por favor, preencha todos os campos do formulário.');
            }
        });
    }
});
