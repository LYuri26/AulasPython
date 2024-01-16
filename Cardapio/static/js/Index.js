// Função para incrementar o contador
function incrementarContador(item) {
  var contador = item.querySelector(".contador span");
  if (contador) {
    var valorAtual = parseInt(contador.textContent);
    contador.textContent = valorAtual + 1;
    atualizarTotalPedido();
  }
}

// Função para decrementar o contador
function decrementarContador(item) {
  var contador = item.querySelector(".contador span");
  if (contador) {
    var valorAtual = parseInt(contador.textContent);
    if (valorAtual > 0) {
      contador.textContent = valorAtual - 1;
      atualizarTotalPedido();
    }
  }
}

// Função para limpar e bloquear checkboxes
function checarCheckboxes() {
  var checkboxes = document.querySelectorAll('input[name="pedido"]');
  checkboxes.forEach(function (checkbox) {
    checkbox.checked = false;
    var item = checkbox.closest(".item-cardapio");
    item.querySelector(".contador span").textContent = "0";
    item.querySelector(".subtrair").disabled = true;
    item.querySelector(".somar").disabled = true;
  });

  atualizarTotalPedido();
}

// Função para atualizar o total do pedido
function atualizarTotalPedido() {
  var total = 0;
  var checkboxes = document.querySelectorAll(".checar");

  checkboxes.forEach(function (checkbox) {
    var preco = parseFloat(checkbox.value);
    var item = checkbox.closest(".item-cardapio");
    var quantidadeElement = item.querySelector(".contador span");
    var quantidade = parseInt(quantidadeElement.textContent);

    if (checkbox.checked) {
      total += preco * quantidade;
      item.querySelector(".subtrair").disabled = false;
      item.querySelector(".somar").disabled = false;
    } else {
      item.querySelector(".subtrair").disabled = true;
      item.querySelector(".somar").disabled = true;

      // Limpar o contador quando o checkbox é desmarcado
      quantidadeElement.textContent = "0";
    }
  });

  document.getElementById("total").textContent =
    "Total: R$ " + total.toFixed(2);
}

// Adicionar eventos de clique aos botões para incrementar/decrementar o contador
const botoesIncrementar = document.querySelectorAll(".item-cardapio .subtrair");
const botoesDecrementar = document.querySelectorAll(".item-cardapio .somar");

botoesIncrementar.forEach((botao) => {
  if (!botao.hasEventListener) {
    botao.hasEventListener = true; // Flag to check if the listener has been added
    botao.addEventListener("click", function () {
      incrementarContador(this.closest(".item-cardapio"));
    });
  }
});

botoesDecrementar.forEach((botao) => {
  if (!botao.hasEventListener) {
    botao.hasEventListener = true;
    botao.addEventListener("click", function () {
      decrementarContador(this.closest(".item-cardapio"));
    });
  }
});

// Adicionar eventos de mudança aos checkboxes
const checkboxes = document.querySelectorAll('input[name="pedido"]');
checkboxes.forEach((checkbox) => {
  checkbox.addEventListener("change", function () {
    atualizarTotalPedido();
  });
});

// Adicionar efeito de imagem pulsante automático
const imagens = document.querySelectorAll(".item-cardapio img");

function pulsarImagens() {
  imagens.forEach((imagem) => {
    imagem.style.transition = "transform 0.5s";
    imagem.style.transform = "scale(1.03)";

    setTimeout(() => {
      imagem.style.transform = "scale(1.0)";
    }, 500);
  });
}

// Iniciar a pulsação automática a cada 3 segundos (ajuste conforme necessário)
setInterval(pulsarImagens, 3000);

function enviarPedido() {
  var totalText = document.getElementById("total").textContent;
  var total = parseFloat(totalText.replace("Total: R$ ", "").replace(",", "."));

  if (isNaN(total)) {
    alert("Selecione pelo menos um item antes de enviar o pedido.");
    return;
  }

  alert("O valor total do seu pedido é de R$ " + total.toFixed(2));

  if (total > 600) {
    const confirmacao = confirm(
      "Tem certeza disso? Por acaso está brincando com a gente? Vai alimentar um batalhão?"
    );

    if (!confirmacao) {
      // Reiniciar e limpar a página
      location.reload();
      return;
    }
  } else {
    var checkboxes = document.querySelectorAll('input[name="pedido"]:checked');

    if (checkboxes.length > 0) {
      alert("Pedido enviado com sucesso!");
      // Aqui você pode adicionar lógica adicional, como enviar os dados para um servidor, etc.
    } else {
      alert("Selecione pelo menos um item antes de enviar o pedido.");
    }
  }

  // Remove the event listener after the first click
  botaoEnviarPedido.removeEventListener("click", enviarPedido);
}

// Adicionar evento de clique ao botão "Enviar Pedido"
const botaoEnviarPedido = document.getElementById("enviar");
if (!botaoEnviarPedido.hasEventListener) {
  botaoEnviarPedido.hasEventListener = true;
  botaoEnviarPedido.addEventListener("click", enviarPedido);
}
