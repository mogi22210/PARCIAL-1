**REQUERIMIENTOS FUNCIONALES**
| ID        | 01 |
| ------------- | ------------- |
|**NOMBRE**     | Inicio de Sesión y Registro       |
|**DESCRIPCIÓN**| Permitir a los estudiantes iniciar sesión o registrarse en la plataforma   | 
|**ENTRADA**    | Nombre de usuario, contraseña (para inicio de sesión), información de registro (para registro) | 
|**SALIDA**     | Acceso a la plataforma (para inicio de sesión), confirmación de registro exitoso | 
|**EXCEPCIONES**| Error si las credenciales son incorrectas (para inicio de sesión), error si ya existe un usuario con el mismo nombre (para registro), errores de conexión | 
|**AUTOR**      | Desarrollador de PUSP | 
|**PRIORIDAD**  | Alta | 


| ID        | 02 |
| ------------- | ------------- |
|**NOMBRE**     | Generación de reportes       |
|**DESCRIPCIÓN**| Permitir a las cuentas administradoras generar reportes sobre la usabilidad de los productos, las compras recientes o reservas de bicicleta   | 
|**ENTRADA**    | Parámetros de selección para el tipo de reporte (usabilidad de productos, compras recientes, reservas de bicicleta) | 
|**SALIDA**     | Reporte generado en terminal | 
|**EXCEPCIONES**| Error si no hay datos disponibles para generar el reporte seleccionado | 
|**AUTOR**      | Desarrollador de PUSP | 
|**PRIORIDAD**  | Alta | 


| ID        | 03 |
| ------------- | ------------- |
|**NOMBRE**     | Reserva de bicicletas       |
|**DESCRIPCIÓN**| Permitir a los estudiantes reservar bicicletas para desplazarse por el campus   | 
|**ENTRADA**    | Selección de bicicleta, fecha y hora de reserva | 
|**SALIDA**     | Confirmación de reserva exitosa | 
|**EXCEPCIONES**| Error si no hay bicicletas disponibles | 
|**AUTOR**      | Desarrollador de PUSP | 
|**PRIORIDAD**  | Alta | 

**REQUERIMIENTOS NO FUNCIONALES**
| ID        | 11 |
| ------------- | ------------- |
|**NOMBRE**     | Usabilidad       |
|**DESCRIPCIÓN**| Garantizar que la interfaz de usuario sea intuitiva y fácil de usar	   | 
|**ENTRADA**    | Interacción del usuario con la interfaz | 
|**SALIDA**     | Retroalimentación clara y guía eficiente a través de los procesos | 
|**EXCEPCIONES**| Errores de navegación, falta de claridad en las instrucciones | 
|**AUTOR**      | Desarrollador de PUSP | 
|**PRIORIDAD**  | Alta |

| ID        | 12 |
| ------------- | ------------- |
|**NOMBRE**     | Disponibilidad       |
|**DESCRIPCIÓN**| Garantizar que el sistema esté disponible en todo momento	   | 
|**ENTRADA**    | - | 
|**SALIDA**     | Confirmación de disponibilidad del sistema | 
|**EXCEPCIONES**| Fallos en la conexión, tiempos de inactividad no planificados | 
|**AUTOR**      | Desarrollador de PUSP | 
|**PRIORIDAD**  | Alta |

| ID        | 13 |
| ------------- | ------------- |
|**NOMBRE**     | Rendimiento      |
|**DESCRIPCIÓN**| Asegurar que el sistema pueda manejar un gran volumen de transacciones simultáneas sin retrasos significativos	   | 
|**ENTRADA**    | Carga del sistema con múltiples transacciones simultáneas | 
|**SALIDA**     | Respuesta rápida del sistema sin retrasos perceptibles | 
|**EXCEPCIONES**| Tiempos de espera prolongados, errores de procesamiento | 
|**AUTOR**      | Desarrollador de PUSP | 
|**PRIORIDAD**  | Alta |
