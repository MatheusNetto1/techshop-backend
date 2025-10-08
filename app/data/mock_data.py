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
    Product(
        id="11",
        name="Caixa de Som Bluetooth",
        price=119.99,
        imageUrl="https://images.pexels.com/photos/3394656/pexels-photo-3394656.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Caixa de som portátil com graves potentes, conexão Bluetooth 5.0 e bateria de até 12 horas."
    ),
    Product(
        id="12",
        name="Monitor UltraWide 34''",
        price=699.99,
        imageUrl="https://images.pexels.com/photos/572056/pexels-photo-572056.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Monitor ultrawide curvo de 34 polegadas com resolução QHD, 144Hz e tecnologia FreeSync."
    ),
    Product(
        id="13",
        name="Cadeira Gamer Xtreme",
        price=349.99,
        imageUrl="https://images.pexels.com/photos/845434/pexels-photo-845434.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Cadeira gamer ergonômica com apoio lombar, regulagem de altura e revestimento em couro sintético."
    ),
    Product(
        id="14",
        name="Roteador Wi-Fi 6 Pro",
        price=199.99,
        imageUrl="https://images.pexels.com/photos/4218543/pexels-photo-4218543.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Roteador de alta performance com suporte ao padrão Wi-Fi 6, 4 antenas e controle via app."
    ),
    Product(
        id="15",
        name="Headset Gamer Surround",
        price=179.99,
        imageUrl="https://images.pexels.com/photos/3945658/pexels-photo-3945658.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Headset com som surround 7.1, microfone com cancelamento de ruído e almofadas confortáveis."
    ),
    Product(
        id="16",
        name="Impressora Multifuncional",
        price=229.99,
        imageUrl="https://images.pexels.com/photos/38568/office-freelancer-computer-business-38568.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Impressora multifuncional com Wi-Fi, impressão frente e verso automática e scanner de alta resolução."
    ),
    Product(
        id="17",
        name="SSD NVMe 1TB",
        price=159.99,
        imageUrl="https://images.pexels.com/photos/5720569/pexels-photo-5720569.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="SSD NVMe com 1TB de capacidade, velocidade de leitura de até 3500MB/s e 5 anos de garantia."
    ),
    Product(
        id="18",
        name="Microfone Condensador Studio",
        price=249.99,
        imageUrl="https://images.pexels.com/photos/5690501/pexels-photo-5690501.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Microfone condensador profissional para gravação e streaming com suporte e filtro pop."
    ),
    Product(
        id="19",
        name="Câmera de Segurança Wi-Fi",
        price=139.99,
        imageUrl="https://images.pexels.com/photos/1334602/pexels-photo-1334602.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Câmera IP com visão noturna, detecção de movimento e armazenamento em nuvem."
    ),
    Product(
        id="20",
        name="Carregador Portátil 20.000mAh",
        price=89.99,
        imageUrl="https://images.pexels.com/photos/4218542/pexels-photo-4218542.jpeg?auto=compress&cs=tinysrgb&w=600",
        description="Powerbank de alta capacidade com carregamento rápido, duas portas USB e indicador LED."
    ),
]