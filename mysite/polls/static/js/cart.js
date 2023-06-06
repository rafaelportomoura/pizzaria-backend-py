// Função para enviar o POST
function sendCartItemUpdate(user, itemID, quantity) {
  // Construir os dados a serem enviados no corpo do POST
  var data = {
    quantity: quantity,
  };

  // Enviar o POST usando fetch ou XMLHttpRequest
  fetch(`/cart/${user}/item/${itemID}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': '{{ csrf_token }}', // Certifique-se de ajustar o valor do token CSRF corretamente
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      // Lógica para lidar com a resposta do POST
      console.log('Atualização do carrinho enviada com sucesso:', data);
    })
    .catch((error) => {
      console.error('Erro ao enviar a atualização do carrinho:', error);
    });
}

// Capturar eventos de clique nos links de aumento e diminuição de quantidade
document.addEventListener('click', function (event) {
  var target = event.target;
  if (target.classList.contains('increase-quantity')) {
    event.preventDefault();
    var tr = target.closest('tr');
    var itemID = tr.getAttribute('data-id');
    var quantity = parseInt(tr.querySelector('span').textContent) + 1;
    sendCartItemUpdate(itemID, quantity);
  } else if (target.classList.contains('decrease-quantity')) {
    event.preventDefault();
    var tr = target.closest('tr');
    var itemID = tr.getAttribute('data-id');
    var quantity = parseInt(tr.querySelector('span').textContent) - 1;
    if (quantity >= 0) {
      sendCartItemUpdate(itemID, quantity);
    }
  }
});
