# Trabajo académico 2 - Topicos de Ciencias de Computación

Problema:<br>
Se requiere que, utilizando como mínimo la ubicación de 10 hospitales, diseñar un CSP que pueda hospedar a 1000+ pacientes de Covid-19. Como restricciones, se pueden definir que:
- Cada hospital tiene una cantidad de camas y no pueden hospedar a más pacientes que esa cantidad
- Los pacientes deben priorizar el hospital más cercano a su ubicación
- Cada paciente tiene un nivel de severidad: A mayor la severidad, mayor la prioridad para ser hospedado en el hospital más cercano.

Modelo Formal:<br>
Conjuntos:<br>
•	𝐻H: Conjunto de hospitales.
•	𝑃P: Conjunto de pacientes.
•	𝐵𝑖Bi: Conjunto de camas en el hospital 𝑖i.

Parámetros:<br>
•	latitud𝑖, longitud𝑖latitudi, longitudi: Coordenadas geográficas del hospital 𝑖i.
•	latitud𝑝, longitud𝑝latitudp, longitudp: Coordenadas geográficas del paciente 𝑝p.
•	severidad𝑝severidadp: Gravedad de la enfermedad del paciente 𝑝p.
•	camas𝑖camasi: Número de camas disponibles en el hospital 𝑖i.

Variables de Decisión:<br>
•	𝑥𝑖𝑗𝑝xijp: Variable binaria que indica si la cama 𝑗j del hospital 𝑖i está asignada al paciente 𝑝p.

Función Objetivo:<br>
  Minimizar∑𝑖∈𝐻∑𝑗∈𝐵𝑖∑𝑝∈𝑃𝑥𝑖𝑗𝑝Minimizar∑i∈H∑j∈Bi∑p∈Pxijp

Restricciones:<br>
1.	Cada paciente 𝑝p debe estar asignado a exactamente una cama en un hospital: ∑𝑖∈𝐻∑𝑗∈𝐵𝑖𝑥𝑖𝑗𝑝=1,∀𝑝∈𝑃∑i∈H∑j∈Bixijp=1,∀p∈P
2.	Cada cama 𝑗j de cada hospital 𝑖i solo puede ser asignada a un paciente 𝑝p: ∑𝑝∈𝑃𝑥𝑖𝑗𝑝≤1,∀𝑖∈𝐻,∀𝑗∈𝐵𝑖∑p∈Pxijp≤1,∀i∈H,∀j∈Bi
3.	Preferencias blandas:
•	Todos los pacientes deben ser asignados a una cama disponible en el hospital más cercano.
•	Los pacientes con mayor severidad deben tener prioridad para ser asignados a camas cuando no haya suficientes disponibles.



Resultados:<br>

![](https://raw.githubusercontent.com/GonJurado/Topicos_Jurado_Diaz/main/captura_mapa.png)

Análisis de Resultados

El modelo de asignación de pacientes a hospitales utilizando programación de restricciones ha demostrado ser una herramienta eficaz para abordar la gestión de recursos durante una pandemia. A continuación, se presentan los principales hallazgos y conclusiones derivados del análisis de los resultados obtenidos:

1. Eficiencia en la asignación de recursos: El modelo ha logrado asignar de manera eficiente a cada paciente a una cama disponible en el hospital más cercano, garantizando así una utilización óptima de los recursos hospitalarios.
2. Optimización de la distancia: La consideración de la proximidad geográfica como una preferencia blanda ha permitido asignar a los pacientes a hospitales cercanos, lo que reduce los tiempos de transporte y aumenta la accesibilidad a la atención médica.
3. Priorización de pacientes críticos: La capacidad del modelo para priorizar a los pacientes con mayor severidad ha contribuido a garantizar que aquellos en condiciones más graves reciban atención médica prioritaria, incluso cuando la disponibilidad de camas es limitada.
4. Visualización de resultados: La generación de mapas 2D ha facilitado la visualización de la distribución geográfica de hospitales, pacientes y la gravedad de las enfermedades, lo que ha facilitado la comprensión y comunicación de los resultados a las partes interesadas.
5. Flexibilidad y adaptabilidad: El modelo ha demostrado ser flexible y adaptable a diferentes escenarios y condiciones cambiantes durante la pandemia, lo que lo convierte en una herramienta valiosa para la toma de decisiones informadas en situaciones de crisis de salud pública.





Conclusiones:<br>
- La programación de restricciones es esencial para modelar eficazmente la asignación de pacientes a hospitales durante una pandemia.
- Es crucial diferenciar entre restricciones duras (esenciales) y blandas (preferencias) para garantizar la viabilidad y satisfacción del modelo.
- La utilización de datos reales, como coordenadas geográficas, es fundamental para diseñar un modelo realista y efectivo.
- El modelo debe ser flexible y adaptable para enfrentar diferentes escenarios durante una crisis de salud.
- La presentación clara de resultados, incluidos mapas y análisis visuales, es crucial para comunicar conclusiones y recomendaciones a las partes interesadas.
