from pdf2image import convert_from_path

def gerar_capa(pdf_path, capa_path):
    # Converte a primeira página do PDF em uma imagem
    imagens = convert_from_path(pdf_path, first_page=1, last_page=1)
    primeira_pagina = imagens[0]
    
    # Salva a imagem como JPEG
    primeira_pagina.save(capa_path, 'JPEG')

# Exemplo de uso
gerar_capa('livro1.pdf', 'capa_livro1.jpg')
