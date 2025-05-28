# EventSync

Guía de instalación y puesta en marcha en un equipo nuevo.

## 1. Pre-requisitos

- **Git**  
- **Python 3.10+**  
- **MariaDB**  

## 2. Clonar el repositorio

```bash
git clone https://github.com/AldoIs/eventsync.git EventSync
cd EventSync
```

## 3. Crear y activar el entorno virtual

**Windows (PowerShell)**

```powershell
python -m venv venv
venv\Scripts\activate
```

## 4. Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Configurar la conexión a MariaDB

Edita `eventsys/settings.py`, sección `DATABASES`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eventsys',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```


## 6. Crear la base de datos y el usuario en MariaDB

Conéctate al cliente de MariaDB y ejecuta:

```sql
CREATE DATABASE IF NOT EXISTS eventsys
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE USER 'tu_usuario'@'localhost' IDENTIFIED BY 'tu_contraseña';
GRANT ALL PRIVILEGES ON eventsys.* TO 'tu_usuario'@'localhost';
FLUSH PRIVILEGES;
```

## 7. Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

## 8.  Cargar datos de ejemplo


  ```bash
 python manage.py shell
from django.contrib.auth import get_user_model
from services.models import Service
from orders.models import Order, OrderItem

User = get_user_model()

# —————— Crear usuarios de prueba ——————
users = [
    {'username': 'alice', 'email': 'alice@example.com', 'password': 'Passw0rd!', 'telefono': '555-1001'},
    {'username': 'bob',   'email': 'bob@example.com',   'password': 'Passw0rd!', 'telefono': '555-1002'},
    {'username': 'carol', 'email': 'carol@example.com', 'password': 'Passw0rd!', 'telefono': '555-1003'},
]
for u in users:
    if not User.objects.filter(username=u['username']).exists():
        user = User.objects.create_user(
            username=u['username'],
            email=u['email'],
            password=u['password'],
            telefono=u['telefono']
        )
        print(f"Usuario creado: {user.username}")

# —————— Crear servicios de prueba ——————
servicios = [
    {'nombre': 'Sonido Básico',     'descripcion': 'Equipo de sonido para eventos pequeños',    'precio': 500.00, 'imagen_url': 'https://placehold.co/200x100?text=Sonido'},
    {'nombre': 'Barra de Bebidas',  'descripcion': 'Bartender y bar completo',                     'precio': 1200.00,'imagen_url': 'https://placehold.co/200x100?text=Bebidas'},
    {'nombre': 'Catering Estándar', 'descripcion': 'Menú de comida para 50 personas',               'precio': 2500.00,'imagen_url': 'https://placehold.co/200x100?text=Catering'},
    {'nombre': 'Decoración',        'descripcion': 'Globos, luces y adornos temáticos',             'precio': 800.00, 'imagen_url': 'https://placehold.co/200x100?text=Deco'},
    {'nombre': 'Fotografía',        'descripcion': 'Sesión fotográfica profesional durante el evento','precio': 1500.00,'imagen_url': 'https://placehold.co/200x100?text=Foto'},
]
for s in servicios:
    svc, created = Service.objects.get_or_create(nombre=s['nombre'], defaults={
        'descripcion': s['descripcion'],
        'precio': s['precio'],
        'imagen_url': s['imagen_url']
    })
    if created:
        print(f"Servicio creado: {svc.nombre}")

# —————— Crear pedidos de prueba ——————
# Pedido de Alice con dos servicios
alice = User.objects.get(username='alice')
order1, _ = Order.objects.get_or_create(user=alice, estado='pending')
svc_sonido = Service.objects.get(nombre='Sonido Básico')
svc_barra  = Service.objects.get(nombre='Barra de Bebidas')
OrderItem.objects.get_or_create(order=order1, service=svc_sonido, defaults={'cantidad': 1, 'precio_unitario': svc_sonido.precio})
OrderItem.objects.get_or_create(order=order1, service=svc_barra,  defaults={'cantidad': 2, 'precio_unitario': svc_barra.precio})
print(f"Pedido #{order1.id} para {alice.username} con items: {[i.service.nombre for i in order1.items.all()]}")

# Pedido de Bob con un servicio
bob = User.objects.get(username='bob')
order2, _ = Order.objects.get_or_create(user=bob, estado='paid')
svc_catering = Service.objects.get(nombre='Catering Estándar')
OrderItem.objects.get_or_create(order=order2, service=svc_catering, defaults={'cantidad': 1, 'precio_unitario': svc_catering.precio})
print(f"Pedido #{order2.id} para {bob.username} con items: {[i.service.nombre for i in order2.items.all()]}")

  ```


## 9. Crear superusuario

```bash
python manage.py createsuperuser
```

Sigue las indicaciones para usuario, email y contraseña.

## 10. Arrancar el servidor de desarrollo

```bash
python manage.py runserver
```

- **App:** http://127.0.0.1:8000/  
- **Admin:** http://127.0.0.1:8000/admin/  

---

¡Listo! Con estos pasos tendrás EventSync funcionando en tu nuevo equipo.
