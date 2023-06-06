const show_modal = (modal) => {
  const the_modal = new bootstrap.Modal(document.getElementById(modal));
  the_modal.show();
};

function addToCart(product_id) {
  let csrfTokenSpan = document.getElementById('csrf_token');
  let csrfTokenInput = csrfTokenSpan.querySelector('input[name="csrfmiddlewaretoken"]');
  let csrfTokenValue = csrfTokenInput.value;

  data = {
    product_id,
  };
  // Enviar a requisição PATCH usando fetch
  fetch(`/cart/${product_id}/add`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfTokenValue,
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      // Lógica para lidar com a resposta da requisição PATCH
      show_modal('modal_success');
      console.log('Dados do usuário atualizados:', data);
    })
    .catch((error) => {
      show_modal('modal_error');
      console.error('Erro ao atualizar os dados do usuário:', error);
    });
}
