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

**REQUERIMIENTOS DE USUARIO**
| ID        | 21 |
| ------------- | ------------- |
|**NOMBRE**     | Procesos simples y rápidos |
|**DESCRIPCIÓN**| Garantizar que los procesos de reserva, pago y compra sean simples y rápidos | 
|**ENTRADA**    | Interacción del usuario con los procesos de reserva, pago y compra | 
|**SALIDA**     | Procesos de reserva, pago y compra completados de manera eficiente | 
|**EXCEPCIONES**| Procesos complicados, lentitud en la ejecución de las transacciones | 
|**AUTOR**      | Desarrollador de PUSP | 
|**PRIORIDAD**  | Alta |

| ID        | 22 |
| ------------- | ------------- |
|**NOMBRE**     | Seguridad y confianza |
|**DESCRIPCIÓN**| Asegurar que los estudiantes se sientan seguros al utilizar la plataforma y confíen en la privacidad de sus datos | 
|**ENTRADA**    | Interacción del usuario con la plataforma | 
|**SALIDA**     | Sensación de seguridad y confianza por parte del usuario al utilizar la plataforma | 
|**EXCEPCIONES**| Problemas de seguridad de datos, falta de transparencia en la privacidad | 
|**AUTOR**      | Desarrollador de PUSP | 
|**PRIORIDAD**  | Alta |

| ID        | 23 |
| ------------- | ------------- |
|**NOMBRE**     | Adaptabilidad a diferentes perfiles de usuario |
|**DESCRIPCIÓN**| Asegurar que la plataforma se adapte a diferentes perfiles de usuario, desde habilidades tecnológicas avanzadas hasta menos familiarizados con la tecnología | 
|**ENTRADA**    | Interacción del usuario con la plataforma | 
|**SALIDA**     | Terminal y funcionalidades adaptadas a diferentes niveles de habilidad tecnológica | 
|**EXCEPCIONES**| Problemas de usabilidad para usuarios menos familiarizados con la tecnología, falta de personalización | 
|**AUTOR**      | Desarrollador de PUSP | 
|**PRIORIDAD**  | Media |

**REQUERIMIENTOS DEL SISTEMA**
| ID        | 31 |
| ------------- | ------------- |
|**NOMBRE**     | Disponibilidad las 24/7 |
|**DESCRIPCIÓN**| Asegurar que el sistema esté disponible las 24 horas del día, los 7 días de la semana | 
|**ENTRADA**    | - | 
|**SALIDA**     | Confirmación de disponibilidad del sistema en todo momento | 
|**EXCEPCIONES**| Tiempos de inactividad no planificados, fallos en el sistema | 
|**AUTOR**      | Desarrollador de PUSP | 
|**PRIORIDAD**  | Alta |

| ID        | 32 |
| ------------- | ------------- |
|**NOMBRE**     | Protocolos de seguridad |
|**DESCRIPCIÓN**| Establecer protocolos de seguridad para proteger la información sensible y prevenir accesos no autorizados | 
|**ENTRADA**    | - | 
|**SALIDA**     | Confirmación de implementación de protocolos de seguridad robustos | 
|**EXCEPCIONES**| Violaciones de seguridad, accesos no autorizados | 
|**AUTOR**      | Desarrollador de PUSP | 
|**PRIORIDAD**  | Alta |

| ID        | 33 |
| ------------- | ------------- |
|**NOMBRE**     | Respaldo y recuperación de datos |
|**DESCRIPCIÓN**| Implementar un sistema de respaldo y recuperación de datos para garantizar la integridad de la información | 
|**ENTRADA**    | - | 
|**SALIDA**     | Confirmación de que los datos se respaldan regularmente y se pueden recuperar en caso de pérdida | 
|**EXCEPCIONES**| Fallos en el proceso de respaldo, incapacidad para recuperar datos | 
|**AUTOR**      | Desarrollador de PUSP | 
|**PRIORIDAD**  | Alta |
