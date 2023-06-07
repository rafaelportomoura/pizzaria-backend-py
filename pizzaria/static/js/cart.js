const show_modal = (modal) => {
  const the_modal = new bootstrap.Modal(document.getElementById(modal));
  the_modal.show();
};

const getCsrf = () => {
  let csrfTokenSpan = document.getElementById('csrf_token');
  let csrfTokenInput = csrfTokenSpan.querySelector('input[name="csrfmiddlewaretoken"]');
  return csrfTokenInput.value;
};

function addToCart(product_id) {
  // Enviar a requisição PATCH usando fetch
  fetch(`/cart/${product_id}/add`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCsrf(),
    },
  })
    .then((response) => response.json())
    .then((data) => {
      // Lógica para lidar com a resposta da requisição PATCH
      location.reload(true);
    })
    .catch((error) => {
      show_modal('modal_error');
      console.error(error);
    });
}

function removeOfCart(product_id) {
  // Enviar a requisição PATCH usando fetch
  fetch(`/cart/${product_id}/remove`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCsrf(),
    },
  })
    .then((response) => response.json())
    .then((data) => {
      // Lógica para lidar com a resposta da requisição PATCH
      location.reload(true);
    })
    .catch((error) => {
      show_modal('modal_error');
      console.error(error);
    });
}
