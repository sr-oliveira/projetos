
  $(function() {
    // Configurar autocomplete de categorias
    $('#search-category').autocomplete({
      source: '/api/categories'
    });
  
    // Submeter formulário de busca
    $('#search-form').submit(function(event) {
      event.preventDefault();
      const formData = $(this).serialize();
      $.get('/api/search', formData, function(results) {
        // Exibir resultados da busca na tabela
        $('#search-results').html('');
        results.forEach(function(result) {
          $('#search-results').append(
            '<tr><td>' + result.title + '</td><td>' + result.category + '</td></tr>'
          );
        });
      });
    });
  });
  