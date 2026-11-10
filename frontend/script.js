fetch("http://localhost:8000/produtos")
    .then(response => response.json())
    .then(produtos => {

        const container =
            document.getElementById("produtos");

        produtos.forEach(produto => {

            container.innerHTML += `
                <div class="card">
                    <h3>${produto.nome}</h3>
                    <p>R$ ${produto.preco}</p>
                </div>
            `;
        });
    });
