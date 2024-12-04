def render_homepage() -> str:
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API FastAPI</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding: 20px;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1>Bem-vindo à API FastAPI</h1>
        <p>Esta API está funcionando corretamente!</p>
        <p>Use as rotas para explorar diferentes funcionalidades.</p>
        <p>Para acessar a documentação: /docs</p>
    </body>
    </html>
    """
