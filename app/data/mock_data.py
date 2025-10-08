# app/data/mock_data.py
from app.models.product import Product

products = [
    Product(
        id="1",
        name="Smartphone Pro X",
        price=999.99,
        imageUrl="https://images.pexels.com/photos/788946/pexels-photo-788946.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Smartphone de última geração com câmera tripla de 48MP, tela AMOLED de 6.5 polegadas e bateria de longa duração."
    ),
    Product(
        id="2",
        name="Laptop Ultra",
        price=1499.99,
        imageUrl="https://images.pexels.com/photos/18105/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=600",
        description="Laptop profissional com processador Intel i7, 16GB RAM, SSD 512GB e tela 15.6\" Full HD."
    ),
    Product(
        id="3",
        name="Fones Wireless Premium",
        price=299.99,
        imageUrl="https://images.pexels.com/photos/3825517/pexels-photo-3825517.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Fones de ouvido sem fio com cancelamento de ruído ativo, som Hi-Fi e bateria de até 30 horas."
    ),
    Product(
        id="4",
        name="Smartwatch Fit",
        price=249.99,
        imageUrl="https://images.pexels.com/photos/393047/pexels-photo-393047.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Smartwatch com monitor de frequência cardíaca, GPS integrado e resistência à água."
    ),
    Product(
        id="5",
        name="Tablet Max",
        price=799.99,
        imageUrl="https://images.pexels.com/photos/1334597/pexels-photo-1334597.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Tablet premium com tela de 11 polegadas, processador octa-core e suporte para caneta digital."
    ),
    Product(
        id="6",
        name="Câmera Digital Pro",
        price=1299.99,
        imageUrl="https://images.pexels.com/photos/90946/pexels-photo-90946.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Câmera profissional mirrorless com sensor de 24MP, gravação 4K e lente intercambiável."
    ),
    Product(
        id="7",
        name="Console Game Plus",
        price=499.99,
        imageUrl="https://images.pexels.com/photos/371924/pexels-photo-371924.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Console de jogos de última geração com gráficos 4K, SSD ultrarrápido e controle sem fio."
    ),
    Product(
        id="8",
        name="Smart TV 4K",
        price=899.99,
        imageUrl="https://images.pexels.com/photos/1201996/pexels-photo-1201996.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Smart TV LED 55 polegadas com resolução 4K Ultra HD, HDR e sistema operacional inteligente."
    ),
    Product(
        id="9",
        name="Teclado Mecânico RGB",
        price=149.99,
        imageUrl="https://images.pexels.com/photos/1772123/pexels-photo-1772123.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Teclado mecânico gamer com iluminação RGB customizável e switches Cherry MX."
    ),
    Product(
        id="10",
        name="Mouse Gamer Pro",
        price=79.99,
        imageUrl="https://images.pexels.com/photos/2115256/pexels-photo-2115256.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Mouse gamer de alta precisão com sensor óptico de 16000 DPI e 8 botões programáveis."
    ),
    
]