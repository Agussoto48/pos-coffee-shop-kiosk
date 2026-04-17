# pos_coffee_shop_kiosk

```
Juan Gonzalez 
Jason Montenegro
Agustin Soto
```


>Sistema de punto de venta para cafeterías. 


---

## Arquitectura general

```
pos_coffee_shop_kiosk/
---domain/
------entities/
------value_objects/
------models/
------interfaces/
------factories/
------enums/
---application/
------dtos/
------use_cases/
---------inventory/
---------category/
---------pricing/
---------reporting/
---------browse_menu/
---------shopping_cart/
---------checkout/
------containers/
---infrastructure/
------repositories/
------payment_methods/
------factories/
------summary_generators/
---presentation/
---composition/
```

---

## domain

> El núcleo del sistema. Aquí viven los conceptos principales del negocio: productos, ventas, carrito, pagos y sus reglas.

---

### `domain/entities/`

> **Los objetos principales del negocio. Representan cosas reales del sistema que tienen identidad propia y cuya información puede cambiar con el tiempo.**

| Archivo | Descripción |
|---|---|
| `product.py` | Representa un producto del sistema POS. Contiene su nombre, descripción, categoría, SKU, precio, stock y opciones de impuesto. |
| `sale.py` | Representa una venta realizada. Contiene la información del carrito comprado, el método de pago, el monto pagado, el cambio, el estado y la fecha. |

---

### `domain/value_objects/`

> **Valores específicos del negocio que se usan a lo largo del sistema. En lugar de manejar strings o números sueltos, cada concepto tiene su propio tipo con validación y significado claro.**

| Archivo | Descripción |
|---|---|
| `money.py` | Representa un monto de dinero junto a su moneda. Se usa en precios, pagos y cambios. |
| `sku.py` | Representa el código comercial de un producto. |
| `product_name.py` | Representa el nombre de un producto. |
| `product_category.py` | Representa la categoría de un producto. Soporta jerarquía con categoría padre para manejar subcategorías. |
| `category_name.py` | Representa el nombre de una categoría. |
| `percentage.py` | Representa un porcentaje. Se usa principalmente en el cálculo de impuestos. |
| `tax_description.py` | Representa la descripción de un impuesto. |
| `tax_option.py` | Representa una opción de impuesto, compuesta por una descripción y un porcentaje. |

---

### `domain/models/`

> **Modelos que agrupan la lógica del flujo de compra. Aquí vive el comportamiento del carrito y sus ítems.**

| Archivo | Descripción |
|---|---|
| `shopping_cart.py` | Modela el carrito de compras. Permite agregar, remover y limpiar ítems, buscar productos y calcular el total. |
| `cart_item.py` | Modela un ítem dentro del carrito. Relaciona un producto con una cantidad y calcula su subtotal. |

---

### `domain/interfaces/`

> **Define qué operaciones necesita el sistema para funcionar: guardar productos, registrar ventas, procesar pagos, entre otras. Cada interfaz es el molde que las implementaciones concretas deben cumplir.**

| Archivo | Descripción |
|---|---|
| `abstract_product_repository.py` | Operaciones para gestionar productos: agregar, remover, buscar por SKU y obtener por categoría. |
| `abstract_sale_repository.py` | Operaciones para guardar y consultar ventas. |
| `abstract_tax_option_repository.py` | Operaciones para administrar las opciones de impuesto. |
| `abstract_product_category_repository.py` | Operaciones para gestionar las categorías de producto. |
| `abstract_payment_method.py` | Define la operación de ejecutar un pago. Cualquier método de pago del sistema debe cumplirla. |
| `abstract_summary_report_generator.py` | Define la operación de generar un reporte resumen. |

---

### `domain/factories/`

> **Define cómo se deben crear los métodos de pago, sin especificar la lógica concreta de construcción. Eso queda en la capa de infraestructura.**

| Archivo | Descripción |
|---|---|
| `abstract_payment_method_factory.py` | Define una fábrica para crear métodos de pago a partir de un tipo de pago y los datos del cliente. |
| `abstract_payment_factory.py` | Define una fábrica más específica para construir una implementación concreta de método de pago a partir de los datos de entrada. |

---

### `domain/enums/`

> **Listas cerradas de valores válidos para conceptos del negocio como monedas, estados de venta y tipos de pago.**

| Archivo | Descripción |
|---|---|
| `currency.py` | Monedas soportadas por el sistema. |
| `sale_status.py` | Estados posibles de una venta: pendiente, exitosa o fallida. |
| `payment_method_type.py` | Tipos de pago disponibles: efectivo, tarjeta y tap. |

---

## application

> Coordina los flujos del sistema. Cada caso de uso representa una acción concreta que el sistema puede realizar, como registrar un producto, agregar algo al carrito o procesar un pago.

---

### `application/dtos/`

> **Son los encargados de transportar información entre capas. Se usan para recibir datos de entrada y devolver datos de salida sin exponer directamente las entidades del negocio.**

| Archivo | Descripción |
|---|---|
| `register_product_request.py` | Datos necesarios para registrar un nuevo producto. |
| `update_product_request.py` | Datos necesarios para actualizar un producto existente. |
| `product_details.py` | Información de un producto lista para mostrarse o devolverse. |
| `client_payment_details.py` | Información que el cliente entrega para efectuar un pago: efectivo, datos de tarjeta, etc. |
| `tax_option_response.py` | Información de una opción de impuesto lista para devolverse. |
| `shopping_cart_summary.py` | Resumen general del estado actual del carrito. |
| `cart_item_summary.py` | Resumen de un ítem individual dentro del carrito. |

---

### `application/use_cases/inventory/`

> **Casos de uso para gestionar el catálogo de productos del negocio.**

| Archivo | Descripción |
|---|---|
| `register_product.py` | Registra un nuevo producto en el sistema. |
| `remove_product.py` | Elimina un producto existente. |
| `update_product.py` | Actualiza la información de un producto. |
| `find_product.py` | Busca y retorna un producto específico. |

---

### `application/use_cases/category/`

> **Casos de uso para organizar los productos en categorías y subcategorías.**

| Archivo | Descripción |
|---|---|
| `add_category.py` | Agrega una categoría principal. |
| `remove_category.py` | Elimina una categoría principal. |
| `add_sub_category.py` | Agrega una subcategoría dentro de una categoría existente. |
| `remove_sub_category.py` | Elimina una subcategoría. |
| `fetch_category_names.py` | Obtiene los nombres de las categorías disponibles. |
| `fetch_sub_category_names.py` | Obtiene los nombres de las subcategorías disponibles. |

---

### `application/use_cases/pricing/`

> **Casos de uso para configurar las opciones de impuesto que se aplican a los productos.**

| Archivo | Descripción |
|---|---|
| `add_tax_option.py` | Agrega una nueva opción de impuesto. |
| `remove_tax_option.py` | Elimina una opción de impuesto existente. |
| `fetch_tax_options.py` | Obtiene las opciones de impuesto disponibles. |

---

### `application/use_cases/reporting/`

> **Casos de uso para generar reportes de actividad del sistema.**

| Archivo | Descripción |
|---|---|
| `generate_summary_report.py` | Genera un reporte resumen con la información de ventas y actividad del sistema. |

---

### `application/use_cases/browse_menu/`

> **Casos de uso para consultar el menú de productos desde el kiosco.**

| Archivo | Descripción |
|---|---|
| `fetch_product_menu.py` | Obtiene el listado de productos disponibles para mostrar en la pantalla del kiosco. |

---

### `application/use_cases/shopping_cart/`

> **Casos de uso que gestionan todo lo relacionado al carrito del cliente durante la compra.**

| Archivo | Descripción |
|---|---|
| `add_cart_item.py` | Agrega un ítem al carrito. |
| `remove_cart_item.py` | Elimina un ítem del carrito. |
| `clear_cart.py` | Vacía completamente el carrito. |
| `fetch_cart_summary.py` | Obtiene el resumen actual del carrito. |

---

### `application/use_cases/checkout/`

> **Casos de uso que manejan el cierre de la compra y el procesamiento del pago.**

| Archivo | Descripción |
|---|---|
| `process_checkout.py` | Coordina el flujo completo de checkout: valida el carrito, procesa el pago y registra la venta. |
| `create_payment_method.py` | Crea el método de pago adecuado según el tipo seleccionado y los datos entregados por el cliente. |

---

### `application/containers/`

> **Agrupan los casos de uso según el contexto donde se usan, para que sea más fácil inyectarlos en la capa de presentación.**

| Archivo | Descripción |
|---|---|
| `administrator_app_use_cases.py` | Casos de uso disponibles para la app de administración. |
| `kiosk_app_use_cases.py` | Casos de uso disponibles para la app del kiosco. |
| `product_inventory_use_cases.py` | Casos de uso de inventario agrupados. |
| `product_category_use_cases.py` | Casos de uso de categorías agrupados. |
| `pricing_options_use_cases.py` | Casos de uso de impuestos y precios agrupados. |
| `reporting_use_cases.py` | Casos de uso de reportes agrupados. |
| `browse_menu_use_cases.py` | Casos de uso de exploración del menú agrupados. |
| `shopping_cart_use_cases.py` | Casos de uso del carrito agrupados. |
| `checkout_use_cases.py` | Casos de uso del checkout agrupados. |

---

## infrastructure

> Aquí están las implementaciones reales del sistema: cómo se guardan los datos, cómo se procesan los pagos y cómo se generan los archivos de reporte.

---

### `infrastructure/repositories/`

> **Implementaciones concretas de cada repositorio. Guardan y leen los datos del sistema usando archivos JSON.**

| Archivo | Descripción |
|---|---|
| `json_product_repository.py` | Guarda y consulta productos en un archivo JSON. |
| `json_product_category_repository.py` | Guarda y consulta categorías en un archivo JSON. |
| `json_tax_option_repository.py` | Guarda y consulta opciones de impuesto en un archivo JSON. |
| `json_sale_repository.py` | Guarda y consulta ventas en un archivo JSON. |

---

### `infrastructure/payment_methods/`

> **Implementaciones concretas de cada método de pago soportado por el sistema.**

| Archivo | Descripción |
|---|---|
| `cash_payment_method.py` | Procesa pagos en efectivo. |
| `tap_card_payment_method.py` | Procesa pagos por tarjeta sin contacto (tap). |
| `card_payment_method.py` | Procesa pagos con tarjeta tradicional. |

---

### `infrastructure/factories/`

> **Se encargan de construir el objeto de método de pago correcto según el tipo de pago seleccionado por el cliente.**

| Archivo | Descripción |
|---|---|
| `basic_payment_method_factory.py` | Fábrica principal. Recibe el tipo de pago y delega la construcción al factory específico. |
| `cash_payment_factory.py` | Construye el método de pago en efectivo. |
| `tap_card_payment_factory.py` | Construye el método de pago tap. |
| `card_payment_factory.py` | Construye el método de pago con tarjeta. |

---

### `infrastructure/summary_generators/`

> **Implementaciones concretas para generar reportes en distintos formatos.**

| Archivo | Descripción |
|---|---|
| `txt_summary_report_generator.py` | Genera el reporte resumen como archivo de texto plano. |

---

## presentation

> Puntos de entrada de la aplicación. Recibe las acciones del usuario, llama a los casos de uso correspondientes y muestra los resultados. No tiene lógica de negocio.

| Archivo | Descripción |
|---|---|
| `pos_app.py` | Coordinador general de la aplicación. |
| `pos_administrator_app.py` | Interfaz del panel de administración: productos, categorías, impuestos y reportes. |
| `pos_kiosk_app.py` | Interfaz del kiosco: exploración del menú, carrito y checkout. |

---

## composition

> Ensambla y conecta todas las piezas del sistema. Instancia los repositorios, factories, generadores y casos de uso, dejando todo listo para funcionar.

| Archivo | Descripción |
|---|---|
| `create_use_cases.py` | Construye e inyecta todas las dependencias del sistema, conectando cada interfaz con su implementación real. |



# 2. Aplicación de los principios SOLID

## Single Responsibility Principle

El principio de responsabilidad única establece que cada clase debe tener una sola razón para cambiar. En este sistema, este principio se cumple mediante una clara separación de responsabilidades entre entidades, value objects, repositorios, casos de uso, factories y componentes de infraestructura.

Las entidades como `Product` y `Sale` se encargan exclusivamente de representar y gestionar el estado del dominio. Los value objects como `Money`, `Sku`, `ProductName`, `CategoryName`, `Percentage` y `TaxDescription` encapsulan valores específicos con reglas propias.

Los casos de uso como `RegisterProduct`, `AddCartItem`, `ProcessCheckout` o `GenerateSummaryReport` encapsulan acciones específicas del sistema, sin asumir responsabilidades adicionales. De igual forma, las factories abstractas (`AbstractPaymentMethodFactory`, `AbstractPaymentFactory`) definen contratos de creación, y las factories concretas (`BasicPaymentMethodFactory`, `CashPaymentFactory`, `TapCardPaymentFactory`, `CardPaymentFactory`) se encargan únicamente de construir los objetos de pago.

## Open/Closed Principle

Este principio indica que el sistema debe estar abierto a extensión pero cerrado a modificación. Esto se logra en el diseño mediante el uso de abstracciones.

La incorporación de nuevos métodos de pago puede realizarse creando una nueva clase que implemente `AbstractPaymentMethod`, junto con su factory correspondiente que implemente `AbstractPaymentFactory`, y registrándola en la factory principal. De esta forma, no es necesario modificar los casos de uso ni las clases existentes.

De igual forma, los repositorios pueden cambiar su implementación creando nuevas clases que implementen interfaces como `AbstractProductRepository` o `AbstractSaleRepository`, sin alterar la lógica de negocio. También se pueden agregar nuevos generadores de reportes implementando `AbstractSummaryReportGenerator`.

## Liskov Substitution Principle

El principio de sustitución de Liskov establece que cualquier implementación concreta debe poder reemplazar a su abstracción sin afectar el comportamiento del sistema.

En este diseño, las implementaciones de repositorios (`JsonProductRepository`, `JsonProductCategoryRepository`, `JsonTaxOptionRepository`, `JsonSaleRepository`) pueden ser utilizadas en cualquier lugar donde se espere su respectiva interfaz abstracta. De igual forma, las clases de métodos de pago (`CashPaymentMethod`, `TapCardPaymentMethod`, `CardPaymentMethod`) pueden ser utilizadas como instancias de `AbstractPaymentMethod`. También se puede con `TxtSummaryReportGenerator`, que puede sustituir a `AbstractSummaryReportGenerator`, y con las factories concretas que cumplen los contratos de `AbstractPaymentFactory` y `AbstractPaymentMethodFactory`.

## Interface Segregation Principle

El principio de segregación de interfaces establece que las clases no deben verse obligadas a depender de interfaces que no utilizan. Este principio se refleja en el diseño mediante el uso de múltiples interfaces pequeñas y específicas en lugar de una interfaz general y extensa.

El sistema define interfaces separadas para productos, ventas, categorías, impuestos, métodos de pago y generación de reportes, como `AbstractProductRepository`, `AbstractSaleRepository`, `AbstractTaxOptionRepository`, `AbstractProductCategoryRepository`, `AbstractPaymentMethod` y `AbstractSummaryReportGenerator`.

## Dependency Inversion Principle

El principio de inversión de dependencias establece que los módulos de alto nivel no deben depender de módulos de bajo nivel, sino de abstracciones.

En este sistema, los casos de uso y la lógica de aplicación dependen de interfaces como los repositorios abstractos, las interfaces de métodos de pago, los generadores de reportes y las factories abstractas. No al revés como sería el caso de depender directamente de `JsonProductRepository`, `CashPaymentMethod`, `CardPaymentMethod` o `TxtSummaryReportGenerator`.